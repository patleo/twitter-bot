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
        cur = conn.cursor()
        cur.execute('CREATE TABLE Companies (Twitter varchar(255), Ticker varchar(255), Rank int);')
        for i in range(len(twitter_handle)):
            comm = "INSERT INTO Companies VALUES({},{},{})".format(twitter_handle[i], stock_ticker[i], forbes_rank[i])
            cur.execute(comm)
            
            