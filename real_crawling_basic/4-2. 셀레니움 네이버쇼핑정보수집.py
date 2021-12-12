from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#브라우저 생성
browser = webdriver.Chrome("C:/chromedriver.exe")

#웹사이트 열기
browser.get('http://www.naver.com')
browser.implicitly_wait(10)  #로딩이 끝날 때까지 10초까지는 기다려줌

#쇼핑 메뉴 클릭
browser.find_element_by_css_selector("a.nav.shop").click()
time.sleep(2) #쇼핑메뉴 클릭 되기전에 검색창 클릭하는게 수행될수 있으니 써준다


#검색창 클릭
search = browser.find_element_by_css_selector('input.co_srh_input._input')
search.click()

search.send_keys('아이폰13')
search.send_keys(Keys.ENTER)

# ---------------------------------------------------------------------

#스크롤 전에 높이를 확인
# execute_script는 자바스크립트 명령어를 실행가능하게 함
before_h = browser.execute_script("return window.scrollY")

#무한 스크롤 
#무한이니까 while 반복문 사용

while True:
    #맨 아래로 스크롤을 내린다.
    #거의 모든 사이트에 body 키가 존재
    browser.find_element_by_css_selector("body").send_keys(Keys.END)
    
    #스크롤 사이 페이지 로딩시간
    time.sleep(1)
    
    #스크롤 후 높이 체크
    after_h=browser.execute_script("return window.scrollY")
    
    if after_h == before_h: break
    before_h = after_h
    
#-----------------------------------------------
#상품 정보 div
items = browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")  #elements임!!! 차이 구분하기

for item in items:
    name = item.find_element_by_css_selector(".basicList_title__3P9Q7").text #이름 클래스명
    link = item.find_element_by_css_selector(".basicList_title__3P9Q7 > a").get_attribute('href') #get_attribute('속성명') : 속성명의 값을 가지고 올수 있다.
    #만약 판매 중단이 되어서 price값이 없는 경우
    try: price = item.find_element_by_css_selector(".price_num__2WUXn").text #가격 클래스명
    except: price = "판매중단"
    
    print(name, price, link)
    
    