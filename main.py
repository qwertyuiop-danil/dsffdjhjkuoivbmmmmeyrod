import requests as r
from time import sleep

url = 'https://raw.githubusercontent.com/qwertyuiop-danil/dsffdjhjkuoivbmmmmeyrod/main/main.py'

code = r.get(url).text

new_code = code
while code == new_code:
  new_code = r.get(url).text
  print("Check...")
  sleep(10)
