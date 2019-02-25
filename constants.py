from nltk.corpus import stopwords


valid_time_filters = ['all', 'day', 'hour', 'month', 'week', 'year']
valid_listings = ['controversial', 'gilded', 'hot', 'new', 'top']

subreddit_keys = ['accounts_active','created_utc', 'display_name', 'public_description', 'subscribers']
submission_keys = ['author', 'created_utc', 'edited', 'gildings', 'num_comments', 'num_crossposts', 'score', 'stickied', 'title']
comment_keys = ['author', 'body', 'created_utc', 'edited', 'score']

subreddit_user_keys = ['accounts_active', 'subscribers']

stopwords = stopwords.words('english')
