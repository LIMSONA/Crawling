import pyautogui
import requests
from bs4 import BeautifulSoup

keyword=pyautogui.prompt("검색어를 입력하세요>>>")
response = requests.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query={keyword}" )

html = response.text
soup = BeautifulSoup (html, 'html.parser')
links = soup.select(".news_tit") #결과는 리스트

for link in links: 
  title= link.text #태그안에 텍스트요소를 가져온다.
  url = link.attrs['href'] #href의 속성값을 가져온다
  #attrs : 속성값 모두 출력
  print(title,url)