# PYTHON GANG
# INSTABOT
# MAIN CODE
# AUTHOR IS VLADIMIR EGOROV
# instagram - @var_poltos

from selenium.common.exceptions import NoSuchElementException
import random
import pyautogui
import time
from selenium import webdriver

if __name__ == '__main__':
    print('===================\n####PYTHON GANG####\n##instabot   v0.1##\n===================')


def create_account():  # create new instagram account or email account
    global full_name, username, password

    def xpath_exception(url):
        try:
            browser.find_element_by_xpath(url)
            existence = 1
        except NoSuchElementException:
            existence = 0
        return existence

    def create_mail():
        browser = webdriver.Chrome('../chromedriver/chromedriver')

        first_name = new_full_name_or_password()
        last_name = new_full_name_or_password()
        account_name = new_full_name_or_password()
        password = new_full_name_or_password()

        browser.get('https://account.mail.ru/signup?from=main&rf=auth.mail.ru')
        browser.find_element_by_xpath(
            '//div/div/div/div[1]/div[3]/form/div[3]/div/div/div[1]/div/div[2]/div[1]/input').send_keys(first_name)
        browser.find_element_by_xpath(
            '//div/div/div/div[1]/div[3]/form/div[3]/div/div/div[2]/div/div[2]/div[1]/input').send_keys(last_name)
        cor = [[369, 436], [371, 479], [463, 442], [468, 484], [670, 436], [671, 680], [348, 509]]
        for i in cor:
            time.sleep(0.6)
            pyautogui.click(i[0], i[1])
        browser.find_element_by_xpath(
            '//div/div/div/div[1]/div[3]/form/div[6]/div/div[2]/div[1]/div/div[1]/span[3]/input').send_keys(
            account_name)
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
        file_mail_log.close()

    def new_full_name_or_password():
        lis_alp = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g',
                   'f',
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
        lis_alp = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g',
                   'f',
                   'e', 'd', 'c', 'b', 'a', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        def rand_word(alp):
            word_num = alp[random.randint(0, int(len(alp) - 1))]
            return word_num

        end_word = 'pythongang'
        cou = 0
        full = int(random.randint(5, 9))
        while cou != full:
            if random.randint(0, 3) == 0:
                end_word += str(rand_word(lis_alp)).upper()
            else:
                end_word += str(rand_word(lis_alp))
            cou += 1
        end_word += '@kiq.ru'
        return end_word

    def new_username():
        lis_alp = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g',
                   'f',
                   'e', 'd', 'c', 'b', 'a', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        def rand_word(alp):
            word_num = alp[random.randint(0, int(len(alp) - 1))]
            return word_num

        end_word = 'pythongang'
        cou = 0
        full = int(random.randint(4, 7))
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
        browser.find_element_by_xpath('//section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(
            mail)
        browser.find_element_by_xpath('//section/main/article/div[2]/div[1]/div/form/div[4]/div/label/input').send_keys(
            full_name)
        browser.find_element_by_xpath('//section/main/article/div[2]/div[1]/div/form/div[5]/div/label/input').send_keys(
            username)
        browser.find_element_by_xpath('//section/main/article/div[2]/div[1]/div/form/div[6]/div/label/input').send_keys(
            password)
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
        browser.quit()


def main_bot():  # main bot's code
    ##############
    def xpath_exception(url):
        try:
            browser.find_element_by_xpath(url)
            existence = 1
        except NoSuchElementException:
            existence = 0
        return existence

    def go_follow(link):
        browser.get(link)
        time.sleep(0.5)
        pyautogui.click(607, 315)

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
            rand = random.randint(0, int(len(lis) - 1))
            resp = lis[int(rand)]
            browser.find_element_by_xpath(
                '//section/main/div/div/article/div[2]/section[3]/div/form/textarea').send_keys(
                resp)
            file.close()
            time.sleep(0.3)
            browser.find_element_by_xpath('//section/main/div/div/article/div[2]/section[3]/div/form/button').click()
            f_cou += 1
            time.sleep(1)
            browser.get(link)

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

    while cou != (bots - 1):
        pas_login = now_bot_info[cou].split(', ')
        browser = webdriver.Chrome('../chromedriver/chromedriver')
        # login and go follow
        browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(2)
        browser.find_element_by_xpath(
            '//section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(
            pas_login[1])
        browser.find_element_by_xpath(
            '//section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(
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


#######################
#   input questions   #
#######################
main_quest = int(input("1 - Create instagram account.\n2 - Main bot's code.\n"))
if main_quest == 1:
    create_account()
elif main_quest == 2:
    main_bot()