import selenium
import time
from random import randint
from selenium.webdriver.common.keys import Keys


def change_emoji(receiver):
    driver = selenium.webdriver.Chrome(executable_path=r"C:\chromedriver.exe")

    driver.get('https://www.messenger.com/t/' + receiver)
    assert "Messenger" in driver.title
    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")

    username.send_keys('email')
    password.send_keys('password')
    driver.find_element_by_name("login").click()

    time.sleep(6)

    driver.execute_script("document.querySelectorAll('._3szq')[2].click()")

    time.sleep(5)

    driver.find_elements_by_class_name(' _4rlu')[randint(0, 92)].click()

    assert "No results found." not in driver.page_source
    driver.close()


while True:
    change_emoji('facebook-username')
    time.sleep(86400)
