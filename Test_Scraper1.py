from bs4 import BeautifulSoup
import requests
import csv

# request the website. turns it into html text
source = requests.get('http://coreyms.com').text

# Call HTML parser aka beautifulsoup on a file, and use lxml to make it an xml file
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

# Grab article for each section in the soup, so you must find it
# article = soup.find('article') old. new uses find_all in a for loop
for article in soup.find_all('article'):

    # Grab the headline
    headline = article.h2.a.text
    print(headline)

    # summary = article.div.p.text This might work, but we specifically want the entry content. this
    # could reaturn the footer or other things
    # Instead, change it slighlty to find entry content.
    summary =  article.find('div', class_='entry-content').p.text
    print(summary)

    # Grab the articles url for the video
    # This is slighlty more complicated since the url is condensed from youtube.
    # make sure to find an iframe with a specific class of youtube. Once in iframe, access it like dictionary
    # by using [] for what you are looking for
    try:
        vid_src = article.iframe['src']
        # change the embed to watch. format it with f. position 4 is where the id is located
        vid_id = vid_src.split('/')[4]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    print(yt_link)
    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()