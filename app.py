from flask import Flask
from flask import redirect, render_template, request
import requests
import time 
from bs4 import BeautifulSoup

app = Flask(__name__)

url = 'https://tenki.jp/forecast/9/43/8240/40203/'
response = requests.get(url)
response.encoding = response.apparent_encoding
result = response.text 

bs = BeautifulSoup(response.text,'html.parser')
tennki = bs.find('p',class_='weather-telop')

tennki = tennki.text
@app.route("/")
def hello_world():
    return render_template('index.html',tennki=tennki)