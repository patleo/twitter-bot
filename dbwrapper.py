import os
import psycopg2
import urlparse

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
        
    def seed_companies_table(self, twitter_handle, stock_ticker, forbes_rank):
        cur = self.conn.cursor()
        cur.execute('CREATE TABLE Companies (id INTEGER PRIMARY KEY, Twitter varchar(255), Ticker varchar(255), Rank int);')
        for i in range(len(twitter_handle)):
            comm = "INSERT INTO Companies (id, Twitter, Ticker, Rank) VALUES({},'{}','{}',{})".format(i+1 ,twitter_handle[i], stock_ticker[i], forbes_rank[i])
            cur.execute(comm)
            
        self.conn.commit()
        self.conn.close()
    
    def seed_twitter_table(self, twitter_handle)
        cur = self.conn.cursor()
        cur.execute('CREATE TABLE Twitter')
        for i in range(len(twitter_handle)):
            comm = "ALTER TABLE Twitter ADD COLUMN '{}' BIGINT;".format(twitter_handle[i])
            cur.execute(comm)
        self.conn.commit()
        self.conn.close()
        
    def query(self):
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM Companies')
        for row in cur:
            print row
    
    def print_table(self, table_name):
        cur = self.conn.cursor()
        comm = 'SELECT * FROM {}'.format(table_name)
        cur.execute(comm)
        for row in cur:
            print row
