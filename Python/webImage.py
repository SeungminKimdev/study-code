import urllib.request
from bs4 import BeautifulSoup

print('Beginning file download with urllib2...')

url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%EC%95%84%EC%9D%B4%EC%9C%A0'
req = urllib.request.Request(url)
res = urllib.request.urlopen(url).read()

soup = BeautifulSoup(res,'html.parser')
print(soup)
soup = soup.find("div",class_="big_thumb")
#img의 경로를 받아온다
imgUrl = soup.find("img")["src"]

#urlretrieve는 다운로드 함수
#img.alt는 이미지 대체 텍스트 == 마약왕
urllib.request.urlretrieve(imgUrl, soup.find("img")["alt"]+'.jpg')