from bs4 import BeautifulSoup
import requests
import csv

DEBUG = True

#### Set up where you are requesting from
user_input = input("Enter your search string: ")
# Add the user_input toe the google search url and request that
search_input = f'https://wikipedia.org/wiki/{user_input}'
search_input.replace(" ", "_")
source = requests.get(search_input).text

#### create soup from the page
soup = BeautifulSoup(source, 'lxml')
if(DEBUG):
    print(soup.prettify())
#### Parse through the soup for the information you want
# The first grab the main elements of the page, div has class=mw
# main_page = soup.find('div', id='search')

