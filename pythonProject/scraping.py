#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils import get_tags, get_hashtags, get_post_text, get_username, get_emojis, get_post_date
from mongoDB_connection import store_data_to_mongodb
import pandas as pd
import time
import os
import en_core_web_sm

#define variables
_current_path = os.getcwd()
DATA_PATH = _current_path + "/scraped_data"

#specify the path to chromedriver.exe (download and save on your computer)
driver = webdriver.Chrome('/Users/yassinederbali/Downloads/chromedriver')
"""
Description:
    Using selenium, this method wi mimc
    a web navigator behavior and 
    and search d-for instagram posts
    related to a specified key word

inputs: 
    Driver: Google chrome driver installed on local machine
    Keyword: The topic to search for (default is #happy)
    
output:
    Posts related to the keywords: Images and texts
"""
def search_and_scrap(driver , keyword):

    #target the search input field
    searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Rechercher']")))
    searchbox.clear()

    #search for the hashtag cat
    #keyword = "#happy"
    searchbox.send_keys(keyword)

    time.sleep(5)
    searchbox.send_keys(Keys.ENTER)

    time.sleep(5)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(5)

    #get images
    driver.execute_script("window.scrollTo(0, 3000);")

    time.sleep(5)
    #target all images on the page
    images = driver.find_elements_by_tag_name('img')
    images_links = [image.get_attribute('src') for image in images]
    #images =  images[:-2]

    #get texts
    images = driver.find_elements_by_tag_name('img')
    texts_raw = [image.get_attribute('alt') for image in images]
    #texts = texts[:-2]
    return images_links, texts_raw

"""
Description:
    take the scraped data and enrich it by extracting meaningful information
    Using Regex and Spacy NER
    Saving data into a csv and a mongo db
    
Inputs: Data scrapped from instagram

"""

def structure_dataframe(images , texts):
    df_scraped = pd.DataFrame(columns=['picture_link' , 'scraped_text' , \
                                   'cleaned_text' ,'username','post_date','location', 'tags'\
                                  ,'hastags', 'emojis'])

    df_scraped['picture_link'] = pd.Series(images)
    df_scraped['scraped_text'] = pd.Series(texts)

    # Form a dataframe with structure scraped data using regex and Spacy NER
    nlp = en_core_web_sm.load()

    for _, row in df_scraped.iterrows():
        if len(str(row["scraped_text"])) != 0:
            if '@' in str(row['scraped_text']):
                row['tags'] = ", ".join([m.group() for m in get_tags(row['scraped_text'])])

            if '#' in str(row['scraped_text']):
                row['hastags'] = ", ".join([m.group() for m in get_hashtags(row['scraped_text'])])

            if len(get_emojis(str(row['scraped_text']))) != 0:
                row['emojis'] = ", ".join([get_emojis(row['scraped_text'])])

            if len(str(get_username(str(row['scraped_text'])))) != 0:
                row['username'] = str(get_username(str(row['scraped_text'])))[2:-2]#"".join([str(get_username(str(row['scraped_text'])))])

            if len(str(get_post_text(str(row['scraped_text'])))) != 0:
                row['cleaned_text'] = str(get_post_text(str(row['scraped_text'])))

            if len(get_post_date(str(row['scraped_text']))) != 0:
                row['post_date'] = get_post_date(str(row['scraped_text']))[0]

            # get 1ocation of the post using Spacy NER
            doc = nlp(str(row['scraped_text']))
            for X in doc.ents:
                if X.label_ == "GPE":
                    row['location'] = X.text

    #save data to csv
    df_scraped.to_csv(DATA_PATH+"/scraped_data.csv")

    #store to mongodb
    store_data_to_mongodb(DATA_PATH+"/scraped_data.csv")