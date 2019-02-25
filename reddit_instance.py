import praw


class RedditInstance():
    def __init__(self):
        self.client_id = 'vCRhC8KZ5GqbTA'
        self.client_secret = 'Lv6fHtG_W1K6Vf6ap2SspYBTo5k'
        self.user_agent = 'PC:Python Scraper:v 1.0.0 (by /u/reallynotrealreally)'
        self.Reddit = praw.Reddit(client_id=self.client_id, client_secret=self.client_secret, user_agent=self.user_agent)

    def get_instance(self):
        return self.Reddit
