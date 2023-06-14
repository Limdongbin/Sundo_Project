import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 한국보호지역 통합 DB 관리 시스템 페이지로 이동
    driver.get('http://www.kdpa.kr/#')
    print('페이지 이동')

    driver.execute_script("arguments[0].setAttribute('style', 'display: block;')",
                          driver.find_element(By.ID, "download_list"))
    print('파일 다운로드 리스트 display 변경 (none => block)')

    sub_menu = driver.find_element(By.ID, 'download_list')
    sub_menu_li = sub_menu.find_elements(By.TAG_NAME, 'li')
    sub_menu_li[0].click()
    print('SHP 다운로드 클릭')
    time.sleep(1)

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(20)
    print('다운로드 확인')

    driver.close()


except Exception as e:
    # 위 코드에서 에러가 발생한 경우 출력
    print(e)



