import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#가장 많이 사용하는 라이브러리 임포트

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
#코드가 끝나도 크롬이 닫히는 것을 방지하는 옵션, 나중에라도 꼭 해주기

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()#크롬창이 최대 사이즈로 변경

driver.get('https://www.naver.com')
#네이버 홈페이지로 접속 get()
time.sleep(3)
#3초 정도 기다리게 한다.

#driver.quit() #크롬 완전히 닫기
# driver.back()#뒤로가기
# driver.forward()#앞으로가기

#탭이동
# driver.switch_to.window(driver.window_handles[0])
#탭닫기
#driver.switch_to.window(driver.window_handles[0])
#driver.close()

# #HTML가져오기
# html = driver.page_source
# print(html)

#셀레니움 element 버튼 이나 사진 검색창등
#xpath, 클래스 이름, id 이름, 링크나 등등 다양한 방법으로 접근
#접근후 클릭이나 텍스트 입력 삭제=클리어 등 액셕을 취할수 있다.


#naver에 접속후 검색 해보기, xpath경로를 통해
#//*[@id="query"]

#driver.find_element(By.XPATH, '//*[@id="query"]').send_keys('커피')
#검색창의 xpath를 찾아서 커피를 입력
#driver.find_element(By.ID, 'search_btn').click()
#검색 단추의 아이디를 찾아서 클릭 입력

#time.sleep(3)

#셀레니움을 활용하여 네이버 로그인



