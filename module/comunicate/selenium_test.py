import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the necessary information from environment variables
email = os.getenv("GOOGLE_EMAIL")
password = os.getenv("GOOGLE_PASSWORD")
folder_name = os.getenv("FOLDER_NAME")
file_name = os.getenv("FILE_NAME")

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set up Chrome driver
driver = webdriver.Chrome()

# Open Google login page
driver.get("https://accounts.google.com")

# Log in to Google account
driver.find_element(By.ID, "identifierId").send_keys(email)
driver.find_element(By.ID, "identifierNext").click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "Passwd")))
driver.find_element(By.NAME, "Passwd").send_keys(password)
driver.find_element(By.ID, "passwordNext").click()

# Wait for login to complete
WebDriverWait(driver, 10).until(EC.url_contains("myaccount.google.com"))

# Open Google Drive
driver.get("https://drive.google.com")

# Wait for Google Drive to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".a-u")))

# Search for the folder
search_box = driver.find_element(By.CSS_SELECTOR, ".a-u .a-v-T")
search_box.send_keys(folder_name)
search_box.send_keys(Keys.ENTER)

# Open the folder
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".a-u .a-v-T")))
driver.find_element(By.CSS_SELECTOR, ".a-u .a-v-T").click()

# Search for the file
search_box = driver.find_element(By.CSS_SELECTOR, ".a-u .a-v-T")
search_box.send_keys(file_name)
search_box.send_keys(Keys.ENTER)

# Download the file
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".a-u .a-v-T")))
driver.find_element(By.CSS_SELECTOR, ".a-u .a-v-T").click()

# Close the driver
driver.quit()
