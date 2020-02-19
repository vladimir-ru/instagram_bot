from selenium import webdriver
import variables
import time
import pyautogui
from selenium.common.exceptions import NoSuchElementException
import random


##############
def xpath_exception(url):
    try:
        browser.find_element_by_xpath(url)
        existence = 1
    except NoSuchElementException:
        existence = 0


def go_follow(link):
    browser.get(link)
    time.sleep(0.5)
    pyautogui.click(578, 315)


def page(link):
    browser.get(link)
    element = "//a[contains(@href, '/p/')]"
    if xpath_exception(element) == 0:
        print('Error')
        return
    time.sleep(0.5)
    posts = int(input('How many posts do you want to do. (the list starts with the last post)\n'))
    f_cou = 0
    while f_cou != posts:
        list_of_status = browser.find_elements_by_xpath(element)
        status = list_of_status[f_cou].get_attribute('href')
        browser.get(status)
        time.sleep(0.5)
        browser.find_element_by_xpath('//section/main/div/div/article/div[2]/section[1]/span[1]/button').click()
        browser.find_element_by_xpath('//section/main/div/div/article/div[2]/section[3]/div/form/textarea').click()
        time.sleep(0.1)
        file = open('resp.txt', 'r')
        lis = file.read().split('\n')
        rand = random.randint(0, int(len(lis)-1))
        resp = lis[int(rand)]
        browser.find_element_by_xpath('//section/main/div/div/article/div[2]/section[3]/div/form/textarea').send_keys(
            resp)
        file.close()
        time.sleep(0.3)
        browser.find_element_by_xpath('//section/main/div/div/article/div[2]/section[3]/div/form/button').click()
        f_cou += 1
##############


file = open('bots_log.txt', 'r')
now_bot_info = file.read().split('\n')
print(f"Now we are having {len(now_bot_info)} bots.")
while True:
    bots = int(input('How many bots do you need?\n'))
    if bots <= int(len(now_bot_info)):
        break
need = int(input('1 - New followers.\n2 - Like and comment new post.\n'))
input_link = str(input('Your link.\n'))
cou = 0

while cou != bots:
    pas_login = now_bot_info[cou].split(', ')
    browser = webdriver.Chrome('../chromedriver/chromedriver')
    # login and go follow
    browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(2)
    browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(
        pas_login[1])
    browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(
        pas_login[0])
    browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div[4]/button').click()
    time.sleep(2)
    if need == 1:
        go_follow(input_link)
    elif need == 2:
        page(input_link)
    cou += 1
    time.sleep(2)
    browser.quit()

file.close()