from os import walk
import random
import time
from PIL import Image
from scraper import scrape
from img_writer import add_text

pictures = []
for _, _, filenames in walk("pictures/"):
    for name in filenames:
        if name.startswith("holo"):
            pictures.append(name)

i = random.randint(0, len(pictures) - 1)
img = Image.open("pictures/" + pictures[i])

words = scrape()
add_text(words, img)
