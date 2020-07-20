import praw

reddit = praw.Reddit(client_id = 'N_9TUKaeGtQ_1A',
                     client_secret = 'CIi2mgP5ltesUVH9QzqY-OzVqt0',
                     username = 'ironbatshashank',
                     password = 'youtubething',
                     user_agent = 'rslash')

subreddit = reddit.subreddit('covid')

hot_python = subreddit.hot(limit=2)

for submission in hot_python:
    if not submission.stickied:
        print(submission.title)
