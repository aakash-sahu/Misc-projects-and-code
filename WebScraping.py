# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:18:44 2018

@author: Aakash
"""

#Web scraping with Beautiful Soup and requests

#conda install beautifulsoup4
#conda install lxml

#many other parsrs as well.. using lxml here..
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#differences-between-parsers
#other parser html5lib

import bs4
from bs4 import BeautifulSoup
import requests
import csv


with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    
print(soup)

print(soup.prettify())

match = soup.title.text
print(match)

#find method to find all matching tags

match = soup.div
print(match)

match = soup.find('div')
print(match)

match = soup.find('div', class_ = 'footer')
print(match)

help(soup.find)

article = soup.find('div', class_ = 'article')
print(article)

headline = article.h2
print(headline)
print(headline.a)
print(headline.text)

headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)

#using find all
for article in soup.find_all('div', class_ = 'article'):
    #print(article.h2.text)
    headline = article.h2.a.text
    print(headline)
    summary = article.p.text
    print(summary)
    print()
    
    
## Getting information from actual webpage
proxies = {
  'http': '',
  'https': '',
}

#requests.get('http://example.org', proxies=proxies)

source = requests.get('http://coreyms.com', proxies=proxies).text

print(source)
type(source)

soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())

article = soup.find('article')

print(article.prettify())

#headline = article.find('h2').find('a').text
headline = article.h2.a.text
print(headline)
#article.a.text

summary = article.find('div', class_ = 'entry-content').p.text
print(summary)

#Value from attribute for a tag can be accessed as a dictionary
vid_src = article.find('iframe', class_ = 'youtube-player')['src']
print(vid_src)

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
print(vid_id)

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)


csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline','Summary','Youtube_link'])

#Now to find all articles
for article in soup.find_all('article'):

    #headline = article.find('h2').find('a').text
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div', class_ = 'entry-content').p.text
    print(summary)  
    
    #If there is error in webpage for e.g youtube link not present
    try:
      vid_src = article.find('iframe', class_ = 'youtube-player')['src']
    
      vid_id = vid_src.split('/')[4]
      vid_id = vid_id.split('?')[0]
      yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
        
    print(yt_link)
    #print()

    csv_writer.writerow([headline,summary,yt_link])
    
csv_file.close()    
