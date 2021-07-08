from selenium import webdriver
from insta_connector import instagram_connector
from scraping import  search_and_scrap , structure_dataframe


#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('/Users/yassinederbali/Downloads/chromedriver')

#set Keyword to search for a topic
KEYWORD = "#happy"


if __name__ == '__main__':
    instagram_connector(driver)
    images, texts = search_and_scrap(driver, KEYWORD)
    structure_dataframe(images, texts)

