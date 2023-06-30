# Website URL template with placeholders for model numbers
website_url_template = 'https://www.bing.com/shop?q=({model_number})&qs=n&form=SHOPSB&sp=-1&lq=0&pq=spt67m8-01&sc=0-10&sk=&cvid=CEC4A7799DFA4DBF9867A9C06C81D147&ghsh=0&ghacc=0&ghpl='

# Iterate over the rows in the Excel file
for index, row in sku_test_df.iterrows():
    model_number_1 = row['Model Number 1']
    model_number_2 = row['Model Number 2']
    
    # Skip iteration if both model numbers are missing
    if pd.isnull(model_number_1) and pd.isnull(model_number_2):
        continue
    
    # Generate the website URLs by replacing the placeholders with the model numbers
    website_url_1 = website_url_template.replace('{model_number}', str(model_number_1))
    website_url_2 = website_url_template.replace('{model_number}', str(model_number_2))
    
    # Open the websites and take screenshots
    if not pd.isnull(model_number_1):
        driver.get(website_url_1)
        screenshot_filename_1 = f'screenshot_{model_number_1}.png'
        driver.save_screenshot(screenshot_filename_1)
    
    if not pd.isnull(model_number_2):
        driver.get(website_url_2)
        screenshot_filename_2 = f'screenshot_{model_number_2}.png'
        driver.save_screenshot(screenshot_filename_2)

# Close the web driver
driver.quit()






