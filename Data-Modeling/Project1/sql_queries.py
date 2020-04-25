# DROP TABLES

songplay_table_drop = "drop table IF EXISTS SongPlay"
user_table_drop = "drop table IF EXISTS Users"
song_table_drop = "drop table IF EXISTS Song"
artist_table_drop = "drop table IF EXISTS Artist"
time_table_drop = "drop table IF EXISTS Time"


# CREATE TABLES

songplay_table_create = (""" 
    CREATE TABLE IF NOT EXISTS SongPlay (
    songplayid SERIAL PRIMARY KEY,
    starttime TIMESTAMP,
    level VARCHAR(5),
    songid_fk VARCHAR(25) NOT NULL,
    userid_fk INTEGER NOT NULL,
    artistid_fk VARCHAR(25) NOT NULL,
    sessionid INTEGER,
    location VARCHAR(70),
    useragent VARCHAR(200)
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS Users (
    userid_pk INTEGER PRIMARY KEY,
    firstname VARCHAR(15),
    lastname VARCHAR(15),
    user_gender CHAR(1),
    user_level VARCHAR(10)
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS Song (
    songid_pk VARCHAR(25) PRIMARY KEY,
    title VARCHAR(100),
    artistid_fk VARCHAR(25) NOT NULL,
    year INTEGER,
    duration NUMERIC
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS Artist (
    artistid_pk VARCHAR(25) PRIMARY KEY,
    artist_name VARCHAR(100),
    location VARCHAR(100),
    latitude FLOAT(5),
    longitude FLOAT(5)
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS Time (
    starttime TIMESTAMP PRIMARY KEY,
    hour INTEGER,
    day INTEGER,
    week INTEGER,
    month INTEGER,
    year INTEGER
    );
""")


# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO SongPlay (songplayid,starttime,level,songid_fk,userid_fk,artistid_fk,sessionid,location,useragent) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)  ON CONFLICT (songplayid) DO NOTHING;
""")

user_table_insert = ("""
INSERT INTO Users (userid_pk ,firstname, lastname,user_gender, user_level) values (%s,%s,%s,%s,%s) ON CONFLICT (userid_pk) DO UPDATE SET user_level=EXCLUDED.user_level;
""")

song_table_insert = ("""
INSERT INTO Song (songid_pk,title,artistid_fk,year,duration) VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO Artist (artistid_pk ,artist_name,location,latitude,longitude) VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO Time (starttime, hour, day, week, month, year)
VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""select songid_pk,artistid_fk from Song JOIN Artist ON Song.artistid_fk=Artist.artistid_pk where title=%s and artist_name=%s and duration= %s  ;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]