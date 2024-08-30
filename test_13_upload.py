from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# запуск тестов без открытия браузера
# options.add_argument('--headless')
g = Service()
driver = webdriver.Chrome(options=options, service=g)
bace_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
driver.get(bace_url)
driver.maximize_window()

path_upload = 'test/test.txt'

click_upload = driver.find_element(By.XPATH, '//*[@id="file"]')

click_but = driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
click_but.click()

click_upload.send_keys(path_upload)
