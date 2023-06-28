#sample python code for automation





from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import datetime
import pandas as pd

# Set the path to the ChromeDriver executable
chromedriver_path = '/path/to/chromedriver'

# Set up the Chrome options
chrome_options = webdriver.ChromeOptions()
# Add any desired options, e.g., to run headless:
# chrome_options.add_argument('--headless')

# Initialize the Chrome driver
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# List of target websites
websites = [
    'https://www.website1.com/search?manufacturer=',
    'https://www.website2.com/search?manufacturer=',
    'https://www.website3.com/search?manufacturer='
]

# Read manufacturer codes from Excel file
excel_file_path = 'manufacturer_codes.xlsx'  # Update with your Excel file path
manufacturer_codes_df = pd.read_excel(excel_file_path)

# Get the current date and time
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Loop through the manufacturer codes
for index, row in manufacturer_codes_df.iterrows():
    manufacturer_code = row['Manufacturer Code']

    # Loop through the websites
    for i, website in enumerate(websites):
        # Construct the URL
        url = website + manufacturer_code

        # Fetch the web page
        response = requests.get(url)

        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, 'html.parser')

        # Capture the screenshot
        screenshot_filename = f'screenshot_{manufacturer_code}_{i}_{current_datetime}.png'
        driver.get("data:text/html;charset=utf-8," + str(soup))
        driver.save_screenshot(screenshot_filename)

# Close the web driver
driver.quit()

