import os
import sys
import urllib.request
import ssl
from urllib.request import urlopen

client_id = "bdpWYU7e70Thq9gFsYAU"
client_secret = "9JU2hmkHTD"

encText = urllib.parse.quote("반갑습니다 네이버")
data = "speaker=mijin&speed=0&text=" + encText

url = "https://openapi.naver.com/v1/voice/tts.bin"
request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode('utf-8'))
rescode = response.getcode()

if(rescode==200):
    print("TTS mp3 저장")
    response_body = response.read()
    with open('1111.mp3', 'wb') as f:
        f.write(response_body)
else:
    print("Error Code:" + rescode)