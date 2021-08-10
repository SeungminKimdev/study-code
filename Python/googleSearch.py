import urllib.request
from bs4 import BeautifulSoup
from urllib import parse
import ssl
import requests
from urllib.request import urlopen

#구글 주소처리
r = requests.get('https://www.google.com/search?q=%EC%95%84%EC%9D%B4%EC%9C%A0&sxsrf=ALeKk00OtgmlC-IcfnN6TKdCuRPBUeKccQ:1628580049152&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjFjcW69aXyAhVrHKYKHZbRBhsQ_AUoAXoECAEQAw&biw=670&bih=937')
html_doc = r.text
#BeautifulSoup로 html 파일 형식으로 불러오기
soup = BeautifulSoup(html_doc,'html.parser')

#img 형식 안에서 src 값 불러오기 -> 이미지 파일 주소
for link in soup.find_all('img'):
    print(link.get('src'))