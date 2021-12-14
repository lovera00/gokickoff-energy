from selenium import webdriver
from time import sleep
user = input("Enter your username: ")
password = input("Enter your password: ")
browser = webdriver.Chrome('c:/pruebas/chromedriver.exe') # Change the path to your chromedriver
sleep(5)
browser.get('https://gokickoff.com/activity_player_detail.php?type=4&option=2&player_id=10665525') # Change the URL to your desired player
sleep(5)
try:
    userInput = browser.find_element_by_name('user_login')
    userInput.send_keys(user)
    passInput = browser.find_element_by_name('pwd_login')
    passInput.send_keys(password)
    buttonInput = browser.find_element_by_xpath('/html/body/center/div[2]/div/div/div[5]/div[1]/div[2]/div/div/form/div[1]/span/span/input')
    buttonInput.click()
    sleep(5)
except TypeError as e:
    print(e)
    browser.quit()
browser.quit()
