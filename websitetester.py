from bs4 import BeautifulSoup, NavigableString
from urllib2 import urlopen, Request
import random
import time

class Scraper:

    popular_choice = ['motivational', 'life', 'positive', 'friendship', 'success', 'happiness', 'love']


    def scrape_quotes(self, type, number_of_quotes=1):
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

    def scrape_reddit(self, subreddit):

        url = "http://www.reddit.com/r/" + subreddit
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        titles = []
        for title in soup.find_all("a", class_="title"):
            titles.append(title.text)
        return titles

    def scrape_twitter(self, user):
        
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
        result = scrape_quotes(popular_choice[random.randint(0, len(popular_choice) - 1)])
        return result

    def __init__(self):
        pass
'''
s = Scraper()
for x in s.scrape_twitter("adidasalerts"):
    print(x)
'''