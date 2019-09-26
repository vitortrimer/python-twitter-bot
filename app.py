from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' +
                hashtag + '&src=typeahead_click')
        time.sleep(4)
        for i in range(1, 4):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('href')
                     for elem in bot.find_elements_by_xpath("//a[@dir='auto']")]
            filteredLinks = list(filter(lambda x: 'status' in x, links))

        for link in filteredLinks:
            bot.get(link)
            try:
                bot.find_element_by_class_name(
                    "r-lrvibr").click()
                time.sleep(3)
            except Exception as ex:
                print(ex)


bot = TwitterBot('pythonmailer.vitor@gmail.com', 'vitorpythonbot')
bot.login()
bot.like_tweet('python')
