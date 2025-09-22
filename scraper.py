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

    #get quote and verse
    s_quote = soup.find("div", attrs={"class":"bilingual-left"})
    s_verse = soup.find("div", attrs={"class":"reference"})
    
    #get only verse text for quote
    quote = s_quote.contents[0].text
    verse = s_verse.text

    return split_text(quote, verse)
