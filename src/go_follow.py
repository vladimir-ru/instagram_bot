from selenium import webdriver
import variables
import time
import pyautogui


##############
def go_follow(link):
    browser.get(link)
    time.sleep(0.5)
    pyautogui.click(578, 315)
##############


file = open('bots_log.txt', 'r')
now_bot_info = file.read().split('\n')
pas_login = now_bot_info[0].split(', ')
print(f"Now we are having {len(now_bot_info)} bots.")
while True:
    bots = int(input('How many bots do you need?\n'))
    if bots <= int(len(now_bot_info)):
        break
need = int(input('1 - New followers.\n'))
input_link = str(input('Your link.\n'))
cou = 0

if __name__ == '__main__':
    print('##########################\n###NOW WORK ONLY FOLLOW###\n##########################')


while cou != int(len(now_bot_info)):
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
    cou += 1
    browser.close()

file.close()