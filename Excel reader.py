import pandas as pd

# Read manufacturer codes from Excel file
excel_file_path = 'manufacturer_codes.xlsx'  # Update with your Excel file path
manufacturer_codes_df = pd.read_excel(excel_file_path)

# Iterate over the manufacturer codes
for index, row in manufacturer_codes_df.iterrows():
    manufacturer_code_1 = row['Manufacturer Code 1']
    manufacturer_code_2 = row['Manufacturer Code 2']
    
    # Rest of the code to perform scraping or other operations with the manufacturer codes
