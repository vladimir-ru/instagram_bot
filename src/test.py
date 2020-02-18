import random
import pyautogui
import time
from selenium import webdriver

#browser = webdriver.Chrome('../chromedriver/chromedriver')

# browser.get('https://temp-mail.org/')
# time.sleep(5)
# browser.find_element_by_xpath("//*[@id='click-to-delete']")
# browser.find_element_by_xpath("//'mail']")

def new_full_name_or_password():
    lis_alp = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
               'e', 'd', 'c', 'b', 'a', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def rand_word(alp):
        word_num = alp[random.randint(0, int(len(alp) - 1))]
        return word_num

    end_word = ''
    cou = 0
    full = int(random.randint(8, 12))
    while cou != full:
        if random.randint(0, 4) == 0:
            end_word += str(rand_word(lis_alp)).upper()
        else:
            end_word += str(rand_word(lis_alp))
        cou += 1
    return end_word

# lis_alp = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
#           'e', 'd', 'c', 'b', 'a']
# print(lis_alp)
#

"""lis_alp = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
           'e', 'd', 'c', 'b', 'a', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def rand_word(alp):
    word_num = alp[random.randint(0, int(len(alp)-1))]
    return word_num


username = ''
cou = 0
full = int(random.randint(5, 10))
while cou != full:
    username += str(rand_word(lis_alp))
    print(username)
    cou += 1
print(username)"""


# username = random.randint(1, len(alp))

'''file = open('bots_log.txt', 'a')
file.write("'password', 'login'\n")
file.close()

file = open('bots_log.txt', 'r')
now_bot_info = file.read().split('\n')
print(now_bot_info[0])
file.close()'''


file = open('bots_log.txt', 'r')
now_bot_info = file.read().split('\n')
pas_login = now_bot_info[0].split(', ')
print(f'Password = {pas_login[0]}\nUsername = {pas_login[1]}')
file.close()



'''def create_mail():
    first_name = new_full_name_or_password()
    last_name = new_full_name_or_password()
    account_name = new_full_name_or_password()
    password = new_full_name_or_password()

    browser.get('https://account.mail.ru/signup?from=main&rf=auth.mail.ru')
    browser.find_element_by_xpath('//div/div/div/div[1]/div[3]/form/div[3]/div/div/div[1]/div/div[2]/div[1]/input').send_keys(first_name)
    browser.find_element_by_xpath('//div/div/div/div[1]/div[3]/form/div[3]/div/div/div[2]/div/div[2]/div[1]/input').send_keys(last_name)
    cor = [[369, 436], [371, 479], [463, 442], [468, 484], [670, 436], [671, 680], [348, 509]]
    for i in cor:
        time.sleep(0.6)
        pyautogui.click(i[0], i[1])
    browser.find_element_by_xpath('//div/div/div/div[1]/div[3]/form/div[6]/div/div[2]/div[1]/div/div[1]/span[3]/input').send_keys(account_name)
    s_cor = [[514, 646], [501, 719]]
    time.sleep(2)
    for i in s_cor:
        pyautogui.click(i[0], i[1])
        pyautogui.typewrite(password)
        time.sleep(4)
    browser.find_element_by_xpath('//div/div/div/div[1]/div[3]/form/div[12]/div[1]/button').click()


time.sleep(4)
create_mail()
# 369 436
# 371 479
# 463 442
# 468 484
# 670 436
# 671 680
# 348 509
# 514 646
# 501 719'''


def check():
    cou = 0
    while cou != 2:
        time.sleep(5)
        x, y = pyautogui.position()
        print(x, y)
        cou += 1

check()