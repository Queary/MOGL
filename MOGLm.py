import requests
#from tqdm import tqdm
from urllib.parse import urlencode
#import patoolib
#import os
#import shutil
#import subprocess
#from tqdm import tqdm
#import sys

#0.0.1 - добавить unpack rar или сразу в папку

#скачивается с яндекс облака
def Download_Y(link,title):
    base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
    public_key = link
    final_url = base_url + urlencode(dict(public_key=public_key))
    response = requests.get(final_url)
    download_url = response.json()['href']
    download_response = requests.get(download_url)
    with open(title, 'wb') as f:
        f.write(download_response.content)
    return True