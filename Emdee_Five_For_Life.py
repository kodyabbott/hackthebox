from bs4 import BeautifulSoup
import hashlib
import requests


def computeMD5hash(my_string):
	m=hashlib.md5()
	m.update(my_string.encode('utf-8'))
	return m.hexdigest()

url = "http://docker.hackthebox.eu:59911"

response1= requests.get(url)
response1.content
soup1 = BeautifulSoup(response1.content , "html.parser")
text_to_md5 = soup1.find('h3').text
md5_string = computeMD5hash(text_to_md5)
headers = {
    'Referer': 'http://docker.hackthebox.eu:59911/'
}

response2=requests.post(url,data={'hash': md5_string },headers=headers ,cookies=response1.cookies)
soup2 = BeautifulSoup(response2.content , "html.parser")
flag = soup2.find('p').text
print flag

