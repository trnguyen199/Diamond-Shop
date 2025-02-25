import os
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

PATH = "C:\Program File (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

def linkedin_func():
    try:
        linkedin_home_page = "http://127.0.0.1:8000/accounts/login/"
        driver.get(linkedin_home_page)
        driver.implicitly_wait(3)
    
        # get the username field
        username = driver.find_element(By.ID, 'session_key')
        # get the password field
        password = driver.find_element(By.ID, 'session_password')
        # get login/submit button
        login = driver.find_element(By.XPATH, '//form/input[2]')
    
        # send login
        username.send_keys('admin')
        password.send_keys('123')
        login.click()
    
    except Exception as e:
        print(e)

