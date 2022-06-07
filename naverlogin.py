import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyperclip

naverid = 'skywoohyun'
naverpw = '@whdngus1993'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()

driver.get('https://www.naver.com')

time.sleep(1)

driver.find_element(By.CLASS_NAME, 'link_login').click()
time.sleep(2)

# driver.find_element(By.ID, 'id').send_keys('skywoohyun')
# time.sleep(2)
# driver.find_element(By.ID, 'pw').send_keys('@whdngus1993')
# time.sleep(2)
# driver.find_element(By.CLASS_NAME, 'btn_login').click()

#위와 같은 방법은 네이버에서 걸린다.
#그래서 복사 붙혀넣기 방법으로 써야 한다.

driver.find_element(By.ID, 'id').click()
pyperclip.copy(naverid)
driver.find_element(By.ID,'id').send_keys(Keys.CONTROL,'v')
time.sleep(1)

driver.find_element(By.ID, 'pw').click()
pyperclip.copy(naverpw)
driver.find_element(By.ID,'pw').send_keys(Keys.CONTROL,'v')
time.sleep(1)

driver.find_element(By.CLASS_NAME, 'btn_login').click()
time.sleep(1)

driver.find_element(By.ID, 'new.dontsave').click()