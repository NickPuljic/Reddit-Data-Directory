import constants
import reddit_data as rd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def get_most_common_comment_words(reddit_instance, subreddit_name, listing, time_filter, limit, word_amount):
    """Returns the most common words in the top comments from the queried submissions"""
    try:
        word_amount = int(word_amount)
    except:
        raise TypeError("The amount of unique words should be an integer.")
    comment_data = rd.get_comment_data(reddit_instance, subreddit_name, listing, time_filter, limit)

    comment_words = Counter()

    for data in comment_data:
        comment_words.update(data['body'].split())

    comment_words = Counter({key: comment_words[key] for key in comment_words if key not in constants.stopwords})
    return comment_words.most_common(word_amount)


def compare_subreddit_user_data(reddit_instance, subreddit_names):
    """Graphs user data for the given subreddits"""
    subreddit_user_data = []
    for subreddit_name in subreddit_names:
        subreddit_data = rd.get_subreddit_data(reddit_instance, subreddit_name)
        user_data = {key: subreddit_data[key] for key in constants.subreddit_user_keys} # https://stackoverflow.com/questions/3420122/filter-dict-to-contain-only-certain-keys
        subreddit_user_data.append(user_data)

    n = len(subreddit_user_data)
    if n < 2:
        print("You must choose at least two subreddits to compare.")
        return

    subscribers = list(map(lambda x: x['subscribers'], subreddit_user_data))
    accounts_active = list(map(lambda x: x['accounts_active'], subreddit_user_data))
    ind = np.arange(n)

    # https://matplotlib.org/gallery/lines_bars_and_markers/bar_stacked.html
    p1 = plt.bar(ind, subscribers)
    p2 = plt.bar(ind, accounts_active, bottom=subscribers)

    plt.ylabel('User Activity')
    plt.title('Subreddit User Data')
    plt.xticks(ind, subreddit_names)
    plt.legend((p1[0], p2[0]), ('Subscribers', 'Current Active Users'))

    plt.show()


def compare_submission_data(reddit_instance, subreddit_name, listing, time_filter, limit):
    """Graphs the scores of the queried posts on the given subreddit"""
    submission_data = rd.get_submission_data(reddit_instance, subreddit_name, listing, time_filter, limit)

    score_data = list(map(lambda x: x['score'], submission_data))
    ind = np.arange(1, 1 + len(score_data))

    plt.plot(ind, score_data, 'o-')

    plt.ylabel("Score")
    plt.xlabel("Submission Number")
    plt.title(subreddit_name + " Submission Score Data")
    plt.xticks(ind, ind)

    plt.show()
