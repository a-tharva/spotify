import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from utils import *


driver = webdriver.Chrome(r"C:\Program Files (x86)\chromedriver.exe") # Driver location
driver.get('http://open.spotify.com')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

mute_status = False

def login():
    login_btn = driver.find_element_by_xpath("//button[text()='Log in']")
    login_btn.click()
    wait.until(EC.visibility_of_element_located((By.ID, 'login-username')))
    type_text(getusername())
    tab()
    type_text(getPassword())
    times(tab, 2)
    enter()
    
    
def times(fn, times):
    for _ in range(0, times):
        fn()
    
def type_text(text):
    action = ActionChains(driver)
    action.send_keys(text)
    action.perform()
    
def press_key(key):
    type_text(key)
    
def tab():
    press_key(Keys.TAB)
    
def enter():
    press_key(Keys.ENTER)
    
def mute():
    mute_btn = driver.find_element_by_xpath("//button[contains(@class, 'volume-bar__icon)]")
    mute_btn.click()
    
def unmute():
    mute()
    
def now_playing_ad():
    now_playing_el = driver.find_elements_by_class_name('now-playing')
    return 'advert' in ''.join(el.text for el in now_playing_el).lower()


login()

while True:
    if now_playing_ad() == True and mute_status == False:
        mute()
        mute_status = True
    elif now_playing_ad() == False and mute_status == True:
        unmute()
        mute_status = False
    else:
        pass