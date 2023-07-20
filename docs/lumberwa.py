import pandas as pd
from selenium import webdriver
from docx import Document
from docx.shared import Inches
from PIL import Image
import io
import requests 
import os

# read the links from the excel file
excel_file_path = r'C:\Users\ankur.chadha\Desktop\Automation\linkswa.xlsx'
lumber_df = pd.read_excel(excel_file_path)

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

# get the column index of the 'Item Number' header
item_col_index = lumber_df.columns.get_loc('Item_#')







