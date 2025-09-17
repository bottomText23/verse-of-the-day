import time
from PIL import Image
from scraper import scrape
from img_writer import add_text

img = Image.open("pictures/holo_grapes.jpg")

words = scrape()
add_text(words, img)

print("finished")
