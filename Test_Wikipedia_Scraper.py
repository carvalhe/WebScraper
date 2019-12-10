from bs4 import BeautifulSoup
import requests
import csv
import re

DEBUG = False

#### Set up where you are requesting from
user_input = input("Enter your search string: ")
# Add the user_input toe the google search url and request that
search_input = f'https://wikipedia.org/wiki/{user_input}'
search_input.replace(" ", "_")
source = requests.get(search_input)

#### create soup from the page
if(source is not None):
    soup = BeautifulSoup(source.text, 'lxml')
    #if(DEBUG):
    #    print(soup.prettify())
    #article = soup.find('div', class_='mw-parsed-output')
    #print(article)

    #### Parse through the soup for the information you want
    # The first grab the main elements of the page
    summary = soup.select('p')[0].text
    # intro = '\n'.join([para.text for para in paragraphs[0:5]])
    if(DEBUG):
        print(summary)
    # now you need to find headers and get any paragraph info between each h2
    for header in soup.select('h2'):
        if(header.text == "See also[edit]"):
            break
        if(header.text == "Contents"):
            continue
        header_val = header.text[0:-6]
        paragraph = header.find_next('p').text
        print(header_val)
        print(paragraph)


