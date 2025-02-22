import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time 

def scrape_website(website):
    print("Launching Chrome...")

    chrome_driver_path = "C:\Users\admin\Downloads\chromedriver-win64_133.0.6943.126\chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try: 
        driver.get(website)
        print("Page Loaded!")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()