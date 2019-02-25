import pandas as pd
import reddit_analysis as ra
import reddit_data as rd
import reddit_instance as ri


def query_subreddit(reddit_instance):
    print("Which subreddit would you like to query?")
    subreddit_name = input("Subreddit name: ")
    print("")
    print(pd.Series(rd.get_subreddit_data(reddit_instance, subreddit_name)))


def query_subreddit_submission_data(reddit_instance):
    print("Which subreddit would you like to lookup submission data for?")
    subreddit_name = input("Subreddit name: ")
    print("Which listing would you like to see submissions for?")
    listing = input('Listing (options: hot, top, new, gilded, controversial): ')
    print("Which time filter would you like to see submissions for?")
    time_filter = input("Time filter (options: all, year, month, week, day, hour): ")
    print("How many submissions do you want data for?")
    limit = input("Submission amount (0-100): ")
    print(pd.DataFrame(rd.get_submission_data(reddit_instance, subreddit_name, listing, time_filter, limit)))


def query_subreddit_comment_data(reddit_instance):
    print("Which subreddit do you want to query the submission score data for?")
    subreddit_name = input("Subreddit name: ")
    print("Which listing would you like to see submissions from?")
    listing = input('Listing (options: hot, top, new, gilded, controversial): ')
    print("Which time filter would you like to see submissions from?")
    time_filter = input("Time filter (options: all, year, month, week, day, hour): ")
    print("How many submissions do you want data for?")
    limit = input("Submission amount (0-100): ")
    print("")
    print(pd.DataFrame(rd.get_comment_data(reddit_instance, subreddit_name, listing, time_filter, limit)))

def query_subreddit_most_common(reddit_instance):
    print("Which subreddit do you want query comments for?")
    subreddit_name = input("Subreddit name: ")
    print("Which listing would you like to see submissions for?")
    listing = input('Listing (options: hot, top, new, gilded, controversial): ')
    print("Which time filter would you like to see submissions for?")
    time_filter = input("Time filter (options: all, year, month, week, day, hour): ")
    print("How many submissions do you want data for?")
    limit = input("Submission amount (0-100): ")
    print("How many words would you like to see?")
    word_amount = input("How many words (integer): ")
    print(pd.DataFrame(ra.get_most_common_comment_words(reddit_instance, subreddit_name, listing, time_filter, limit, word_amount)))


def visualize_subreddit_user_data(reddit_instance):
    print("Choose the subreddits you wish to compare!")
    subreddit_names = []
    while True:
        subreddit_name = input("Subreddit name (leave blank to continue): ")
        if not subreddit_name:
            break
        subreddit_names.append(subreddit_name)
    ra.compare_subreddit_user_data(reddit_instance, subreddit_names)


def visualize_subreddit_submission_score_data(reddit_instance):
    print("Which subreddit do you want to view the submission score data for?")
    subreddit_name = input("Subreddit name: ")
    print("Which listing would you like to see submissions for?")
    listing = input('Listing (options: hot, top, new, gilded, controversial): ')
    print("Which time filter would you like to see submissions for?")
    time_filter = input("Time filter (options: all, year, month, week, day, hour): ")
    print("How many submissions do you want to see data for?")
    limit = input("Submission amount (0-100): ")
    ra.compare_submission_data(reddit_instance, subreddit_name, listing, time_filter, limit)


def display_interface(reddit_instance):
    while True:
        print("")
        print("Please choose a command by it's number:")
        print("1: Query Subreddit Basic Information")
        print("2: Query Subreddit Submissions Data")
        print("3: Query Subreddit Comment Data")
        print("4: Query subreddit Most Common Comment Words")
        print("5: Visualize Subreddit User Data")
        print("6: Visualize Subreddit Submission Score Data")
        print("9: Exit")
        command = input("Command: ")
        if command == '1':
            query_subreddit(reddit_instance)
        elif command == '2':
            query_subreddit_submission_data(reddit_instance)
        elif command == '3':
            query_subreddit_comment_data(reddit_instance)
        elif command == '4':
            query_subreddit_most_common(reddit_instance)
        elif command == '5':
            visualize_subreddit_user_data(reddit_instance)
        elif command == '6':
            visualize_subreddit_submission_score_data(reddit_instance)
        elif command == '9':
            break
        else:
            print("Invalid command")


if __name__ == '__main__':
    reddit_instance = ri.RedditInstance()
    print("Welcome to the Reddit Data Directory!")
    try:
        display_interface(reddit_instance)
    except Exception as e:
        print("")
        print("The following error has occurred:")
        print(e)
        print("Please try again.")
        print("")
