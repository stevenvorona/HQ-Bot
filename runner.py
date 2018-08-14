import io
import os
from bs4 import BeautifulSoup
import pprint
import subprocess
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

qa = []
query = ""
for text in texts[2:]:
    if not qa:
        query += text.description + " "
        if "?" in text.description:
            qa.append(query)
            query = ""
    else:
        qa.append(text.description)

answers = qa[1:]

#strip common words
removeList = ['of','the', 'a', 'if', 'not','be','to','and']
for i in answers:
    for j in removeList:
        if j in answers:
            answers.remove(j)

service = build("customsearch", "v1",
            developerKey="devKey")

res = (service.cse().list(q=qa[0],cx='GOOGLE CSE CUSTOM CX').execute())
massiveData = ""
for key in res:
    massiveData += str(res[key]).lower()

#print massiveData
for answer in answers:
    print answer + ": " + str(massiveData.count(answer.lower()))
