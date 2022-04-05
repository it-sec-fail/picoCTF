#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import gmpy2

n=1280678415822214057864524798453297819181910621573945477544758171055968245116423923
c=62324783949134119159408816513334912534343517300880137691662780895409992760262021
e=65537
counter=0

url = 'http://factordb.com/index.php'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
params = {'query': str(n)}

try:
    print("Getting primes from factordb.com")
    response = requests.get(url, headers=headers, params=params)
    soup = BeautifulSoup(response.text,'html.parser')
except:
    print("something went wrong...")
    exit(1)

print("Got the numbers...")

for number in soup.find_all("font",{"color": "#000000"}):
    if counter < 1:
        p = int(number.get_text())
    else:
        q = int(number.get_text())
    counter=counter+1

print("Lets decrypt then...")
ph = (p-1)*(q-1)
d = gmpy2.invert(e, ph)
plaintext = pow(c, d, n)
print("Flag: {}".format(bytearray.fromhex(format(plaintext, 'x')).decode()))
