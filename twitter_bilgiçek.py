from twitter_kullanıcı_bilgisi import username,password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe',chrome_options=self.browserProfile)  # wepdriver.chrome sayfayı chrome uzerinde acar
        self.username = username
        self.password = password



    def sıgnIn(self):
        self.browser.get("https://twitter.com/login") # bu linke get gider
        time.sleep(2)
        usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")


        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)


    def search(self, hashtag):
        searchInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input")
        searchInput.send_keys(hashtag)
        time.sleep(2)

        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        result = []

        list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]")# twitter deki paylaşımların başlığının kodu
        time.sleep(2)
        print("count: " + str(len(list)))

        for i in list:
            result.append(i.text)

        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter>20:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(5)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter+=1

            list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]")# twitter deki paylaşımların başlığının kodu
            time.sleep(5)
            print("count: " + str(len(list)))
            for i in list:
                result.append(i.text)

        list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]")# twitter deki paylaşımların başlığının kodu
        time.sleep(5)
        print("count: " + str(len(list)))

        count = 1
        for item in result:
            print(f"{count}-{item}")
            count+=1
            print("*" * 30)




twitter = Twitter(username,password)
twitter.sıgnIn()
twitter.search("python")