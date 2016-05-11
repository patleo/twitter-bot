import os
import psycopg2
import urlparse
import datetime

class DBWrapper:
    def __init__(self):
        urlparse.uses_netloc.append("postgres")
        url = urlparse.urlparse(os.environ["DATABASE_URL"])

        self.conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
        )
    
    def add_twitter_row(self, twitter_handles, twitter_followers):
        """Splits sql statement into 2 parts to populate appropriate field/value then commits it to db"""
        cur = self.conn.cursor()
        comm = "INSERT INTO Twitter (DateCreated, "
        for i in range(len(twitter_handles)):
            if i < (len(twitter_handles) - 1):
                comm += "{},".format(twitter_handles[i])
            else:
                comm += "{})".format(twitter_handles[i])
                
        comm += "VALUES( {},".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        for i in range(len(twitter_followers)):
            if i < (len(twitter_handles) - 1):
                comm += "{},".format(twitter_followers[i])
            else:
                comm += "{});".format(twitter_followers[i])
                
        cur.execute(comm)
        self.conn.commit()
    
    def seed_companies_table(self, twitter_handle, stock_ticker, forbes_rank):
        cur = self.conn.cursor()
        cur.execute('CREATE TABLE Companies (id INTEGER PRIMARY KEY, Twitter varchar(255), Ticker varchar(255), Rank int);')
        for i in range(len(twitter_handle)):
            comm = "INSERT INTO Companies (id, Twitter, Ticker, Rank) VALUES({},'{}','{}',{})".format(i+1 ,twitter_handle[i], stock_ticker[i], forbes_rank[i])
            cur.execute(comm)
            
        self.conn.commit()
    
    def seed_twitter_table(self, twitter_handle):
        cur = self.conn.cursor()
        cur.execute('CREATE TABLE Twitter (DateCreated timestamp);')
        for i in range(len(twitter_handle)):
            comm = "ALTER TABLE Twitter ADD COLUMN {} BIGINT;".format(twitter_handle[i])
            cur.execute(comm)
        self.conn.commit()
            
    def return_table(self, table_name):
        table = []
        cur = self.conn.cursor()
        comm = 'SELECT * FROM {}'.format(table_name)
        cur.execute(comm)
        for row in cur:
            table.append(row)
        return table
    
    def close_conn(self):
        self.conn.close()
