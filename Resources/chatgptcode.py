from bs4 import BeautifulSoup
import requests
import datetime
import pandas as pd
from selenium import webdriver

# Set the path to the EdgeDriver executable
edgedriver_path = 'C:\Users\ankur.chadha\desktop\msedgedriver'  # Replace with the actual path to msedgedriver

# Set up the Edge options
edge_options = webdriver.EdgeOptions()
# Add any desired options, e.g., to run headless:
# edge_options.add_argument('--headless')

# Initialize the Edge driver
driver = webdriver.Edge(executable_path=edgedriver_path, options=edge_options)

# List of target websites
websites = [https://www.bing.com/shop?FORM=SHOPTB]

# Read manufacturer codes from Excel file
excel_file_path = 'C:\Users\ankur.chadha\Desktop\Automation\sku_test.xlsx'  # Update with your Excel file path
sku_test_df = pd.read_excel(excel_file_path)

# Get the current date and time
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Iterate over the manufacturer codes
for index, row in sku_test_df.iterrows():
    manufacturer_code_1 = row['Manufacturer Code 1']
    manufacturer_code_2 = row['Manufacturer Code 2']
    item_description = row['item description']

#skip iteration if manufacturer codes are missing
if pd.isnull(manufacturer_code_1) or pd.isnull(manufacturer_code_2):
continue


 # Construct the screenshot filename based on item description
screenshot_filename_1 = f'screenshot_{item_description}_{i}_{current_datetime}.png'
driver.save_screenshot(screenshot_filename_1)

    # Loop through the websites
    for i, website in enumerate(websites):
        # Construct the URL using manufacturer code 1
        url_1 = website + manufacturer_code_1

        # Fetch the web page
        response_1 = requests.get(url_1)

        # Create a BeautifulSoup object
        soup_1 = BeautifulSoup(response_1.text, 'html.parser')

        # Check if the web page contains the desired content
        if 'No results found' not in response_1.text:
            # Capture the screenshot using manufacturer code 1
            screenshot_filename_1 = f'screenshot_{manufacturer_code_1}_{i}_{current_datetime}.png'
            driver.get("data:text/html;charset=utf-8," + str(soup_1))
            driver.save_screenshot(screenshot_filename_1)
        else:
            # Construct the URL using manufacturer code 2
            url_2 = website + manufacturer_code_2

            # Fetch the web page
            response_2 = requests.get(url_2)

            # Create a BeautifulSoup object
            soup_2 = BeautifulSoup(response_2.text, 'html.parser')

            # Capture the screenshot using manufacturer code 2
            screenshot_filename_2 = f'screenshot_{manufacturer_code_2}_{i}_{current_datetime}.png'
            driver.get("data:text/html;charset=utf-8," + str(soup_2))
            driver.save_screenshot(screenshot_filename_2)

# Close the web driver
driver.quit()


