from bs4 import BeautifulSoup
import requests

def split_text(quote, verse):
    words = []
    n = 0
    while n <= (len(quote) - 1):
        words = words + quote[n].split()
        n += 1

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
    quote = [] 
    n = 0
    while n <= (len(s_quote.contents) - 2):
        quote.append(s_quote.contents[n].text)
        n += 1
    
    #get book, chapter and verse number
    verse = s_verse.text

    return split_text(quote, verse)
