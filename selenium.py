from selenium import
import time   #для того, чтобы браузер не закрывался и можно было всё посмотреть

driver = webdriver.Chrome()   #ни короткого пути, ни самого интерпретатора в папке нет
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
time.sleep(5) #для того, чтобы браузер не закрывался и можно было всё посмотреть
driver.close()