# Loop through the websites
for i, website_url_template in enumerate(website_url_template):

        # Fetch the web page
        response_1 = requests.get(website_url_1)

        # Create a BeautifulSoup object
        soup_1 = BeautifulSoup(response_1.text, 'html.parser')

    # Capture the screenshot using manufacturer code 1
        screenshot_filename_1 = f'{item_number_col_index}_{item_description_col_index}.png'
        driver.get(website_url_1)
        driver.save_screenshot(screenshot_filename_1)

else:

    # Construct the URL using manufacturer code 2
    website_url_2 = website_url_template + str(model_number_2)

    # Fetch the web page
    response_2 = requests.get(website_url_2)

    # Create a BeautifulSoup object
    soup_2 = BeautifulSoup(response_2.text, 'html.parser')


    # Capture the screenshot using manufacturer code 2
    screenshot_filename_2 = f'screenshot_{model_number_2}_{i}_{current_datetime}.png'
    driver.get("data:text/html;charset=utf-8," + str(soup_2))
    driver.save_screenshot(screenshot_filename_2)

driver.quit()
