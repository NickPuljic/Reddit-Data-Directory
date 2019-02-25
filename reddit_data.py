import constants
import helpers
from datetime import datetime


def get_subreddit_data(reddit_instance, subreddit_name):
    """Query and return basic data for a given subreddit"""
    reddit = reddit_instance.get_instance()

    if subreddit_name == 'all':
        raise ValueError("Cannot retrieve data from all.")

    try:
        subreddit = reddit.subreddit(subreddit_name)

        # This is to evaluate the lazy expression to make sure it is a valid subreddit
        description = subreddit.description
    except:
        raise ValueError("That subreddit does not exist.")

    subreddit_dict = {key: vars(subreddit)[key] for key in constants.subreddit_keys} # https://stackoverflow.com/questions/3420122/filter-dict-to-contain-only-certain-keys
    if 'created_utc' in subreddit_dict:
        subreddit_dict['created_utc'] = datetime.utcfromtimestamp(subreddit_dict['created_utc']).strftime('%Y-%m-%d %H:%M:%S')
    return subreddit_dict


def get_submission_data(reddit_instance, subreddit_name='all', listing="hot", time_filter='all', limit=100):
    """Query and return the information for the most relavant posts in a given
    subreddit within the query parameters"""
    limit = helpers.validate_limit(limit)
    subreddit = helpers.validate_subreddit_info(reddit_instance, subreddit_name, listing, time_filter)

    submission_data = []

    if listing == 'hot':
        for submission in subreddit.hot(limit=limit):
            submission_data.append(helpers.format_submission(submission))
    elif listing == 'top':
        for submission in subreddit.top(limit=limit, time_filter=time_filter):
            submission_data.append(helpers.format_submission(submission))
    elif listing == 'controversial':
        for submission in subreddit.controversial(limit=limit, time_filter=time_filter):
            submission_data.append(helpers.format_submission(submission))
    elif listing == 'new':
        for submission in subreddit.new(limit=limit, time_filter=time_filter):
            submission_data.append(helpers.format_submission(submission))
    elif listing == 'gilded':
        for submission in subreddit.gilded(limit=limit, time_filter=time_filter):
            submission_data.append(helpers.format_submission(submission))
    return submission_data


def get_comment_data(reddit_instance, subreddit_name='all', listing="hot", time_filter='all', limit=100):
    """Query and return the comment data from the top comments on the queried submissions"""
    limit = helpers.validate_limit(limit)
    subreddit = helpers.validate_subreddit_info(reddit_instance, subreddit_name, listing, time_filter)

    comment_data = []

    if listing == 'hot':
        for submission in subreddit.hot(limit=limit):
            submission.comments.replace_more(limit=0) # replace MoreComments object from submission comments so we see all comments
            for comment in submission.comments.list():
                comment_data.append(helpers.format_comment(comment))
    elif listing == 'top':
        for submission in subreddit.top(limit=limit, time_filter=time_filter):
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                comment_data.append(helpers.format_comment(comment))
    elif listing == 'controversial':
        for submission in subreddit.controversial(limit=limit, time_filter=time_filter):
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                comment_data.append(helpers.format_comment(comment))
    elif listing == 'new':
        for submission in subreddit.new(limit=limit, time_filter=time_filter):
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                comment_data.append(helpers.format_comment(comment))
    elif listing == 'gilded':
        for submission in subreddit.gilded(limit=limit, time_filter=time_filter):
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                comment_data.append(helpers.format_comment(comment))
    return comment_data
