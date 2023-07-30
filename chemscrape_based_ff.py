import sys
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

options = webdriver.FirefoxOptions()
firefox_path = GeckoDriverManager().install()
firefox_service = Service(firefox_path)

print("Creating driver")
driver = webdriver.Firefox(options=options)
print("Driver created")

with open("links_record.txt") as file:
    links = [line.rstrip() for line in file]

links = list(reversed(links))
links = links[int(sys.argv[1]):]

driver.implicitly_wait(5)

wait_time = 30
wait = WebDriverWait(driver, wait_time)

for link in links:
    if link == "/Chemical-Structure.21111803.html":
        # skip
        continue

    full_link = "http://www.chemspider.com" + link
    print("Visiting", full_link)
    driver.get(full_link)

    try:
        # Wait for the page to load the 3D button
        btn_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[title="3D"]')))

        # Click it
        btn_element.click()

        # We know the 3D structure is ready when the "switch to 2D" button appears
        _ = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[title="2D"]')))

        time.sleep(2)

        # Find the button whose title attribute is "Save"
        download_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[title="Save"]')))

        download_button.click()

    except TimeoutException:
        with open("errors.txt", "a") as myfile:
            myfile.write(full_link + "\n")

        print("Too slow :(")

driver.quit()
