#김포에서 제주로 가는 편도 항공편을 검색 후
#스크래핑, 뷰티풀을 통해 텍스트 정리
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyperclip
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

#driver.maximize_window()

page = 'https://flight.naver.com'
driver.get(page)

time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div/div[1]/button[2]/i').click()
time.sleep(1)

#출발지 버튼
# tabContent_route__1GI8F select_City__2NOOZ start
driver.find_element(By.CLASS_NAME,'start').click()
time.sleep(1)

driver.find_element(By.CLASS_NAME,'autocomplete_input__1vVkF').send_keys('김포')
time.sleep(1)

#//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/div/a[1]/div/div[1]/i[1]
driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/div/a[1]/div/div[1]/i[1]').click()
time.sleep(1)

driver.find_element(By.CLASS_NAME,'end').click()
time.sleep(1)

driver.find_element(By.CLASS_NAME,'autocomplete_input__1vVkF').send_keys('제주')
time.sleep(1)

driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/div/a').click()
time.sleep(1)

driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button').click()
time.sleep(1)

#month를 속성값을 받아서
#월선택
monthdata = driver.find_elements(By.CLASS_NAME,'month')
days = monthdata[0].find_elements(By.CLASS_NAME,'num')

#print('days :',len(days))
#일선택 예시로 오늘 선택
days[23].click() # 오늘 클릭
time.sleep(2)

driver.find_element(By.CLASS_NAME,'searchBox_search__2KFn3').click()
#항공권 검색 버튼
time.sleep(10)

html = driver.page_source
bs = BeautifulSoup(html,'lxml')
results = bs.find_all('div', class_='result')


for temp in results:
    rdict = {}
    rdict['항공사'] = temp.find('img',class_='logo')['alt']

    timedata = temp.find_all('b',class_='route_time__-2Z1T')
    rdict['출발시간'] = timedata[0].text
    rdict['도착시간'] = timedata[1].text

    rdict['요금'] = temp.find('i',class_='domestic_num__2roTW').text

    print(rdict)
