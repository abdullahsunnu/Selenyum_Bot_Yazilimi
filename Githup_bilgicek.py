from Githup_kullanıcı_bilgisi import username, password  # kullanıcı dosyasının yolunu belirttik
from selenium import webdriver
import time


class Github:  # Githup sınıfı oluşturduk
    def __init__(self, username, password):  # parametrelerini verdik
        self.browser = webdriver.Chrome()  # wep driveri chrome de acacağımızı soyledik
        self.username = username  # eşitledilk
        self.password = password
        self.followers = []  # followers i boş bir listeye atadık

    def signIn(self):  # login giriş sayfası

        # login sayfasının linkini get dedik
        self.browser.get("https://github.com/login")
        time.sleep(2)  # uyuttuk

        # username ve passwordun xpath ini aldım
        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        # giriş butonuna clıck için xpath aldık
        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]").click()


    def loadFollowers(self):
        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")

        for i in items:
            self.followers.append(i.find_element_by_css_selector(".Link--secondary").text)  # hepsini almak için for dongusune soktuk

    def getFollowers(self):  # self.username göre ayarla # işlem yapılacak sayfaının lınkı get
        self.browser.get("https://github.com/fdeniz07?tab=followers") # kullanıcı ismini yaz (MET-DEV) yerine

        time.sleep(2)

        self.loadFollowers()

        while True:
            links = self.browser.find_element_by_class_name("pagination").find_elements_by_tag_name("a")

            if len(links) == 1:
                if links[0].text == "Next":
                    links[0].click()
                    time.sleep(1)
                    self.loadFollowers()
                else:
                    break
            else:
                for link in links:
                    if link.text == "Next":
                        link.click()
                        time.sleep(1)

                        self.loadFollowers()
                    else:
                        continue

github = Github(username, password)
github.signIn()
github.getFollowers()
print(len(github.followers))
print(github.followers)


