import pandas as pd
from selenium import webdriver
from docx import Document
from docx.shared import Inches
from PIL import Image
import keyboard
import win32gui
import os
import time

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
vendor_col_index_2 = lumber_df.columns.get_loc('Home_Depot')
vendor_col_index_3 = lumber_df.columns.get_loc('Chinook')
vendor_col_index_4 = lumber_df.columns.get_loc('Menards')

# get the column index of the 'Item Number' and 'Description' header
item_col_index = lumber_df.columns.get_loc('Item_#')
desc_col_index = lumber_df.columns.get_loc('Description')

# Iterate over the rows of the excel file
for index, row in lumber_df.iterrows():
    vendor_1 = row[vendor_col_index]
    vendor_2 = row[vendor_col_index_2]
    vendor_3 = row[vendor_col_index_3]
    vendor_4 = row[vendor_col_index_4]

    item_number = row[item_col_index]
    description = str(row[desc_col_index])
    if pd.isnull(item_number):
        break

    vendors = [vendor_1, vendor_2, vendor_3, vendor_4]

    for vendor_url in vendors:
        # check if vendor is not null before opening link
        if pd.isna(vendor_url) or not str(vendor_url).strip():
            continue
        vendor = str(vendors)

        for website in vendors:
            driver.get(vendor_url)

            wait_time = 2
            time.sleep(wait_time)

















