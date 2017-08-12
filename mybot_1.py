import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

tweetlist = ['test tweet one!', 'test tweet two!', 'test tweet three!']

for line in tweetlist:
    api.update_status(line)
    print(line, '- printed')
    print('...')
    time.sleep(15)

print('All done!')
