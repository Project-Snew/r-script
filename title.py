import praw

reddit = praw.Reddit(client_id = 'N_9TUKaeGtQ_1A',
                     client_secret = 'CIi2mgP5ltesUVH9QzqY-OzVqt0',
                     username = 'ironbatshashank',
                     password = 'youtubething',
                     user_agent = 'rslash')

subreddit = reddit.subreddit('tits')

hot_title = subreddit.hot(limit=2)

for submission in hot_title:
    if not submission.stickied:
        print(submission.title)

        comments = submission.comments.list()
        for comment in comments:
            print(20 * '--')
            print(comment.body)
