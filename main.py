import tabula
import pandas as pd
import glob

# Specify the folder path containing the PDF files
pdf_folder_path = r"C:\Users\Learner_XZHCG221\Budget_Sheet\Statement"

# Get a list of PDF files in the folder
pdf_files = glob.glob(pdf_folder_path + "/*.pdf")

# Initialize an empty list to store DataFrames for each PDF
dfs = []

# Iterate over each PDF file
for pdf_file in pdf_files:
    try:
        # Read tables from the PDF file
        tables = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)

        # Check if any tables were extracted
        if tables:
            # Extract the desired table from the list of tables
            # (You may need to adjust the index based on the structure of your statement)
            table = tables[0]

            # Append the table DataFrame to the list
            dfs.append(table)
    except Exception as e:
        print(f"Error occurred while processing {pdf_file}: {str(e)}")

# Check if any tables were extracted
if dfs:
    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    # Save the combined DataFrame to a CSV file
    combined_df.to_csv('combined_statements.csv', index=False)
else:
    print("No tables found in the PDF files.")

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('combined_statements.csv')

# Find the column containing the date and description
date_desc_column = next((col for col in df.columns if 'DATE' in col.upper()), None)

if date_desc_column:
    # Split the date and description into separate columns
    df[['DATE', 'DESCRIPTION']] = df[date_desc_column].str.split(' ', 1, expand=True)
    
    # Drop the original column
    df.drop(date_desc_column, axis=1, inplace=True)
    
    # Save the updated DataFrame to a new CSV file
    df.to_csv('combined_statements_updated.csv', index=False)
else:
    print("Unable to find the 'DATE DESCRIPTION' column in the CSV file.")

#import tabula
#import pandas as pd
#import glob
#import json

# Specify the folder path containing the PDF files
#pdf_folder_path = r"C:\Users\Learner_XZHCG221\Budget_Sheet\Statement"

# Get a list of PDF files in the folder
#pdf_files = glob.glob(pdf_folder_path + "/*.pdf")

# Initialize an empty list to store DataFrames for each PDF
#dfs = []

# Iterate over each PDF file
#for pdf_file in pdf_files:
#    try:
        # Read tables from the PDF file
#        tables = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)

        # Check if any tables were extracted
#        if tables:
            # Extract the desired table from the list of tables
            # (You may need to adjust the index based on the structure of your statement)
#            table = tables[0]

            # Append the table DataFrame to the list
#            dfs.append(table)
#    except Exception as e:
#        print(f"Error occurred while processing {pdf_file}: {str(e)}")

# Check if any tables were extracted
#if dfs:
    # Concatenate all DataFrames into a single DataFrame
#    combined_df = pd.concat(dfs, ignore_index=True)

    # Convert the combined DataFrame to JSON
 #   json_data = combined_df.to_json(orient='records')

    # Save the JSON data to a file
#    output_file_path = "combined_statements.json"
#    with open(output_file_path, "w") as file:
#        file.write(json_data)

#    print("PDFs converted to JSON successfully.")
#else:
#    print("No tables found in the PDF files.")








