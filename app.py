import tweepy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    new_speak = [
        'bb',
        'bellyfeel',
        'blackwhite',
        'crimestop',
        'crimethink',
        'dayorder',
        'dep',
        'doubleplusgood',
        'doubleplusungood',
        'doublethink',
        'duckspeak',
        'facecrime',
        'Ficdep',
        'free',
        'fullwise',
        'goodthink',
        'goodsex',
        'goodwise',
        'Ingsoc',
        'joycamp',
        'malquoted',
        'Miniluv',
        'Minipax',
        'Minitrue',
        'Miniplenty',
        'Oldspeak',
        'oldthink',
        'ownlife',
        'plusgood',
        'plusungood',
        'Pornosec',
        'prolefeed',
        'Recdep',
        'rectify',
        'ref',
        'sec',
        'sexcrime',
        'speakwrite',
        'Teledep',
        'telescreen',
        'thinkpol',
        'unperson',
        'upsub']  # list of newspeak words

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/?lang=en')
        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.email)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def censor(self):
        bot = self.bot
        tweets = bot.find_element_by_class_name(
            "css-1dbjc4n").text
        # if tweets not in TwitterBot.new_speak:
        #     tweets.replace(tweets)

    def check(self, user):
        # leave this for now
        check = True
        consumer_key = "8LfgceWJmQWwmjVMLEZCp4fvn"
        consumer_secret = "wNbCmgCbpboKBwLjbdiZr7Ugyw9bhLNVz5hYUUJU7nRVEfl5Y9"
        access_token = "872684552-W1M5j1gPwLNf7ZPYFwYu49HjjkohsZBttINuzhmE"
        access_token_secret = "i7hVgq7furWacz4VF9UF4VsFPap5FnoxmAtXvKBWcFs2h"

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True,
                         wait_on_rate_limit_notify=True)

        tweets = api.user_timeline(
            screen_name=user, count=200, include_rts=False, tweet_mode='extended')

        for info in tweets[:3]:
            if(info not in self.new_speak):
                print("new speak violation: ", info.full_text)
                check = False
        return check


team = TwitterBot('ScraperBot5', 'Arshdeep16')
team.login()
team.censor()
# checks if following new speak
check = team.check("ScraperBot5")
print(check)
