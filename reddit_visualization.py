import constants
import reddit_data as rd
import matplotlib.pyplot as plt
import numpy as np


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
