from İnstagram_kullanıcı_bilgisi import username,password # kullanıcı bilgimin olduğu sayfa
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys  # enter e basmak için bu modulu import ettik


class Instagram:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe',chrome_options=self.browserProfile)  # wepdriver.chrome sayfayı chrome uzerinde acar
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/") # instagram login linki
        time.sleep(5)
        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input") # ısım yerinin xpath i
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input") # sifre yerinin xpath i

        usernameInput.send_keys(self.username) # isim ve parola bilgilerini gönderiyor
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)   # enter işlemi yapıyor
        time.sleep(7)


    def getFollowers(self, max):
        self.browser.get(f"https://www.instagram.com/"+username)   # {self.username} OLACAK
        time.sleep(2)

        # Instagram.scroolBar(self)

        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(4)
        #sayac = 0
        # followers = self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa") # aldığımız kışının isminin css i

        # YENİ EKLEnDİ

        dialog = self.browser.find_element_by_xpath("/html/body/div[5]/div")  # div[role=dialog] ul
        followerCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"first count: {followerCount}")

        action = webdriver.ActionChains(self.browser)  # action uzeriinden istediğimiz tuşları göderebilecez.

        while followerCount < max:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()  #.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))
            if followerCount != newCount:
                followerCount = newCount
                print(f"second count: {newCount}")
                time.sleep(1)
            else:
                break

        followers = dialog.find_elements_by_css_selector("li") #li

        followerList = []
        i = 0
        for user in followers:

            link = user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)
            i += 1
            if i == max:
                break

        with open("followers.txt", "w", encoding="UTF-8") as file:
            for item in followerList:
                file.write(item+ ",") # + "\n" # ********** dosyayı yazılan bilgileri duz yazdırır yorumda alt satıra atar.*************



    # sayac = 0
    # def followUser(self, username):
    #     sayac+=1
    #     self.browser.get(f"{sayac} https://www.instagram.com/"+username)  #
    #     time.sleep(6)






        # time.sleep(4)
        # for user in followers:
        #     sayac += 1
        #     print(str(sayac)+ "--> "+f"https://www.instagram.com/{user.text}/") # aldığımız kışıleri f str ile url cevirdim
        #     time.sleep(2)

    # def scroolBar(self):
    #     jsKomut = """
    #     sayfa = document.querySelector(".isgrP");
    #     sayfa.scrollTo(0,sayfa.scrollHeight);
    #     var sayfaSonu = sayfa.scrollHeight;
    #     return sayfaSonu;
    #     """
    #     sayfaSonu = self.browser.execute_script(jsKomut)
    #
    #     while True:
    #         son = sayfaSonu
    #         time.sleep(7)
    #         sayfaSonu = self.browser.execute_script(jsKomut)
    #
    #         if son == sayfaSonu:
    #             break

    def followUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)


        followButon = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div/button")
        #followButon = self.browser.find_element_by_tag_name("button")
        if followButon.text != "Message" and followButon.text != "Requested":
            followButon.click()
            time.sleep(2)



        # elif followButon.text == "Follow":
        #     followButon.click()
        #     time.sleep(2)


        else:
            print("Zaten takiptesin")



    def unFollowUser(self, username):
        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(2)

        followButton = self.browser.find_elements_by_tag_name('button')[1]
        if followButton.text != "Follow":
            followButton.click()
            time.sleep(2)
            self.browser.find_element_by_xpath('//button[text()="Unfollow"]').click()
        else:
            print("zaten takip etmiyorsun")




instagram = Instagram(username, password) # giriş yaparken bilgi girme
instagram.signIn()  # giriş yap

#instagram.getFollowers(50) # takipçileri çeker


listee =[] # toplu takip etme işlemi for döngüsü
for user in listee:
    if user == "": # takp edilecek ismin kullanıcı bilgisi
        continue
    instagram.followUser(user)
    time.sleep(3)

#instagram.followUser(user) # tek tek atkip etme işlemi



#instagram.unFollowUser(self.username) # takibi birakma

