from bs4 import BeautifulSoup
import requests
import csv

DEBUG = False

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
    summary = soup.select('p')[0].text
    # intro = '\n'.join([para.text for para in paragraphs[0:5]])
    if(DEBUG):
        print(summary)
    # add summary to the csv
    csv_writer.writerow([summary])

    # set up the next row for the csv
    csv_writer.writerow(['Headline', 'Information'])
    # now you need to find headers and get any paragraph info between each h2
    for header in soup.select('h2'):
        if(header.text == "See also[edit]"):
            break
        if(header.text == "Contents"):
            continue
        header_val = header.text[0:-6]
        if(DEBUG):
            print(header_val)
        
        nextNode = header.find_next('p')
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
