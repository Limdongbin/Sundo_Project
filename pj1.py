from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

# Chrome 드라이버 경로 지정
driver_path = 'C:\python\Sources\project\data\chromedriver_win32\chromedriver.exe'

# Service 객체 생성
service = Service(driver_path)

# WebDriver 초기화
driver = webdriver.Chrome(service=service)

# 웹 페이지 열기
driver.get("http://www.kdpa.kr")

# ul 요소 열기 (display 속성을 변경하여 보이게 함)
driver.execute_script("arguments[0].style.display = 'block';", driver.find_element(By.ID, "download_list"))

# 첫 번째 li 요소의 a 버튼 클릭
first_li_element = driver.find_element(By.CSS_SELECTOR, "#download_list li:first-child")
a_element = first_li_element.find_element(By.TAG_NAME, "a")
a_element.click()

# 경고 대화 상자 승인 (확인 버튼 클릭)
alert = Alert(driver)
alert.accept()

# 대기 시간 설정
WebDriverWait(driver, 30).until(EC.url_contains(".zip"))

# WebDriver 종료
driver.quit()