import pandas as pd
from selenium import webdriver
from docx import Document
from docx.shared import Inches
from PIL import Image
import keyboard
import win32gui
import os
import time
import datetime
from urllib.parse import urlparse

# load the excel file
excel_file_path = r'C:\Users\ankur.chadha\Desktop\Automation\linkswa.xlsx'
lumber_df = pd.read_excel(excel_file_path)

# set up selenium with edge
edgedriver_path = r'C:\Users\ankur.chadha\desktop\msedgedriver'
os.environ["PATH"] += os.pathsep + edgedriver_path
edge_options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=edge_options)
driver.maximize_window()

# get the column index of the 'Vendor' header
vendor_col_index = lumber_df.columns.get_loc('Dunn')
vendor_col_index_2 = lumber_df.columns.get_loc('HomeDepot')
vendor_col_index_3 = lumber_df.columns.get_loc('Chinook')
vendor_col_index_4 = lumber_df.columns.get_loc('Menards')

# get the column index of the 'Item Number' and 'Description' header
item_col_index = lumber_df.columns.get_loc('Item#')
desc_col_index = lumber_df.columns.get_loc('Description')

# Iterate over the rows of the excel file
for index, row in lumber_df.iterrows():
    vendor_1 = row[vendor_col_index]
    vendor_2 = row[vendor_col_index_2]
    vendor_3 = row[vendor_col_index_3]
    vendor_4 = row[vendor_col_index_4]

    item_number = str(row[item_col_index])
    description = str(row[desc_col_index])
    if pd.isnull(item_number):
        break

    
    vendors = [vendor_1, vendor_2, vendor_3, vendor_4]
    vendor_names = ['Dunn', 'HomeDepot', 'Chinook', 'Menards']

    # create a folder with the date to store screenshots
    date_str = datetime.datetime.now().strftime("%m%d%Y")
    folder_name = 'lumberwa_' + date_str

    if not os.path.exists(folder_name):
        try:
            os.mkdir(folder_name)
            print(f"Directory '{folder_name}' created.")
        except Exception as e:
            print(f"Could not create directory. Error: {str(e)}")

    for vendor_url, vendor_name in zip(vendors, vendor_names):
        # check if vendor is not null before opening link
        if pd.isna(vendor_url) or not str(vendor_url).strip():
            continue

        driver.get(vendor_url)
        wait_time = 2
        time.sleep(wait_time)

        description = str(row[desc_col_index]).replace('\'', '_').replace('\"', '_').replace('-', ' ').replace('/', '_')

        #Take a screenshot
        screenshot_filename = f'{folder_name}/{description}_{vendor_name}.png'
        driver.save_screenshot(screenshot_filename)
        driver.delete_all_cookies()




















