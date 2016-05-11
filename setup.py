import os, sys

local = False # Default

if 'DYNO' not in os.environ:
    local = True
    
if local == False:
    consumer_key = os.environ['consumer_key']
    consumer_secret = os.environ['consumer_secret']
    access_token_key = os.environ['access_token_key']
    access_token_secret = os.environ['access_token_secret']
    
elif local == True:
    import localsetup
    consumer_key = localsetup.consumer_key 
    consumer_secret = localsetup.consumer_secret
    access_token_key = localsetup.access_token_key
    access_token_secret = localsetup.access_token_secret