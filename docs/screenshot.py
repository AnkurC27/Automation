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
os.environ["PATH"] += os.pathsep + edgedriver_dir
driver = webdriver.Edge(options=edge_options)
driver.maximize_window()

excel_file_path = r'C:\Users\ankur.chadha\Desktop\Automation\skutest.xlsx'  
sku_test_df = pd.read_excel(excel_file_path)

# List of websites
websites = ['https://www.homedepot.com/s/{model_number}?NCNI-5', 
            'https://www.whitecap.com/search/?query={model_number}', 
            'https://www.acehardware.com/search?query={model_number}', 
            'https://www.acetool.com/searchresults.asp?Search={model_number}&Submit=', 
            'https://www.toolnut.com/shop.html?q={model_number}']

model_number_col_index = sku_test_df.columns.get_loc('Model Number 1')
model_number_col_index_2 = sku_test_df.columns.get_loc('Model Number 2')

# Get the column index of the 'Item Number' header
item_number_col_index = sku_test_df.columns.get_loc('Item Number')

# Iterate over the rows in the Excel file
for index, row in sku_test_df.iterrows():
    model_number_1 = row[model_number_col_index]
    model_number_2 = row[model_number_col_index_2]
    item_number = row[item_number_col_index]
    folder_name = str(int(item_number/100)*100)

    if not os.path.exists(folder_name):
        try:
            os.mkdir(folder_name)
            print(f"Directory '{folder_name}' created.")
        except Exception as e:
            print(f"Could not create the directory. Error{str(e)}")
        
        

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