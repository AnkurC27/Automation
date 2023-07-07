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


# Read manufacturer codes from Excel file
excel_file_path = r'C:\Users\ankur.chadha\Desktop\Automation\skutest.xlsx'  
sku_test_df = pd.read_excel(excel_file_path)

# Get the column index of the 'Item Number' header
item_number_col_index = sku_test_df.columns.get_loc('Item Number')
for index, row in sku_test_df.iterrows():
    item_number = row[item_number_col_index]
    folder_name = str(int(item_number/100)*100)
    directory = folder_name

try:
    os.mkdir(directory)
    print(f"Directory '{directory}' created.")
except Exception as e:
    print(f"Could not create directory. Error: {str(e)}")
