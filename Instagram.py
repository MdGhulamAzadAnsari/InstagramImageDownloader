from selenium import webdriver
import urllib.request
import time
import random
import os
class Instagram:
    def __init__(self):
        self.bot = webdriver.Firefox()

    def download_image(self, url):
        name = random.randrange(1, 1000)
        full_name = str(name) + ".jpg"
        path = os.path.join('E:\\Instagram\\', full_name)
        urllib.request.urlretrieve(url, path)  

    def find_img(self, hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/iammdusmanansari')
        time.sleep(4)
        for _ in range(1,2):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            posts = bot.find_elements_by_tag_name('a')
            links = [elem.get_attribute('href') for elem in posts]
            links = [link for link in links if "https://www.instagram.com/p/" in link]
            
            for link in links:
                bot.get(link)
                try:
                    media = bot.find_element_by_xpath("//meta[@property='og:image']")
                    self.download_image(media.get_attribute('content'))
                except Exception as ex:
                    print(ex)
                    time.sleep(2)

ed = Instagram()
ed.find_img('mdusmanansari')
print("Images Successful Downloaded.")
