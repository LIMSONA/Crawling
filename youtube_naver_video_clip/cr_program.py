from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 실행시 에러메시지 해결
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def youtube_program(video_url):
    try:    
        driver.get(url=video_url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
        return title
    except:
        return "오류발생"
    finally:
            driver.close()
        # #bs4로
        # url= requests.get(video_url)
        # soup= BeautifulSoup(url.text, "lxml")
        # title = soup.select_one('meta[itemprop="name"][content]')['content']
        # return title
        
        
def naver_program(video_url):
        try:
            while True:
                driver.get(video_url)
                # 영상 제목
                n_title = driver.find_element_by_class_name('LiveHeader_text_2XGaZ').text
                return n_title
        except:
            print("오류발생")
        finally:
            driver.close()


want= input()
if "youtube" in want:
    youtube_program(want)
else:
    naver_program(want)
