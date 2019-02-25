import constants
from datetime import datetime


def format_comment(comment):
    """Formats a comment's info in a human-readable way"""
    comment_dict = {key: vars(comment)[key] for key in constants.comment_keys} # https://stackoverflow.com/questions/3420122/filter-dict-to-contain-only-certain-keys
    comment_dict['created_utc'] = datetime.utcfromtimestamp(comment_dict['created_utc']).strftime('%Y-%m-%d %H:%M:%S')
    if 'author' in comment_dict and comment_dict['author']:
        comment_dict['author'] = comment_dict['author'].name
    if 'edited' in comment_dict and comment_dict['edited']:
        comment_dict['edited'] = datetime.utcfromtimestamp(comment_dict['edited']).strftime('%Y-%m-%d %H:%M:%S')
    return comment_dict


def format_submission(submission):
    """Formats a submission's info in a human-readable way"""
    submission_dict = {key: vars(submission)[key] for key in constants.submission_keys} # https://stackoverflow.com/questions/3420122/filter-dict-to-contain-only-certain-keys
    submission_dict['created_utc'] = datetime.utcfromtimestamp(submission_dict['created_utc']).strftime('%Y-%m-%d %H:%M:%S')
    if 'author' in submission_dict and submission_dict['author']:
        submission_dict['author'] = submission_dict['author'].name
    if 'edited' in submission_dict and submission_dict['edited']:
        submission_dict['edited'] = datetime.utcfromtimestamp(submission_dict['edited']).strftime('%Y-%m-%d %H:%M:%S')
    return submission_dict


def validate_limit(limit):
    """Validates the limit integer, returns a usable integer"""
    try:
        limit = int(limit)
    except:
        raise TypeError("Limit should be an integer.")

    if limit > 100:
        print("Warning: only able to get 100 submissions at once. 'Limit' has been set to 100.")
        limit = 100
    elif limit < 1:
        print("Warning: should get at least one submission. 'Limit' has been set to 1.")

    return limit


def validate_subreddit_info(reddit_instance, subreddit_name, listing, time_filter):
    """Validate the given data and subreddit information, returns a subreddit object"""
    if time_filter not in constants.valid_time_filters:
        raise ValueError("Not a valid time filter, valid filters are: " + str(valid_time_filters))
    if listing not in constants.valid_listings:
        raise ValueError("Not a valid listing, valid listings are: " + str(valid_listings))

    reddit = reddit_instance.get_instance()

    try:
        subreddit = reddit.subreddit(subreddit_name)
        # This is done to evalute the lazy object that is 'subreddit' at this point to verify it is a real subreddit
        if subreddit_name != 'all':
            description = subreddit.description
    except:
        raise ValueError("That subreddit does not exist.")

    return subreddit
