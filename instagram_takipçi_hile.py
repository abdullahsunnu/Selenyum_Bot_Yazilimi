import os
import time
from selenium import webdriver
from İnstagram_kullanıcı_bilgisi import username,password



with open("followers.txt","r",encoding='utf-8') as dosya:
    icerik = dosya.readlines()
    for satır in icerik:
        satır = satır.replace("https://www.instagram.com","")
        satır = satır.replace("/","\"")
        print(satır)