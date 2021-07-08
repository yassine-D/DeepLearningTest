from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('/Users/yassinederbali/Downloads/chromedriver')


def instagram_connector(driver):
    #open the webpage
    driver.get("http://www.instagram.com")

    #handle alerts pop ups
    not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accepter tout")]'))).click()

    # target username and password
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    #enter username and password
    username.clear()
    username.send_keys("yassine.derbali2611@gmail.com")
    password.clear()
    password.send_keys("SpencerYassine*123*")

    #target the login button and click it
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    #handle alerts
    #alert_1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accepter tout")]'))).click()
    time.sleep(6)
    alert_2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Enregistrer les identifiants")]'))).click()
    time.sleep(6)
    alert_3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Activer")]'))).click()
    print("instagram log in ..")

