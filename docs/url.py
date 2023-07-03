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
edgedriver_dir = r'C:\Users\ankur.chadha\desktop\msedgedriver'  

# Set up the Edge options
edge_options = webdriver.EdgeOptions()

# Add the Edge driver directory to the PATH environment variable
os.environ["PATH"] += os.pathsep + edgedriver_dir

# Initialize the Edge driver
driver = webdriver.Edge(options=edge_options)

# Read model numbers from Excel file
excel_file_path = r'C:\Users\ankur.chadha\Desktop\Automation\skutest.xlsx'  
sku_test_df = pd.read_excel(excel_file_path)

# Website URL template with a placeholder for the model number
website_url_template = 'https://www.bing.com/shop?q={model_number}&FORM=SHOPTB'

'https://www.bing.com/shop?q={model_number}&FORM=SHOPTB'

# Get the column index of the 'Model Number' header
model_number_col_index = sku_test_df.columns.get_loc('Model Number')

# Iterate over the model numbers
for index, row in sku_test_df.iterrows():
    model_number = row[model_number_col_index]
    
    # Skip iteration if the model number is missing
    if pd.isnull(model_number):
        continue
    
    # Generate the website URL by replacing the placeholder with the model number
    website_url = website_url_template.replace('{model_number}', str(model_number))
    
    # Open the website and take a screenshot
    driver.get(website_url)
    screenshot_filename = f'screenshot_{model_number}.png'
    driver.save_screenshot(screenshot_filename)

# Close the web driver
driver.quit()





