from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def passport(self, lat=40.7128, lon=-74.0060):
        params = {
        "latitude": lat,
        "longitude": lon,
        "accuracy": 100}

        self.driver.execute_cdp_cmd("Page.setGeolocationOverride", params)

    def login(self):
        self.driver.maximize_window()

        self.driver.get('https://tinder.com')

        sleep(5)

        g_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
        g_btn.click()

        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email.send_keys(username)

        next1 = self.driver.find_element_by_xpath('//*[@id="identifierNext"]')
        next1.click()

        sleep(5)

        pwd = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        pwd.send_keys(password)

        next2 = self.driver.find_element_by_xpath('//*[@id="passwordNext"]')
        next2.click()

        self.driver.switch_to.window(base_window)

        self.passport()

        sleep(10)

        cookies_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        cookies_btn.click()

        sleep(2)

        location_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        location_btn.click()

        sleep(3)

        notification_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        notification_btn.click()

    def right(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def left(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def close_popup(self):
        popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                try:
                    self.right()
                except Exception:
                    try:
                        self.close_popup()
                    except Exception:
                        self.close_match()
            except Exception:
                break

bot = TinderBot()

logged_in = False
while not logged_in:
    logged_in = True
    try:
        bot.login()
    except:
        bot.driver.quit()
        bot = TinderBot()
        logged_in = False

sleep(3)

bot.passport()

bot.auto_swipe()
