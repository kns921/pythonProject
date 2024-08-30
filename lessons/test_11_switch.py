from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# запуск тестов без открытия браузера
options.add_argument('--headless')
g = Service()
driver = webdriver.Chrome(options=options, service=g)
bace_url = 'https://demoqa.com/browser-windows'
driver.get(bace_url)
driver.maximize_window()

""""Switch tab"""
click_but = driver.find_element(By.XPATH, '//*[@id="tabButton"]')
click_but.click()
print(driver.current_url)
print('Button New Tab Click')

driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)
header_tab = driver.find_element(By.XPATH, '//*[@id="sampleHeading"]')
header_tab = header_tab.text
print('Header New Tab: ' + header_tab)

# Switch Back
driver.switch_to.window(driver.window_handles[0])

"""Switch Windows"""
click_new_win = driver.find_element(By.XPATH, '//*[@id="windowButton"]')
click_new_win.click()
print(driver.current_url)
print('Button New Window Click')

win_1 = driver.window_handles[0]
win_2 = driver.window_handles[1]
driver.switch_to.window(win_2)
print(driver.current_url)

header_win = driver.find_element(By.XPATH, '//*[@id="sampleHeading"]')
header_win = header_win.text
print('Header New Window: ' + header_win)
