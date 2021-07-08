import csv
from pymongo import MongoClient

def store_data_to_mongodb(filepath):

    csvfile = open(filepath, 'r')
    reader = csv.DictReader(csvfile)
    mongo_client = MongoClient()
    db = mongo_client.october_mug_talk
    db.segment.drop()

    # naming columns
    header = ['picture_link', 'scraped_text', \
              'cleaned_text', 'username', 'post_date', 'location', 'tags' \
        , 'hastags', 'emojis']

    for each in reader:
        row = {}
        for field in header:
            row[field] = each[field]

        db.segment.insert(row)


