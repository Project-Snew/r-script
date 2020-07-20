import praw

reddit = praw.Reddit(client_id = 'N_9TUKaeGtQ_1A',
                     client_secret = 'CIi2mgP5ltesUVH9QzqY-OzVqt0',
                     username = 'ironbatshashank',
                     password = 'youtubething',
                     user_agent = 'rslash')

subreddit = reddit.subreddit('tits')

hot_title = subreddit.hot(limit=3)

for submission in hot_title:
    if not submission.stickied:
        print(submission.title)

        submission.comments.replace_more(limit=0)

        for comment in submission.comments.list():
            print(20 * '--')
            print('Parent ID:', comment.parent())
            print('Comment ID:, comment.id')
            print(comment.body)


#Now we have to make program to just check the parent id and create a structure to make all
#comments and replies in proper structure. We'll just have all those in same line which 
#have the same parent id. That's easy.