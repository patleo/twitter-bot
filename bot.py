from TwitterAPI import TwitterAPI
import setup

api = TwitterAPI(setup.consumer_key, setup.consumer_secret, setup.access_token_key, setup.access_token_secret)

r = api.request('users/show', {'screen_name':'walmart'})

for item in r:
    print item['followers_count']

from dbwrapper import DBWrapper
db = DBWrapper()
db.print_table('Twitter')



