import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries



def load_staging_tables(cur, conn):
 """
This will load data into staging_tables from S3 Bucket using the queries declared on the sql_queries script
"""
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


        
        
def insert_tables(cur, conn):
"""
Inserts data from staging tables into the dimensional tables using the queries declared on the sql_queries script
"""        
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    
""" Loads configs from dwh.cfg and start loading data from S3 to staging_tables created using create_tables.py and   transform the data and loads it into dimension tables"""


    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()