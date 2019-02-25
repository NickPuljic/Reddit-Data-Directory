

def compare_subreddit_user_data(reddit_instance):
    print("Choose the subreddits you wish to compare!")
    subreddits_user_data = []
    subreddit_names = []
    while True:
        subreddit_name = input("Subreddit name (leave blank to continue):")
        if not subreddit_name:
            break
        subreddit_data = get_subreddit_data(reddit_instance, subreddit_name)
        subreddit_names.append(subreddit_name)
        subreddit_user_data = {key: subreddit_data[key] for key in ['accounts_active', 'subscribers']} # https://stackoverflow.com/questions/3420122/filter-dict-to-contain-only-certain-keys
        subreddits_user_data.append(subreddit_user_data)

    n = len(subreddits_user_data)
    if n < 2:
        print("You must choose at least two subreddits to compare.")
        return

    subscribers = list(map(lambda x: x['subscribers'], subreddits_user_data))
    accounts_active = list(map(lambda x: x['accounts_active'], subreddits_user_data))
    ind = np.arange(n)
    #width = .2 #check

    # https://matplotlib.org/gallery/lines_bars_and_markers/bar_stacked.html
    p1 = plt.bar(ind, subscribers)
    p2 = plt.bar(ind, accounts_active, bottom=subscribers)

    plt.ylabel('User Activity')
    plt.title('Subreddit User Data')
    plt.xticks(ind, subreddit_names)
    plt.legend((p1[0], p2[0]), ('Subscribers', 'Current Active Users'))

    plt.show()

def compare_submission_data(reddit_instance):
    print("Which subreddit do you want to compare?")
    subreddit_name = input("Subreddit name:")
    print("For what time period?")
    time_filter = input("Time period (all, day, hour, month, week, year):")
    print("How many submissions do you want to compare?")
    limit = input("How many? (1-100):")
    submission_data = get_submission_data(reddit_instance, subreddit_name=subreddit_name, time_filter=time_filter, limit=limit)

    score_data = list(map(lambda x: x['score'], submission_data))
    ind = np.arange(len(score_data))

    plt.plot(ind, score_data, 'o-')

    plt.ylabel("Score")
    plt.xlabel("Submission Number")
    plt.title(subreddit_name + " Submission Score data")
    plt.xticks(ind, ind)

    plt.show()
