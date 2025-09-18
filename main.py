from os import listdir
import random
import time
from PIL import Image
from scraper import scrape
from img_writer import add_text

pictures = []
for name in listdir("pictures/"):
    pictures.append(name)

i = random.randint(0, len(pictures) - 1)
img = Image.open("pictures/" + pictures[i])

try:
    words = scrape()
    add_text(words, img)
except:
    print("An error occurred :( check your internet connection.")
