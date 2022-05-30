pip install google-play-scraper

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google_play_scraper import app, Sort, reviews_all
from tqdm import tqdm

#Define and configure PlayStore Scrapper Library, and
#Input apps link form google play store exp: com.dinnerdash.global
hk_users_reviews = reviews_all(
    'com.InputAppsLink',
    sleep_milliseconds=0,
    lang='id',
    sort=Sort.NEWEST,
    count= 100
)

def print_json(json_object):
  json_str = json.dumps(
    json_object,
    indent=2,
    sort_keys=True,
    default=str
  )
  print(highlight(json_str, JsonLexer(), TerminalFormatter()))

#convert collected reviews data into dataframe
df_reviews = pd.DataFrame(np.array(hk_users_reviews), columns=['review'])
df_reviews= df_reviews.join(pd.DataFrame(df_reviews.pop('review').tolist()))
#display dataframe header
df_reviews.head()

import json
import re
import csv
from csv import reader
from csv import DictWriter, writer
from datetime import date, time, datetime
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import pandas as pd
import numpy as np

df_reviews.to_csv('NameYourFile.csv')

review_properties = {}

with open('YourFileName.csv', 'r', encoding='utf8') as f:
  cf = csv.DictReader(f)
  with open('YourFileName-clean.csv', 'w', encoding="utf8", newline='') as f:
      csv_writer = DictWriter(f, fieldnames=['reviewID', 'userName', 'content', 'score', 'thumbsUpCount', 'reviewCreatedVersion', 'at', 'replyContent', 'replyAt'])
       
      csv_writer.writeheader()
      for row in cf:
              review_properties['content'] = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "",row['content'].lower())
              review_properties['replyContent'] = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "",row['replyContent'].lower())

              csv_writer.writerow({
                            'reviewID' : row['reviewId'],
                            'userName' : row['userName'],
                            'content' : review_properties['content'],
                            'score' : row['score'],
                            'thumbsUpCount' : row['thumbsUpCount'],
                            #'review' : review_properties['review'],
                            #'review_count' : row['review_count'],
                            #'score_count' : row['score_count'],
                            'reviewCreatedVersion' : row['reviewCreatedVersion'],
                            'at' : row['at'],
                            'replyContent' : review_properties['replyContent'],
                            #'replyAt' : row['replyAt']
                            })

print("DONE!")