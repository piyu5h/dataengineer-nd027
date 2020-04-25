import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """This function read JSON files of song and artist data and saves into Song and Artist row by row.
        Arguments:
        cur: Cursor of sparkifydb
        filepath: path of JSON file
        Return: None
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    for value in df.values:
        artist_id, artist_latitude, artist_location, artist_longitude, artist_name, duration, num_songs, song_id, title, year = value

        # insert artist record
        if artist_id is not None:
            artist_data = [artist_id, artist_name, artist_location, artist_longitude, artist_latitude]
            cur.execute(artist_table_insert, artist_data)

        # insert song record
        if song_id is not None:
            song_data = [song_id, title, artist_id, year, duration]
            cur.execute(song_table_insert, song_data)


def process_log_file(cur, filepath):
    """ This function read JSON Files of Activity of User and filters by NextSong, selects needed fields, transforms them and inserts
    them into Time, Users and SongPlay.
    Parameters:
                cur:  Cursor of the sparkifydb 
                filepath: Path of JSON File
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page']=='NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms') 
    
    # insert time data records
    time_data = []
    for timerecord in t:
        time_data.append([timerecord, timerecord.hour, timerecord.day, timerecord.week, timerecord.month, timerecord.year])
    column_labels = ('start_time', 'hour', 'day', 'week', 'month', 'year')
    time_df = pd.DataFrame.from_records(time_data, columns=column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
            # insert valid songplay record
            songplay_data = (index, pd.to_datetime(row.ts, unit='ms'), row.level, songid,int(row.userId),artistid, row.sessionId, row.location, row.userAgent)
            cur.execute(songplay_table_insert, songplay_data)
        

def process_data(cur, conn, filepath, func):
    """Iterate all files nested under filepath, and processes all json files found.
    Parameters:
        cur : Cursor of the sparkifydb 
        conn : Connectio to the sparkifycdb database
        filepath : Filepath parent of the logs to be analyzed
        func : Function to be used to process each json file  
    Returns:
        Name of files processed
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))
    
    return all_files


def main():
    """This Function will be used to perform ETL operation of this project. """
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()