from bs4 import BeautifulSoup
import requests
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import os
from PIL import Image, ImageDraw, ImageFont
import time

# Set the path to the EdgeDriver executable
edgedriver_path = r'C:\Users\ankur.chadha\desktop\msedgedriver'

# Set up Edge options
edge_options = webdriver.EdgeOptions()

# Add the Edge driver directory to the PATH environment variable
os.environ["PATH"] += os.pathsep + edgedriver_path

# Initialize the Edge driver
driver = webdriver.Edge(options=edge_options)

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))

# Maximize the browser window
driver.maximize_window()

# Read manufacturer codes from Excel file
excel_file_path = r'C:\Users\ankur.chadha\Desktop\Automation\skutest.xlsx'
sku_test_df = pd.read_excel(excel_file_path)

# List of websites
websites = ['https://www.homedepot.com/s/{model_number}?NCNI-5',
            'https://www.whitecap.com/search/?query={model_number}',
            'https://www.acetool.com/searchresults.asp?Search={model_number}&Submit=',
            'https://www.toolnut.com/shop.html?q={model_number}']

# Website Names
website_names = {
    'www.homedepot.com': 'home_depot',
    'www.whitecap.com': 'whitecap',
    'www.acehardware.com': 'acehardware',
    'www.acetool.com': 'acetool',
    'www.toolnut.com': 'toolnut'
}

# Get the column index of the 'Model Number' header
model_number_col_index = sku_test_df.columns.get_loc('Model Number 1')
model_number_col_index_2 = sku_test_df.columns.get_loc('Model Number 2')

# Get the column index of the 'Item Number' header
item_number_col_index = sku_test_df.columns.get_loc('Item Number')
item_desc_col_index = sku_test_df.columns.get_loc('Item Description')

def add_watermark(screenshot_filename):
    img = Image.open(screenshot_filename)
    draw = ImageDraw.Draw(img)
    text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    position = (10, 10)
    font = ImageFont.truetype("C:\\Windows\\Fonts\\arial.ttf", 30)
    color = "black" 

    # Get image and text dimensions
    img_width, img_height = img.size
    text_width, text_height = draw.textsize(text, font=font)

    position = ((img_width - text_width) // 2, 10)

    draw.text(position, text, font=font, fill=color)
    img.save(screenshot_filename)


# Iterate over the rows in the Excel file
for index, row in sku_test_df.iterrows():
    model_number_1 = row[model_number_col_index]
    model_number_2 = row[model_number_col_index_2]

    item_number = row[item_number_col_index]
    if pd.isnull(item_number):
        break

    folder_name = str(int(item_number/100)*100)

    if not os.path.exists(folder_name):
        try:
            os.mkdir(folder_name)
            print(f"Directory '{folder_name}' created.")
        except Exception as e:
            print(f"Could not create the directory. Error{str(e)}")

    for model_number in [model_number_1, model_number_2]:
        # Check if model number is not null before opening websites and taking screenshots
        if not model_number or model_number.isspace():
            continue

        website_wait_times = {
        'https://www.homedepot.com/s/{model_number}?NCNI-5': 5,
        'https://www.whitecap.com/search/?query={model_number}': 10,
        'https://www.acehardware.com/search?query={model_number}': 0,
        'https://www.acetool.com/searchresults.asp?Search={model_number}&Submit=': 0,
        'https://www.toolnut.com/shop.html?q={model_number}': 0
}

        for website in websites:
            website_url = website.format(model_number=model_number)
            driver.get(website_url)
            
            wait_time = website_wait_times.get(website, 2)
            time.sleep(wait_time)

            try:
                driver.switch_to.alert.accept()
            except NoAlertPresentException:
                pass

            item_desc = str(row[item_desc_col_index])
            website_name = website.split("//")[-1].split("/")[0]

            custom_website_name = website_names.get(website_name, website_name)

            item_desc = str(row[item_desc_col_index]).replace('\'', '_').replace('\"', '_')

            # Take a screenshot
            screenshot_filename = f'{folder_name}/{row["Item Number"]}_{item_desc}_{custom_website_name}_{index}.png'
            driver.save_screenshot(screenshot_filename)
            add_watermark(screenshot_filename)
            driver.delete_all_cookies()  

# Close the web driver
driver.quit()

