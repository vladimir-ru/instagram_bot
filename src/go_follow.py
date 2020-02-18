from selenium import webdriver
import variables
import time
import pyautogui

cou = 0
file = open('bots_log.txt', 'r')
now_bot_info = file.read().split('\n')
pas_login = now_bot_info[0].split(', ')

if __name__ == '__main__':
    print('##########################\n###NOW WORK ONLY FOLLOW###\n##########################')


while cou != int(len(now_bot_info)):
    pas_login = now_bot_info[cou].split(', ')
    browser = webdriver.Chrome('../chromedriver/chromedriver')
    # login and go follow
    browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(7)
    browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(
        pas_login[1])
    browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(
        pas_login[0])
    browser.find_element_by_xpath('//section/main/div/article/div/div[1]/div/form/div[4]/button').click()
    time.sleep(5)
    browser.get('https://www.instagram.com/var_poltos/')
    time.sleep(10)
    pyautogui.click(578, 315)
    cou += 1
    time.sleep(15)
    browser.close()

file.close()