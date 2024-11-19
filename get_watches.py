import requests
from selectolax.parser import HTMLParser
import json
import sys
import pandas as pd


sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")


def get_watches_api():
  import requests

  url = "https://www.hublot.com/en-us/api/v1/watches?collection=1597&collection_url=/watches/big-bang&collection_name=Big%20Bang&collection_uri_name=big-bang&default_current_breadcrumb=\\[object%20Object\\]&root_name=Watches&root_uri_name=/en/watches&country_edition=US&country=US&ajax=1"

  payload = {}
  headers = {
  'sec-ch-ua-platform': '"Windows"',
  'Referer': 'https://www.hublot.com/en-us/find-your-hublot/big-bang',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'Cookie': 'HUB_UC=US; _abck=5F59847FA8D54891F77DD4F6A4002927~-1~YAAQR2l8aMnWNSyTAQAAFxy2LQyT5u7cM8QRya+krM6wIqPKlRvJvuIj9nC/QZy92TcBijc1ZBvGKE9JAahn6ZoO3Ge5d0Euc9TnQm95xanD/aPAjHxoO/QEte6r1rMVEeT4lIjs2CnlvYWlrXbDyRZ06F9DLYM9vOiw0CgBpXFhpSb01VgIXwGdweF2md8YpJYEQ7czYTQtmVA9V8NBJ1XyViaSCI3WLQc9BMDPNtm8zXN6yRJoCmVy1Qjb++0cppiGNZ45Uic+I0ATwUHLAD9QVg1twEyITaayyTeH1St8DUNeEXuWVPLjLtdSEe0k/UjwhJYPLsGuRqjNRBF9UIvQYCXkUWb5cx14XCCbQdET7VSnLNGt+X66oxdEl+FgrcF+Tg9XCt4yWsUxqjV25EPwLS2kiODvTC0eCp4=~-1~-1~-1; ak_bmsc=E7AFAAA2BC825FAFFB32564FCA9FE14E~000000000000000000000000000000~YAAQR2l8aMrWNSyTAQAAFxy2LRkyaLk7Df1o0he4d/8FS8T8lCG1otskDtaiw5MkSF7Bmzd7Lp1AHeqTxuWu3v6QovK6l4H4YBWEZH0bl+4E5N6RBPd81IymxDHecdcX4m6MFg2AJXNKUAu4NQ+ndE9Ws5wqlAoYZyKnrGB4nEy3w98wgChjQKu+X9hp2Y5wmpv9bQunlWZ82TUQ/VSMDQFAG3cRtrcqfBxQmLoSQK8y+04IPwgpKgyIN2GV/kKgjc1ZKQbajHgOSdF2/0P84OLh7/CX+qWBpHrgs00E7tpqPLkJAVvyXTiEn8lqFGBEkS1vjXB3nKdBL6ujCnPdK8iFikioWQeOlw==; bm_sz=F36ACB02834F31EC1D9F03ABEEE8EE61~YAAQR2l8aMvWNSyTAQAAFxy2LRlz39iIMIfv8ktXJvZAKXAJvNtuzgqJVu3k7VunO5JszQ2kCFraNd7VnmF+iJODEPJxNhWxovIxRm2p6Bu7MaRNSfF5QwqqRezOrkGo79oOUId3i9znm3JppvJjlCHMwUWaDpHtGur0Y8wc0wrYvpjjHFlyzS5OMnMvePk3W1uHdk2CVs6Zo3DBlwMjebYN8JdefAo7PD1LfBsPqR+yX5W7zHxevs4xNhRyqebWbbbqXWHYeU8HPK+rXqA4j89zCoT5pDqNi3LSAEIbg1elVFBUZfORQVtpbjWcKW9KewOo5pbT+qaQ5ponR2/MjfmNdVi/DjFtpX+o~3227956~4474420'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  
  with open('hublot_watches.json', 'w') as f:
    json.dump(response.json(), f, indent=4)

  
with open('hublot_watches.json', 'r') as f:
  data = json.load(f)

def keep_columns(data: dict, columns: list) -> dict:
  keys = list(data)
  for key in keys:
    if key not in columns:
      del data[key]
  return data

def process(data):
  columns = ["title_without_size", "watch_case", "size", "collection", "image", "prices", "weight", "url"]
  for item in data:
    item["prices"] = dict(item["prices"])['USD']
    item["image"] = "https://www.hublot.com/" + item["image"].split(" 1x")[1].split("data-srcset=")[1].replace('"', "")
    item["url"] = "https://www.hublot.com/" + item["url"]
  # remove unwanted column

  data = [keep_columns(item, columns) for item in data]
  return data

data = process(data)





