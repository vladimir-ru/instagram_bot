import random
import pyautogui
import time
from selenium import webdriver


def create_mail():
    browser = webdriver.Chrome('../chromedriver/chromedriver')

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
    time.sleep(0.5)
    for i in s_cor:
        pyautogui.click(i[0], i[1])
        pyautogui.typewrite(password)
        time.sleep(4)
    browser.find_element_by_xpath('//div/div/div/div[1]/div[3]/form/div[12]/div[1]/button').click()
    file_mail_log = open('mails_log', 'a')
    inp_mail = str(input('Please enter mail!... '))
    end_str = f'{inp_mail}, {password}\n'
    file_mail_log.write(end_str)
    file_mail_log   .close()


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


def rand_mail():
    lis_alp = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
               'e', 'd', 'c', 'b', 'a', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def rand_word(alp):
        word_num = alp[random.randint(0, int(len(alp) - 1))]
        return word_num

    end_word = 'vova'
    cou = 0
    full = int(random.randint(5, 9))
    while cou != full:
        if random.randint(0, 3) == 0:
            end_word += str(rand_word(lis_alp)).upper()
        else:
            end_word += str(rand_word(lis_alp))
        cou += 1
    end_word += '@kiq.kr'
    return end_word


def new_username():
    lis_alp = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
               'e', 'd', 'c', 'b', 'a', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def rand_word(alp):
        word_num = alp[random.randint(0, int(len(alp) - 1))]
        return word_num

    end_word = ''
    cou = 0
    full = int(random.randint(8, 12))
    while cou != full:
        if cou == 4:
            end_word += 'var_pol'

        elif random.randint(0, 4) == 0:
            end_word += str(rand_word(lis_alp)).upper()
        else:
            end_word += str(rand_word(lis_alp))
        cou += 1
    return end_word


need_mail = str(input('Do you want to create mail account? \n(y/n)'))
if need_mail == 'y':
    time.sleep(1)
    create_mail()
accounts = int(input('How many accounts do you want to create? '))
auto = str(input('Do you want to automatic create?\n(y/n) '))


counter = 0
while counter != accounts:
    browser = webdriver.Chrome('../chromedriver/chromedriver')
    time.sleep(5)
    mail = rand_mail()
    if auto == 'n':
        while True:
            full_name = str(input('Please enter full name... '))
            username = str(input('Please enter username... '))
            password = str(input('Please enter password... '))
            ok = str(input('Is that all right?\n(y/n) '))
            if ok == 'y':
                break
    if auto == 'y':
        full_name = new_full_name_or_password()
        username = new_username()
        password = new_full_name_or_password()

    browser.get('https://www.instagram.com/')
    time.sleep(5)
    browser.find_element_by_xpath('//section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(mail)
    browser.find_element_by_xpath('//section/main/article/div[2]/div[1]/div/form/div[4]/div/label/input').send_keys(full_name)
    browser.find_element_by_xpath('//section/main/article/div[2]/div[1]/div/form/div[5]/div/label/input').send_keys(username)
    browser.find_element_by_xpath('//section/main/article/div[2]/div[1]/div/form/div[6]/div/label/input').send_keys(password)
    counter += 1
    right_login = str(input('Do you want to save this username?\n(y/n)'))
    if right_login == 'n':
        username = str(input('Write right username... '))
    save_account = str(input('Do you want to save this account?\n(y/n) '))
    if save_account == 'y':
        file = open('bots_log.txt', 'a')
        load = f"{password}, {username}\n"
        file.write(load)
        file.close()
    else:
        print(f'Good, you created {counter} account!')
