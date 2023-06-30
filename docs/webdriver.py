from bs4 import BeautifulSoup
import requests
import datetime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.service import Service

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