import requests
import tqdm
from urllib.parse import urlencode
import patoolib
import os
import shutil
import subprocess

md = "TestMOGL"
df = "downloaded_file.zip"
mi = 26
#os.getcwd() - путь к текущей папке где запущен файл
#Popen(["/usr/bin/git", "commit", "-m", "Fixes a bug."])
#"""
#первый этап загрузка
base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
public_key = 'https://disk.yandex.ru/d/9c8-tFh7olg70A' 
final_url = base_url + urlencode(dict(public_key=public_key))
print(final_url)
response = requests.get(final_url)
print(response)
download_url = response.json()['href']
print(download_url)
download_response = requests.get(download_url)
print(download_response)
#print(download_response.content) - жесткое зависание
print(subprocess.run("1:1"))

with open('downloaded_file.zip', 'wb') as f,i in i+=1:
    print(i)
    print(len(download_response.content))
    print("1")
    f.write(download_response.content)
#"""
#перед этим удаление mods
if(os.path.isdir(md)):
   print("файл есть "+str(md))
   shutil.rmtree(md)
   print("файл удален "+str(md))
else:
    print("файл не найден "+mf)
'''
if(os.path.isdir(mf)):
   print("файл есть "+str(mf))
   shutil.rmtree(mf)
   print("файл удален "+str(mf))
else:
    print("файл не найден "+mf)
'''
#перемещение модс
#разархивация
patoolib.extract_archive(df, outdir="./")
print("файл разархивирован "+df)
#удаление rar
try:
    os.remove(df) #shutil.rmtree(df)(old)
    print("файл rar удален "+df)
except:
    print("не удалось удалить файл "+df)

