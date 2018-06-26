import requests
import json
from pprint import pprint
import urllib, os
from urllib.request import urlretrieve
import time
from tqdm import tqdm
import sys

sid = sys.argv[1]
eid = sys.argv[2]
#cid = '3316'

headers = {
    'Pragma': 'no-cache',
    'Origin': 'http://h5.super-dreamers.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3472.0 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json, text/plain, */*',
    'Cache-Control': 'no-cache',
    'Referer': 'http://h5.super-dreamers.com/',
    'Connection': 'keep-alive',
}

for j in range(int(sid), int(eid)+1):
    cid =str(j)
    data = [
      ('id', cid),
    ]

    response = requests.post('http://api.super-dreamers.com/mobile/chapter/load-more', headers=headers, data=data)
    result = json.loads(response.content)
    t = result['chapter']['chapterPicVos']
    urls = [i['picUrl'] for i in t]
    pprint(urls)

    directory = cid
    if not os.path.exists(directory):
        os.makedirs(directory)

    for idx, url in tqdm(enumerate(urls)):
        urlretrieve(url, cid + '/' + str(idx) + ".jpg")
        print('[Done]', url, idx, cid)
        time.sleep(0.7)

