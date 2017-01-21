from bs4 import BeautifulSoup, NavigableString
from urllib.request import urlopen
import requests
import random
import time


popular_choice = ['motivational', 'life', 'positive', 'friendship', 'success', 'happiness', 'love']


def get_quotes(type, number_of_quotes=1):
    url = "http://www.brainyquote.com/quotes/topics/topic_" + type + ".html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
    quotes = []
    for quote in soup.find_all('a', {'title': 'view quote'}):
        quotes.append(quote.contents[0])
    random.shuffle(quotes)
    result = quotes[:number_of_quotes]
    return result

def reddit_test():

    url = "http://www.reddit.com/r/frugalmalefashion"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = []
    for title in soup.find_all("a", class_="title"):
        titles.append(title.text)
    return titles

def twitter_test(user):
    
    endpoint = "https://twitter.com/%s"

    f = urlopen(endpoint % user)
    html =  f.read()
    f.close()

    soup =  BeautifulSoup(html, 'html.parser') 

    tweets =  soup.find_all('strong', {'class': 'fullname js-action-profile-name show-popup-with-id'})
    results = []
    for i in range(0,len(tweets)):
        user = tweets[i].contents[0]

        action_tag = soup('span', {'class': 'username js-action-profile-name'})
        show_name = action_tag[i].contents[1].contents[0]

        twit_text = soup('p', {'class': 'js-tweet-text'})

        message = ""
        for nib in twit_text[i]:
            if isinstance(nib, NavigableString):
                message += nib
            else:
                message += nib.text

        results.append(user + " @ " + show_name + " " + message)
    return results

    
   

def get_random_quote():
    result = get_quotes(popular_choice[random.randint(0, len(popular_choice) - 1)])
    return result
for x in twitter_test("adidasalerts"):
    print(x)