
import sys
import snscrape.modules.twitter as sntwitter
import pandas as pd

query = sys.argv[1]
tweets = []
limit = 15

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.content, tweet.user.username, tweet.user.displayname, tweet.url])

df = pd.DataFrame(tweets, columns=['Date', 'Tweet', 'Handle', 'Display Name', 'Tweet Url'])
print(df)

df.to_csv(query+'.csv')