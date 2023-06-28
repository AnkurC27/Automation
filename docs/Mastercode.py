from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd

#set the path to the EdgeDriver executable
edgedriver_path = 'desktop/Python Files/msedgedriver'

#set up the Edge options
edge_options = webdriver.EdgeOptions()

#Initialize the Edge driver
driver = webdriver.Edge(executable_path=edgedriver_path, options=edge_options)

#list of target websites
websites = 




