 # Loop through the websites
for i, website in enumerate(websites):
        # Construct the URL using manufacturer code 1
        url_1 = website + str(model_number_1)

        # Fetch the web page
        response_1 = requests.get(url_1)

        # Create a BeautifulSoup object
        soup_1 = BeautifulSoup(response_1.text, 'html.parser')

        # Check if the web page contains the desired content
        if 'No results found' not in response_1.text:
            # Capture the screenshot using manufacturer code 1
            screenshot_filename_1 = f'screenshot_{model_number_1}_{i}_{current_datetime}.png'
            driver.get("data:text/html;charset=utf-8," + str(soup_1))

            #wait for the desired element or condition to be met
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))

            driver.save_screenshot(screenshot_filename_1)

        else:
            # Construct the URL using manufacturer code 2
            url_2 = website + str(model_number_2)

            # Fetch the web page
            response_2 = requests.get(url_2)

            # Create a BeautifulSoup object
            soup_2 = BeautifulSoup(response_2.text, 'html.parser')

            # Capture the screenshot using manufacturer code 2
            screenshot_filename_2 = f'screenshot_{model_number_2}_{i}_{current_datetime}.png'
            driver.get("data:text/html;charset=utf-8," + str(soup_2))

            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))

            driver.save_screenshot(screenshot_filename_2)