from bs4 import BeautifulSoup
import requests

def split_text(quote, verse):
    words = quote.split()
    words.append(verse)
    return words

def scrape():
    #get the html of the website
    webpage = requests.get("https://www.verseoftheday.com/en/")
    soup = BeautifulSoup(webpage.text, "html.parser")

    #get quote and verse in array n_text
    s_text = soup.find_all("div", attrs={"class":"bilingual-left"})
    n_text = s_text[0].text.split("—")

    quote = n_text[0]
    verse = n_text[1]

    return split_text(quote, verse)
