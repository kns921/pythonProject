from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_settings():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument('--headless')
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    bace_url = 'https://www.saucedemo.com/'
    driver.get(bace_url)
    driver.maximize_window()
    print('Start test')
