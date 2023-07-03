from bs4 import BeautifulSoup
import requests
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Set the path to the EdgeDriver executable
edgedriver_path = r'C:\Users\ankur.chadha\desktop\msedgedriver'  

# Set up the Edge options
edge_options = webdriver.EdgeOptions()

# Initialize the Edge driver with the EdgeOptions object
driver = webdriver.Edge(service=Service(edgedriver_path), options=edge_options)

# Read manufacturer codes from Excel file
excel_file_path = r'C:\Users\ankur.chadha\Desktop\Automation\SKU test.xlsx'  
sku_test_df = pd.read_excel(excel_file_path)

# Get the current date and time
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Website URL template with a placeholder for the model number
website_url_template = 'https://www.bing.com/shop?q={model_number}&qs=n&form=SHOPSB&sp=-1&lq=0&pq=spt67m8-01&sc=0-10&sk=&cvid=CEC4A7799DFA4DBF9867A9C06C81D147&ghsh=0&ghacc=0&ghpl='

# Iterate over the rows in the Excel file
for index, row in sku_test_df.iterrows():
    model_number_1 = row['Model Number 1']
    model_number_2 = row['Model Number 2']
    
    # Skip iteration if both model numbers are missing
    if pd.isnull(model_number_1) and pd.isnull(model_number_2):
        continue

    # Generate the website URLs by replacing the placeholders with the model numbers
    website_url_1 = website_url_template.replace('{model_number}', str(model_number_1))
    website_url_2 = website_url_template.replace('{model_number}', str(model_number_2))

    # Loop through the websites
    for i, website_url in enumerate([website_url_1, website_url_2]):
        # Fetch the web page
        response = requests.get(website_url)

        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, 'html.parser')

        # Wait for the desired element or condition to be met
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))

        # Capture the screenshot
        screenshot_filename = f'screenshot_{model_number_1 if i == 0 else model_number_2}_{i}_{current_datetime}.png'
        driver.get("data:text/html;charset=utf-8," + str(soup))
        driver.save_screenshot(screenshot_filename)

# Close the web driver
driver.quit()

