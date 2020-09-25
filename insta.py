# -*- coding: utf-8 -*-
"""
SPecyIN'
"""

import time
import re
import math
import shutil
import urllib
import requests
print("\n\n         Instagram Image Download Script By - SPecyIN\n\n")
url=input('Enter URL: ')
if url[0:4]!="http" and url[0:4]!="Http":
    url='https://'+url
imgreq = requests.get(url) #requests.get will get the data and store it in imgreq
src = imgreq.content.decode('utf-8') #decode to utf-8
extract_image_link = re.search('meta property="og:image" content=[\'"]?([^\'" >]+)', src)
image_link = extract_image_link.group()
imgurl = re.sub('meta property="og:image" content="', '', image_link)
filename="instaimage.jpg"
r = requests.get(imgurl, stream = True)
if r.status_code == 200:
    r.raw.decode_content = True
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)
    print('Image sucessfully Downloaded in Downloads Named :',filename)

