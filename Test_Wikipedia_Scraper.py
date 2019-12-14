#### Switching branch name
from bs4 import BeautifulSoup
import requests
import csv

DEBUG = True

#### Set up where you are requesting from
user_input = input("Enter your search string: ")
# Add the user_input toe the google search url and request that
search_input = f'https://wikipedia.org/wiki/{user_input}'
search_input.replace(" ", "_")
source = requests.get(search_input)

#### Create a csv file to store information later
# do a w for write
csv_file = open('wiki_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Summary'])




#### create soup from the page
if(source is not None):
    soup = BeautifulSoup(source.text, 'lxml')
    #if(DEBUG):
    #    print(soup.prettify())
    #article = soup.find('div', class_='mw-parsed-output')
    #print(article)

    #### Parse through the soup for the information you want
    # The first grab the main elements of the page
    summary = soup.select('p')[1].text
    # intro = '\n'.join([para.text for para in paragraphs[0:5]])
    if(DEBUG):
        print(summary)
    # add summary to the csv
    csv_writer.writerow([summary])

    # set up the next row for the csv
    csv_writer.writerow(['Headline', 'Information'])
    # now you need to find headers and get any paragraph info between each h2
    for header in soup.select('h2'):
        if(header.text == "External links[edit]"):
            break
        if(header.text == "Contents") or header.text == "Notes[edit]" or header.text == "See also[edit]":
            continue
        if(header.text == "References[edit]"):
            csv_writer.writerow(['References'])
            # this is the bottom of the page, make a specific section in csv file for links in references
            # loop through any <li> given
            nextNode = header.find_next('li')
            '''
            for refrences in header.find('li'):
                if refrences.name == 'li':
                    print('yes')
                else:
                    print(refrences.name)
                    print('no')
                    break

            while(True):
                
                if nextNode.name == 'li':
                    citation = nextNode.find('cite', class_='citation web')
                    link = citation.find('a', href= [True])
                    link = link['href']
                    # must split it to grab the hyperlink
                    citation = citation.text.split("href")
                    csv_writer.writerow([citation, link])
                else:
                    print(nextNode.name)
                    break
                '''
            citation = nextNode.find('cite', class_='citation web')
            link = citation.find('a', href= [True])
            link = link['href']
            # must split it to grab the hyperlink
            citation = citation.text.split("href")
            csv_writer.writerow([citation, link])


            break
        else:
            header_val = header.text[0:-6]
            if(DEBUG):
                print(header_val)
            
            nextNode = header.find_next('p')
            # print(nextNode.text)
            paragraph = nextNode.text + '\n'
            
            if(DEBUG):
                print(nextNode.text)
            while True:
                nextNode = nextNode.next_sibling
                if nextNode.name == 'p':
                    paragraph += nextNode.text + '\n'
                    if(DEBUG):
                        print (nextNode.text)
                else:
                    break
            csv_writer.writerow([header_val, paragraph])

csv_file.close()
