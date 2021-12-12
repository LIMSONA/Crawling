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