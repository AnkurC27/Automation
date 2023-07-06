from bs4 import BeautifulSoup
import requests
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# Set the path to the directory containing the EdgeDriver executable
edgedriver_dir = r'C:\Users\ankur.chadha\desktop\msedgedriver'  # Replace with the directory containing msedgedriver

# Set up the Edge options
edge_options = webdriver.EdgeOptions()

# Add the Edge driver directory to the PATH environment variable
os.environ["PATH"] += os.pathsep + edgedriver_dir

# Initialize the Edge driver
driver = webdriver.Edge(options=edge_options)

# List of websites
websites = ['https://www.espn.com', 'https://www.nike.com', 'https://www.knicks.com']

# Open each website and take 2 screenshots
for website in websites:
    
    driver.get(website)

    # Take 2 screenshots
    for i in range(2):
        # Take a screenshot
        screenshot_filename = f'{website.replace("https://www.", "")}_screenshot_{i+1}.png'
        driver.save_screenshot(screenshot_filename)

# Close the web driver
driver.quit()