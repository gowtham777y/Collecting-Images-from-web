from bs4 import BeautifulSoup
import requests
import random

for i in range(1,4):
    html_text=requests.get('https://www.gettyimages.in/photos/telangana-indians?family=creative&license=rf&page='+str(i)+'&phrase=telangana%20indians&sort=mostpopular#license').text #This iterates over 4 pages of images
    soup=BeautifulSoup(html_text,'lxml')
    images=soup.find_all('img',class_='gallery-asset__thumb gallery-mosaic-asset__thumb')
    for image in images:
        name='TS_'+str(random.randrange(3730,4035))
        link=image['src']
        with open(f'Photos/{name}.jpg','wb') as f: #wb is to store with bytes
            im =requests.get(link)
            f.write(im.content)
