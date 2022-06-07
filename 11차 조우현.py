import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

#다음은 셀레니움과 BeautifulSoup를 이용하여 네이버 베스트셀러를 스크래핑 하는 코드입니다..
#다음 괄호안의 내용을 채워넣으세요.

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

#4번 크롬창을 최대로 만드는 코드를 작성하세요.
driver.maximize_window()

#5번 https://book.naver.com/search/search.nhn?query=%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%85%80%EB%9F%AC 로 접속하세요.
driver.get('https://book.naver.com/search/search.nhn?query=%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%85%80%EB%9F%AC')

#6번 5초 딜레이를 주세요.
time.sleep(5)

html =  driver.page_source #7번 html소스를 가져오는 코드를 작성하세요

bs = BeautifulSoup(html,'lxml') #8번 위 html을 이용하여 beautifulshop 객체를 만들고 파서를 lxml로 설정하세요

result = bs.find( 'ul' ,class_='basic' )   #9번 ul tag로 시작하고  #10번 class가 basic인것을 찾으세요
bookname = result.find_all('dt')

best_list = []
for temp in bookname:
    best_list.append(temp.text)

print(best_list)