import requests

url = "https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1653264000&period2=1684800000&interval=1d&events=history&includeAdjustedClose=true"
 
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

content = requests.get(url, headers=headers).content

print(content)