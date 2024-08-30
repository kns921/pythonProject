import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import timedelta

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# запуск тестов без открытия браузера
options.add_argument('--headless')
g = Service()
driver = webdriver.Chrome(options=options, service=g)
bace_url = 'https://demoqa.com/date-picker'
driver.get(bace_url)
driver.maximize_window()

"""Today"""
now_day = datetime.datetime.now(datetime.UTC).strftime('%d/%m/%Y')
print('Today: ' + now_day)

"""Today + 10 days"""
f_day = (datetime.datetime.now(datetime.UTC)) + timedelta(days=10)
new_day = f_day.strftime('%d/%m/%Y')
print('After 10 days: ' + new_day)

"""Select date"""
select_date = driver.find_element(By.XPATH, '//*[@id="datePickerMonthYearInput"]')
select_date.send_keys(Keys.BACKSPACE * 10)

time.sleep(2)
select_date.send_keys(new_day)
select_date.send_keys(Keys.RETURN)
print(new_day + " selected")
