import requests
from bs4 import BeautifulSoup
import openpyxl

fpath=r"C:\Users\akmris00\Desktop\기타 코딩파일\주식data.xlsx"

wb = openpyxl.load_workbook(fpath)

ws= wb.active # 현재 활성화된 시트 선택

codes = [
        '005930', #삼성전자
        '000660', #SK하이닉스
        '035720', #카카오
]

row =2

for code in codes:
  url = f"https://finance.naver.com/item/sise.naver?code={code}"
  response = requests.get(url)
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  price = soup.select_one("#_nowVal").text
  print(price)
  
  ws[f'B{row}'] = int(price) #B열
  row+=1
  
wb.save(fpath)