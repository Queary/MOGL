import requests
from tqdm import tqdm
from urllib.parse import urlencode
import patoolib
import os
import shutil
import subprocess
from tqdm import tqdm
import sys

f = 0
md = "TestMOGL"
df = "downloaded_file.zip"
#mi = 26


def sizeof_fmt(num: int | float) -> str:
    for x in ['bytes', 'KB', 'MB', 'GB']:
        if num < 1024.0:
            return "%.1f %s" % (num, x)

        num /= 1024.0

    return "%.1f %s" % (num, 'TB')


url = 'https://downloader.disk.yandex.ru/zip/fedab54a1d8ce3c2e96cd12bc0fd47eb377b7fa5314c005fb90622d45940d549/677282fd/VGFvNDNUbHZPQWxDbzNNamcwK3lvdHk0dHFnV0I4V0FpMU9PTlBmM3pJSjRLK0hlaEp2MCt6Yng3WGREOTdYbHEvSjZicG1SeU9Kb25UM1ZvWG5EYWc9PQ==?uid=0&filename=TestMOGL.zip&disposition=attachment&hash=Tao43TlvOAlCo3Mjg0%2Byoty4tqgWB8WAi1OONPf3zIJ4K%2BHehJv0%2Bzbx7XdD97Xlq/J6bpmRyOJonT3VoXnDag%3D%3D&limit=0&owner_uid=290028591&tknv=v2'
# Streaming, so we can iterate over the response.
base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
public_key = 'https://disk.yandex.ru/d/9c8-tFh7olg70A'
final_url = base_url + urlencode(dict(public_key=public_key))
response = requests.get(final_url)
download_url = response.json()['href']
rs = requests.get(download_url, stream=True)

# Total size in bytes.
total_size = int(rs.headers.get('content-length', 0))
#print('From content-length:', sizeof_fmt(total_size))

chunk_size = 1024
print(str(total_size) + " total size")
num_bars = int(total_size / chunk_size)
print(str(num_bars) + " num_bars")
file_name = os.path.basename("downloaded_file.zip")
#file_data = open(file_name, mode='rb').read()
#print('/', sizeof_fmt(len(file_data)))
if(f == 1):print("113Mб")
with open("downloaded_file.zip", mode='wb') as f:
    for data in tqdm(rs.iter_content(chunk_size), total=num_bars, unit='Kb', file=sys.stdout):
        
        f.write(data)
#file_data = open(rs, mode='rb').read()


#"""
#перед этим удаление mods
if(os.path.isdir(md)):
   print("файл есть "+str(md))
   shutil.rmtree(md)
   print("файл удален "+str(md))
else:
    print("файл не найден "+md)
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

EX = input()
#показать конец
print("нажмите enter чтобы закрыть программу щегла")

