from TwitterAPI import TwitterAPI
import setup
from dbwrapper import DBWrapper
from twitterclasses import Company


db = DBWrapper()
company_table = db.return_table('Companies')
company_list = []

# Returns company info from Company table and adds necessary info to list of companies
for comp in company_table:
    c = Company(comp[1], comp[2]) 
    company_list.append(c)

# Sets up Twitter auth    
api = TwitterAPI(setup.consumer_key, setup.consumer_secret, setup.access_token_key, setup.access_token_secret)  

# Goes through list of companies and makes twitter api request to return followers count
for comp in company_list:
    r = api.request('users/show', {'screen_name': comp.twitter_handle})
    for item in r:
        comp.followers_count = item['followers_count']

# Creates two lists to feed the Twitter table
twitter_handles = []
twitter_followers = []

for comp in company_list:
    twitter_handles.append(comp.twitter_handle)
    twitter_followers.append(comp.followers_count)
    
db.add_twitter_row(twitter_handles, twitter_followers)

db.close_conn()