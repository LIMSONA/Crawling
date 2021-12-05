import requests
from bs4 import BeautifulSoup

keyword= input("검색어를 입력하세요>>>")
lastpage= int(input("마지막 페이지번호를 입력해주세요>>>"))
pageNum=1
for i in range(1,lastpage*10,10):
  print(f"{pageNum}페이지 입니다.==========================")
  response = requests.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query={keyword}&start={i}")
  html = response.text
  soup = BeautifulSoup (html, 'html.parser')
  links = soup.select(".news_tit") #결과는 리스트

  for link in links: 
    title= link.text #태그안에 텍스트요소를 가져온다.
    url = link.attrs['href'] #href의 속성값을 가져온다
    #attrs : 속성값 모두 출력
    print(title,url)
  pageNum+=1