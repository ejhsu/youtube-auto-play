from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

startURL = input('please enter start youtube url: ')
driver = webdriver.Firefox()
driver.get(startURL)
prevTitle = driver.title
while True:
    print(prevTitle)
    try:
        # locate the auto play element
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".ytd-compact-autoplay-renderer a"))
        )
    finally:
        # click the auto play video
        elem = driver.find_element_by_css_selector(
            '.ytd-compact-autoplay-renderer a').click()
        
        # wait for title changes
        while True:
            if prevTitle != driver.title:
                prevTitle = driver.title
                break