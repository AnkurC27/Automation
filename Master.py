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
edgedriver_path = r'C:\Users\ankur.chadha\desktop\msedgedriver'  # Replace with the actual path to msedgedriver

# Set up the Edge options
edge_options = webdriver.EdgeOptions()
# Add any desired options, e.g., to run headless:
# edge_options.add_argument('--headless')

# Initialize the Edge driver with the EdgeOptions object
driver = webdriver.Edge(service=Service(edgedriver_path), options=edge_options)

# List of target websites
websites = ['https://www.bing.com/shop?FORM=SHOPTB']

# Read manufacturer codes from Excel file
excel_file_path = r'C:\Users\ankur.chadha\Desktop\Automation\SKU test.xlsx'  # Update with your Excel file path
sku_test_df = pd.read_excel(excel_file_path)

# Get the current date and time
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Iterate over the manufacturer codes
for index, row in sku_test_df.iterrows():
    model_number_1 = row['Model Number 1']
    model_number_2 = row['Model Number 2']
    item_description = row['Item Description']

    # Skip iteration if manufacturer codes are missing
    if pd.isnull(model_number_1) and pd.isnull(model_number_2):
        continue

    # Loop through the websites
    for i, website in enumerate(websites):
        # Construct the URL using manufacturer code 1
        url_1 = website + str(model_number_1)

        # Fetch the web page
        response_1 = requests.get(url_1)

        # Create a BeautifulSoup object
        soup_1 = BeautifulSoup(response_1.text, 'html.parser')

        # Check if the web page contains the desired content
        if 'No results found' not in response_1.text:
            # Capture the screenshot using manufacturer code 1
            screenshot_filename_1 = f'screenshot_{model_number_1}_{i}_{current_datetime}.png'
            driver.get("data:text/html;charset=utf-8," + str(soup_1))
            driver.save_screenshot(screenshot_filename_1)
        else:
            # Construct the URL using manufacturer code 2
            url_2 = website + str(model_number_2)

            # Fetch the web page
            response_2 = requests.get(url_2)

            # Create a BeautifulSoup object
            soup_2 = BeautifulSoup(response_2.text, 'html.parser')

            # Capture the screenshot using manufacturer code 2
            screenshot_filename_2 = f'screenshot_{model_number_2}_{i}_{current_datetime}.png'
            driver.get("data:text/html;charset=utf-8," + str(soup_2))
            driver.save_screenshot(screenshot_filename_2)

 # Construct the screenshot filenames based on item description
screenshot_filename_1 = f'screenshot_{item_description}_1_{current_datetime}.png'
screenshot_filename_2 = f'screenshot_{item_description}_2_{current_datetime}.png'

# Close the web driver
driver.quit()
