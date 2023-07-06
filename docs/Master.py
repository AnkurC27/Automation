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
from PIL import Image, ImageDraw, ImageFont


# Set the path to the EdgeDriver executable
edgedriver_path = r'C:\Users\ankur.chadha\desktop\msedgedriver'  

#set up edge options
edge_options = webdriver.EdgeOptions()

# Add the Edge driver directory to the PATH environment variable
os.environ["PATH"] += os.pathsep + edgedriver_path

# Initialize the Edge driver
driver = webdriver.Edge(options=edge_options)

# Maximize the browser window
driver.maximize_window()

# Read manufacturer codes from Excel file
excel_file_path = r'C:\Users\ankur.chadha\Desktop\Automation\skutest.xlsx'  
sku_test_df = pd.read_excel(excel_file_path)

# Website URL template with a placeholder for the model number
website_url_template = 'https://www.bing.com/shop?q={model_number}&FORM=SHOPTB'

# Get the column index of the 'Model Number' header
model_number_col_index = sku_test_df.columns.get_loc('Model Number 1')
model_number_col_index_2 = sku_test_df.columns.get_loc('Model Number 2')

# Get the column index of the 'Item Number' header
item_number_col_index = sku_test_df.columns.get_loc('Item Number')

# Get the column index of the 'Model Number' header
item_description_col_index = sku_test_df.columns.get_loc('Item Description')

# Iterate over the rows in the Excel file
for index, row in sku_test_df.iterrows():
    model_number_1 = row[model_number_col_index]
    model_number_2 = row[model_number_col_index_2]

    print(f'Processing row{index}: model_number_1={model_number_1}, model_number_2={model_number_2}')
    
    # Skip iteration if both model numbers are missing
    if pd.isnull(model_number_1) and pd.isnull(model_number_2):
        continue
    
    # Check if model number 1 is not null before taking screenshot
    if pd.notnull(model_number_1):
        # Generate the website URLs by replacing the placeholders with the model numbers
        website_url_1 = website_url_template.replace('{model_number}', str(model_number_1))

        # Capture the screenshot using manufacturer code 1
        driver.get(website_url_1)
        screenshot_filename_1 = f'screenshot_{row[item_number_col_index]}_{row[item_description_col_index]}.png'
        driver.save_screenshot(screenshot_filename_1)

        # Add Watermark to screenshot
        img = Image.open(screenshot_filename_1)
        draw = ImageDraw.Draw(img)
        text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        position = (10, 10)
        font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 15)
        draw.text(position, text, font=font)
        img.save(screenshot_filename_1)

    # Check if model number 2 is not null before taking screenshot
    if pd.notnull(model_number_2):
        # Construct the URL using manufacturer code 2
        website_url_2 = website_url_template.replace('{model_number}', str(model_number_2))
        
        # Fetch the web page
        response_2 = requests.get(website_url_2)

        # Create a BeautifulSoup object
        soup_2 = BeautifulSoup(response_2.text, 'html.parser')

        # Capture the screenshot using manufacturer code 2
        driver.get(website_url_2)
        screenshot_filename_2 = f'screenshot_{model_number_2}.png'
        driver.save_screenshot(screenshot_filename_2)

         # Add Watermark to screenshot
        img = Image.open(screenshot_filename_2)
        draw = ImageDraw.Draw(img)
        text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        position = (10, 10)
        font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 15)
        draw.text(position, text, font=font)
        img.save(screenshot_filename_2)

driver.quit()

