import io
import os
from bs4 import BeautifulSoup
import pprint
import subprocess
import requests

from googleapiclient.discovery import build
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'bots.png')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

#remove vision. part?
image = vision.types.Image(content=content)

# Performs label detection on the image file
response = client.text_detection(image=image)
texts = response.text_annotations

query = ""
linenum = 0
for text in texts[3:]:
    query += text.description + " "
    linenum+=1
    if "?" in text.description:
        break

question = query
answers = ((texts[0].description).splitlines())[linenum-5:]

for answer in answers:
    question += ' \"' + answer + '\"'
    r = requests.get("https://www.google.com/search", params={'q':question})

    data = BeautifulSoup(r.text, "lxml")
    res = data.find("div", {"id": "resultStats"})
    count = res.text
    count = (count).replace('About ', '')
    count = (count).replace('results', '')
    print answer + ": " + count
    question = query
