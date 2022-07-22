import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import random

url = urllib.request.urlopen('https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US')



def parse(url):

    soup = BeautifulSoup(url,'xml')


    data_frame = pd.DataFrame(columns=['title','description','guid','link','pubDate','visits'])


    articles = soup.find_all('item')
    items_length = len(articles)


    for index,item in enumerate(articles):
        title = item.find('title').text
        description = item.find('description').text
        guid = item.find('guid').text
        link = item.find('link').text
        pub_date = item.find('pubDate').text
        visits = str(random.randint(1,1000)).format("0.f")
        


        row = {
            'title': title,
            'description':description,
            'guid':guid,
            'link':link,
            'pubDate':pub_date,
            'visits':visits
        }


        data_frame = data_frame.append(row, ignore_index=True)
        print(f'Appending row %s of %s' % (index+1, items_length))

    return data_frame
    


data_frame = parse(url)
data_frame.to_csv('yahoo.csv')





