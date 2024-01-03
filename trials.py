import pandas as pd
from datetime import datetime



def create_new_csv(input_file_path, output_file_path):
    try:
        # output_file_path = f"cleaned_{publisher_name_file}.csv"
        df = pd.read_excel(input_file_path)

        # Adding a column to dataframe
        df['Accrual campaign name'] = 'dir_list_split[1]'

        # Create the new DataFrame with the required columns
        new_df = df[['Date', 'Publisher', 'Accrual campaign name', 'Concept Name', 'Geo Targeting', 'Impressions', 'Clicks','Spends']]

        # Rename the columns as per the user input
        new_df['Campaign Name'] = 'dir_list_split[0]'
        new_df['Publisher'] = 'dir_list_split[2]'

        # Renaming columns names to main format
        new_df.rename(columns = {'Geo Targeting':'GEO'}, inplace = True)

        # Save the new DataFrame as a CSV file
        new_df.loc[:,['Date', 'Publisher', 'Campaign Name','Accrual campaign name', 'Concept Name', 'GEO', 'Impressions', 'Clicks','Spends']].to_csv(output_file_path, index=False)

        print("New CSV file created successfully.")
    except Exception as e:
        print(f"Error processing the Excel file: {e}")

        

if __name__ == "__main__":
    input_file_path = "June\JUNE\AMAZON FASHION WRS\Beauty\IN_Vogue_GQ_Amazon_June_23.csv"  # Replace this with the actual input Excel/CSV file path
    output_file_path = "cleaned_idiva.csv"  # Replace this with the desired output CSV file path
    create_new_csv(input_file_path, output_file_path)



# Call the function with your input and output file paths
input_file_path = "June\JUNE\AMAZON FASHION WRS\Beauty\IN_Vogue_GQ_Amazon_June_23.csv"
output_file_path = 'cleaned_GQ.csv'
clean_and_convert(input_file_path, output_file_path)

campaign_name = '123'
accrual_campaign_name = '456'
publisher_name = '234'
input_file_path = "June\JUNE\AMAZON FASHION WRS\Beauty\ABeauty WRS_Beauty WRS-XCM_Vogue.csv"
df = pd.read_csv(input_file_path)
output_file_path = f"cleaned_qwe.csv"

# Get the column names
column_names = list(df.columns)
column_names
first_column_name = column_names[0]
first_column_name
date_column_name = column_names[1]

# Find the index to drop rows up to "Line Item"
index_to_drop_to = df[df[first_column_name] == 'Line Item'].index[0]
df_cleaned = df.drop(range(index_to_drop_to))  # Adjust range to include the "Line Item" row

# Reset the index
df_cleaned.reset_index(drop=True, inplace=True)

# Set the second row as the new header
new_header = df_cleaned.iloc[0]
df_cleaned = df_cleaned[:1]
df_cleaned.columns = new_header
df_cleaned

# Find the row index where "Date range" is present
date_range_row_index = df[df[first_column_name] == 'Date range'].index[0]
date_range_value = df.loc[date_range_row_index, date_column_name]

date_range_value

date_parts = date_range_value.split(' - ')
start_date = date_parts[0].strip()
date_object = datetime.strptime(start_date, '%d-%b-%Y')
formatted_date = date_object.strftime('%Y-%m-%d')

# Clean the DataFrame
df_cleaned = df_cleaned.dropna(subset=['Line Item'])
df_cleaned = df_cleaned[df_cleaned['Line Item'] != 'Total']

# Create new columns
df_cleaned['Campaign Name'] = campaign_name
df_cleaned['Publisher'] = publisher_name
df_cleaned['Accrual campaign name'] = accrual_campaign_name
df_cleaned['Date'] = formatted_date
df_cleaned['GEO'] = ''
df_cleaned['Spends'] = ''

# Rename columns
df_cleaned.rename(columns={'Line Item': 'Concept Name', 'Ad server impressions': 'Impressions', 'Ad server clicks': 'Clicks'}, inplace=True)

# Write the cleaned DataFrame to an output CSV file
df_cleaned.loc[:, ['Date', 'Publisher', 'Campaign Name', 'Accrual campaign name', 'Concept Name', 'GEO', 'Impressions', 'Clicks', 'Spends']].to_csv(output_file_path, index=False)

print("New CSV file created successfully.")


# Call the function with your input and output file paths
input_file_path = "June\JUNE\AMAZON FASHION WRS\Beauty\Pinkvilla beauty.xlsx"
output_file_path = 'cleaned_pinkvilla.csv'

campaign_name = '123'
accrual_campaign_name = '456'
publisher_name = '234'
dir_list_split = ['abc','123','pinkvilla','Roadblock']
df = pd.read_excel(input_file_path)

column_names = list(df.columns)
column_names
first_column_name = column_names[0]
first_column_name
date_column_name = column_names[1]

# Find the index to drop rows up to "Line Item"
index_to_drop_to = df[df[first_column_name] == 'Roadblock'].index[0]
df_cleaned = df.drop(range(index_to_drop_to))  # Adjust range to include the "Line Item" row

df_cleaned.reset_index(drop=True, inplace=True)

df_cleaned

new_header = df_cleaned.iloc[0]
df_cleaned = df_cleaned[1:]
df_cleaned.columns = new_header


df_cleaned = df_cleaned[df_cleaned['Roadblock'] != 'Total']

df_cleaned

column_names = list(df_cleaned.columns)
first_column_name_2 = column_names[0]

if 'Roadblock' in dir_list_split:
    df_cleaned['Concept Name'] = 'Roadblock'
else:
    df_cleaned['Concept Name'] = 'Something Else'


df_cleaned.rename(columns={first_column_name_2: 'Date', 'Ad Impressions': 'Impressions'}, inplace=True)

df_cleaned['Campaign Name'] = campaign_name
df_cleaned['Publisher'] = publisher_name
df_cleaned['Accrual campaign name'] = accrual_campaign_name
# df_cleaned['Date'] = formatted_date
df_cleaned['GEO'] = ''
df_cleaned['Spends'] = ''



df_cleaned

df_cleaned[['Date'][0]]

for i in range(len(df_cleaned['Date'])):
    for date in df_cleaned['Date']:
        day_without_suffix = date.split()[0].rstrip("stndrdth")
        parsed_date = datetime.strptime(day_without_suffix + " " + " ".join(date.split()[1:]), "%d %B %Y")
        formatted_date = parsed_date.strftime("%Y-%m-%d")
        df_cleaned[['Date'][i]] = formatted_date

new_df = df_cleaned.loc[:, ['Date', 'Publisher', 'Campaign Name', 'Accrual campaign name', 'Concept Name', 'GEO', 'Impressions', 'Clicks', 'Reach', 'Spends']]

input_file_path = "June\JUNE\AMAZON FASHION WRS\Beauty\ABeauty WRS_Beauty WRS-XCM_Vogue.csv"
# output_file_path = 'cleaned_pinkvilla.csv'

campaign_name = '123'
accrual_campaign_name = '456'
publisher_name = '234'
dir_list_split = ['abc','123','Vogue']
df = pd.read_csv(input_file_path)


# def create_new_csv_format_4(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name):
#     try:
#         output_file_path = f"cleaned_123.csv"

# Get the column names
column_names = list(df.columns)
first_column_name = column_names[0]
date_column_name = column_names[1]

# Find the index to drop rows up to "Line Item"
index_to_drop_to = df[df[first_column_name] == 'Line Item'].index[0]
df_cleaned = df.drop(range(index_to_drop_to))  # Adjust range to include the "Line Item" row

# Reset the index
df_cleaned.reset_index(drop=True)

# Set the second row as the new header
new_header = df_cleaned.iloc[0]
df_cleaned = df_cleaned[1:]
df_cleaned.columns = new_header

df_cleaned.reset_index(drop=True, inplace=True)
df_cleaned

# Find the row index where "Date range" is present
date_range_row_index = df[df[first_column_name] == 'Date range'].index[0]
date_range_value = df.loc[date_range_row_index, date_column_name]

date_parts = date_range_value.split(' - ')
start_date = date_parts[0].strip()
date_object = datetime.strptime(start_date, '%d-%b-%Y')
formatted_date = date_object.strftime('%Y-%m-%d')

# Clean the DataFrame
df_cleaned = df_cleaned.dropna(subset=['Line Item'])
df_cleaned = df_cleaned[df_cleaned['Line Item'] != 'Total']

df_cleaned.reset_index(drop=True, inplace=True)

# Create new columns
df_cleaned['Campaign Name'] = campaign_name
df_cleaned['Publisher'] = publisher_name
df_cleaned['Accrual campaign name'] = accrual_campaign_name
df_cleaned['Date'] = formatted_date
df_cleaned['GEO'] = ''
df_cleaned['Spends'] = ''

# Rename columns
df_cleaned.rename(columns={'Line Item': 'Concept Name', 'Ad server impressions': 'Impressions', 'Ad server clicks': 'Clicks'}, inplace=True)

df_cleaned
okay = df_cleaned['Concept Name'][3].split('_')
okay

print(len(df_cleaned['Concept Name']))

for i in range(len(df_cleaned['Concept Name'])):
    line_split = df_cleaned['Concept Name'][i].split('_')
    print (line_split)
    if 'GQ' or'Vogue' in line_split:
        print('Cool')
    # df_cleaned[['Publisher'][i]] = publisher_name
    else:
        print('Publisher not found')


# Write the cleaned DataFrame to an output CSV file
df_cleaned.loc[:, ['Date', 'Publisher', 'Campaign Name', 'Accrual campaign name', 'Concept Name', 'GEO', 'Impressions', 'Clicks', 'Spends']].to_csv(output_file_path, index=False)

print("New CSV file created successfully.")

    # except Exception as e:
    #     print(f"Error processing the Excel file: {e}")


create_new_csv_format_4(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name)

list1 = ['IN', 'GQ', 'Amazon', 'Interscroller', 'June23']

if 'GQ' in list1:
    print("qwe")


input_file_path = "June\JUNE\AMAZON FASHION WRS\Sale\AMAZON Fashion Report Mediakart June_23.xlsx"
# output_file_path = 'cleaned_pinkvilla.csv'
output_file_path = f"cleaned_1234.csv"

campaign_name = '123'
accrual_campaign_name = '456'
publisher_name = '234'
dir_list_split = ['abc','123','Vogue']
df = pd.read_excel(input_file_path)
df

df = df.dropna(axis = 1 , thresh=1)
# Reset the index
# df.reset_index(drop=True, inplace=True)

column_names = list(df.columns)
first_column_name = column_names[0]

# Find the index to drop rows up to "Line Item"
index_to_drop_to = df[df[first_column_name] == 'Publisher'].index[0]

df = df.drop(range(index_to_drop_to))

# Find the index to drop rows after "Total"
index_to_drop_after = df[df[first_column_name] == 'Total'].index[0]

df = df.loc[:index_to_drop_after-1]

# Reset the index
df.reset_index(drop=True, inplace=True)

# Change the header of the file
new_header = df.iloc[0]
df = df[1:]
df.columns = new_header

# Split the "Line Item Name" column and get the "GEO" value
df['GEO'] = df['Geo Targeting'].apply(get_geo)

# Assigning the column values
df['Accrual campaign name'] = accrual_campaign_name
df['Campaign Name'] = campaign_name
df['Publisher'] = publisher_name

df['Concept Name'] = df['Line Item Name']

# Converting date to format
for i in range(1,len(df['Date'])+1):
    df['Date'][i] = df['Date'][i].date()

# # Reset the index
# df.reset_index(drop=True, inplace=True)       

# Df to CSV
df.loc[:,['Date', 'Publisher', 'Campaign Name','Accrual campaign name', 'Concept Name', 'GEO', 'Impressions', 'Clicks', '25% Views', '50% Views', '75% Views', '100% Views', 'Spends']].to_csv(output_file_path, index=False)
print("New CSV file created successfully.")

# Formatting the date for csv
def formating_date(df, campaign_name, publisher_name):
    try:

        date_formats = ["%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d", "%Y/%m/%d", "%d.%m.%Y", "%Y.%m.%d", "%d-%m-%Y %H:%M:%S", "%d/%m/%Y %H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S", "%d.%m.%Y %H:%M:%S", "%Y.%m.%d %H:%M:%S"]

        for i in range(len(df['Date'])):
            parsed_date = None
            for date_format in date_formats:
                try:
                    date_obj = datetime.strptime(str(df['Date'][i]), date_format)
                    formatted_date = date_obj.strftime("%d-%m-%Y")
                    parsed_date = formatted_date
                    df['Date'][i] = formatted_date
                    print(date_obj)
                    break
                except ValueError:
                    continue
                    # print(f"Error processing the Excel file: {e}")

            if parsed_date is None:
                print(f"Date Format not recognised for {df['Date'][i]} - {campaign_name} - {publisher_name} ")
    
    except Exception as e:
        print(f"error processing the date {e}")

campaign_name = 123
publisher_name = 456

formating_date(df, campaign_name, publisher_name)

input_file_path = "Publisher_done\Done\ABeauty WRS_Beauty WRS-XCM_Dailyhunt.csv"
# output_file_path = 'cleaned_pinkvilla.csv'
output_file_path = f"cleaned_1234.csv{start_date}"

campaign_name = '123'
accrual_campaign_name = '456'
publisher_name = '234'
dir_list_split = ['abc','123','Vogue']
df = pd.read_csv(input_file_path)
df

df = df.dropna(subset = ['Date'])

start_date_time = min(df['Date'])
end_date_time = max(df['Date'])

start_date_time

start_date = start_date_time.datetime.strftime('%d-%m-%Y')


date_formats = ["%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d", "%Y/%m/%d", "%d.%m.%Y", "%Y.%m.%d", "%d-%m-%Y %H:%M:%S", "%d/%m/%Y %H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S", "%d.%m.%Y %H:%M:%S", "%Y.%m.%d %H:%M:%S"]

for i in range(len(df['Date'])):
    parsed_date = None
    for date_format in date_formats:
        try:
            date_obj = datetime.strptime(str(df['Date'][i]), date_format)
            parsed_date = date_obj
            formatted_date = date_obj.strftime("%d-%b-%Y")
            df.at[i, 'Date'] = formatted_date
            # print(formatted_date)
            break
        except ValueError:
            continue
            # print(f"Error processing the Excel file: {e}")

    if parsed_date is None:
        print(f"Date Format not recognised for {df['Date'][i]} - {campaign_name} - {publisher_name} ")

df.dtypes

start_date_time = min(df['Date'])
end_date_time = max(df['Date'])
start_date = start_date_time.strftime('%d-%m-%Y')
end_date = end_date_time.strftime('%d-%m-%Y')

start_date_time
end_date_time


import pandas as pd


input_file_path = "files_combined.csv"
# output_file_path = 'cleaned_pinkvilla.csv'
output_file_path = f"cleaned_1234.csv{start_date}"

campaign_name = '123'
accrual_campaign_name = '456'
publisher_name = '234'
dir_list_split = ['abc','123','Vogue']
df = pd.read_csv(input_file_path)
df

print(df.dtypes)

df['50% Views'] = df['50% Views'].apply(pd.to_numeric)

print(type(df['Impressions'][1]))

print(df['Impressions'][0].isdigit())

if type(int(df['Impressions'][0])) == str:
    print("amazing")


true_count = 0
false_count = 0
for i in range(len(df['Impressions'])):
    value = df['Impressions'][i]
    if value.isdigit() == True:
        true_count = true_count + 1
    elif value.isdigit() == False:
        false_count = false_count + 1
        # print(f'False value-{value}')
    else:
        print(f'value not recognised for{value}')
    
print (f'True Count {true_count}')
print (f'False Count {false_count}')

a = '123,345'

delim = ','

b = int(a.replace(delim,''))
print(type(b))

delim = ','

def column_value_to_int(value):
    try:
        # value = column_name
        delim = ','
        value = str(value)
        if value.isdigit() == True:
            return value
            # value = int(float(value))
        elif value.isdigit() == False:
            value = value.replace(delim,'')
            return value
        else:
            print(f'no delim - {value}')
            return None
    except ValueError as e:
        print(f'problem in - {e}')
    

df['Impressions'] = df['Impressions'].apply(column_value_to_int)

df['Impressions']

int_column_names = ['Impressions','Engagements','Reach','Views', '25% Views', '50% Views', '75% Views', '100% Views', 'Spends']

def apply_column_to_int(df):
    try:
        int_column_names = ['Impressions','Engagements','Reach','Views', '25% Views', '50% Views', '75% Views', '100% Views', 'Spends']

        for column in int_column_names:
            df[column] = df[column].apply(column_value_to_int)
            
        
        return df
    except ValueError as e:
        print(f'problem in - {e}')

apply_column_to_int(df)

import pandas as pd

input_file_path_plan = "output/files_combined.csv"
# output_file_path = 'cleaned_pinkvilla.csv'
output_file_path = f"cleaned_1234.csv"

campaign_name = '123'
accrual_campaign_name = '456'
publisher_name = '234'
dir_list_split = ['abc','123','Vogue']
df = pd.read_csv(input_file_path_plan)
df.columns.to_list()

df = df.drop_duplicates(subset=df.columns.to_list())

df.to_csv(output_file_path, index=False)


df_plan.columns

input_file_path_files = "files_combined.csv"
df_files = pd.read_csv(input_file_path_files)
df_files.columns

df2 = df_files.groupby(['Publisher', 'Campaign Name', 'GEO']).agg({'Impressions': ['sum'], 'Spends': ['sum']})
df2.to_csv('try.csv')

df2.columns

df2 = df2.reset_index()
df2

df2 = df2.droplevel(level = 1, axis = 1)
df2.to 



import pandas as pd
from fuzzywuzzy import fuzz

# Sample data
data1 = {'GEO': ['T4']}
data2 = {'GEO': ['T4 (Delhi NCR, Mumbai + Thane, Bangalore, Hyderabad)']}

# Create DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Define a function to calculate similarity
def similarity_score(str1, str2):
    return fuzz.token_sort_ratio(str1, str2)  # Token sort ratio is a variation of Levenshtein distance

# Apply the similarity function and filter based on a threshold
threshold = 80  # Adjust the threshold as needed
df1['similarity_score'] = df1['GEO'].apply(lambda x: df2['GEO'].apply(lambda y: similarity_score(x, y)).max())
matches = df1[df1['similarity_score'] >= threshold]

# Perform a left join based on the similarity threshold
merged_df = pd.merge(matches, df2, on='similarity_score', suffixes=('', '_matched'), how='left')

# Print the merged DataFrame
print(merged_df)

matches


# Check the similarity score
full_name = "RO T10 (Chennai, Kolkata, Pune, Jaipur, Ahmedabad, Lucknow)"
name = "T10"

print(f"Similarity score: {fuzz.token_set_ratio(name, full_name)}")

df = pd.read_csv("Other_stuff\Book1.csv")

for i in range(len(df['Plan'])):
    print(f"Similarity score for {i}: {fuzz.ratio(df['Final Report'][i], df['Plan'][i])}___{df['Final Report'][i]}--{df['Plan'][i]}")

import pandas as pd

input_file_path_files = "Publisher_done\Done\Cheggout.xlsx"
df = pd.read_excel(input_file_path_files)

df

df['Clicks'] = df['Clicks'].apply(pd.to_numeric)


import pandas as pd

input_file_path_plan = "static/files/Amazon WRS Campaign (Nov-Dec 2023)_Sale_Truecaller-Impact.xlsx"
# output_file_path = 'cleaned_pinkvilla.csv'
output_file_path = f"cleaned_1234.csv"

campaign_name = 'Build Up-Phase 1'
accrual_campaign_name = 'Jupiter Specials'
publisher_name = 'DSP'
dir_list_split = ['abc','123','Vogue']
df = pd.read_excel(input_file_path_plan)
df

df.columns

column_names = list(df.columns)
first_column_name = column_names[0]

index_to_drop_to = df[df[first_column_name] == 'Date'].index[0]

df = df.drop(range(index_to_drop_to))

# Reset the index
df.reset_index(drop=True, inplace=True)

# Change the header of the file
new_header = df.iloc[0]
df = df[1:]
df.columns = new_header.tolist()

# Reset the index
df.reset_index(drop=True, inplace=True)


import re
import pandas as pd
from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer, AutoModel
import os

re.split(' - | _ |- |_',a)

# Given string
geo = pd.read_csv('main_input_files\Geo.csv')
geo_data = str(tuple(geo['Geos'].tolist()))


line_item_name = "Amazon_Fresh SVD_IN_E-Commerce_Agency_Non PG_1st Jan-7th Jan_2024_Surat"


def get_geo(line_item_name):
    parts = re.split('_| - ', str(line_item_name))
    print(parts)
    for part in parts:
        if part.strip().lower() == 'in':
            continue
        elif part.strip().lower() in geo_data.strip().lower():
            print(part)
            return part
    return None

get_geo(line_item_name)

'Indore' in geo_data
geo_data



