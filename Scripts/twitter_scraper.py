import pandas as pd
import snscrape.modules.twitter as twitter

def tweet_getter(query,limit,start_date,end_date,replies=False):
    """
    A function to extract tweets from twitter.

    Args:

    query: topic you may be interested in (Any)
    limit: maximum number of tweets (Int) 
    start_time (Datetime): earliest time period for the tweets (Format{YYYY-MM-DD})
    end_time (Datetime): latest time period for the tweets (Format{YYYY-MM-DD})
    replies (Boolean): to filter replies. It will include replies if True.
    """
    if replies is False:
        item = f'{query} lang:en until:{end_date} since:{start_date} -filter:replies'
    elif replies is True:
        item = f'{query} lang:en until:{end_date} since:{start_date}'

    tweets = []

    for tweet in twitter.TwitterSearchScraper(item).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append({
            'Date':tweet.date,
            'Username':tweet.user.username,
            'Content':tweet.content,
            'Language':tweet.lang,
            'Replies':tweet.replyCount,
            'Like':tweet.likeCount,
            'Retweets':tweet.retweetCount,
            'Device':tweet.sourceLabel
            })
            print(f'Added a tweet ...{len(tweets)} done out of {limit}')
    return pd.DataFrame(tweets)

if __name__ == '__main__':
    tweets_data = tweet_getter('', 150000, '2022-01-01','2022-07-07',False)
    print(tweets_data.head(10))
    tweets_data.to_csv(r'C:/Users/user/Desktop/Project/Sentiment Analysis/Twitter-Sentiment-Analysis/.csv',index=False)