import os
import csv
import pandas as pd
import time
from datetime import datetime
import re

# github trial

pd.options.mode.chained_assignment = None

# Defining the path where files are stored
path = "static/files/"
# path = 'Other_stuff/Jupiter Campaign Reports/Jupiter Specials - Akshat/Publisher Reports/'
dir_list = os.listdir(path)

# dir_list
# Reading Geo CSV
geo = pd.read_csv('main_input_files\Geo.csv')
geo_data = str(tuple(geo['Geos'].tolist()))

# Reading publishers CSV
publisher1 = pd.read_csv('main_input_files\publisher_format_1.csv')
publisher_format_1 = tuple(publisher1['Publishers'].tolist())

# Reading publishers CSV
publisher2 = pd.read_csv('main_input_files\publisher_format_2.csv')
publisher_format_2 = tuple(publisher2['Publishers'].tolist())

# Reading publishers CSV
publisher3 = pd.read_csv('main_input_files\publisher_format_3.csv')
publisher_format_3 = tuple(publisher3['Publishers'].tolist())

# Reading publishers CSV
publisher4 = pd.read_csv('main_input_files\publisher_format_4.csv')
publisher_format_4 = tuple(publisher4['Publishers'].tolist())

# Reading publishers CSV
publisher5 = pd.read_csv('main_input_files\publisher_format_5.csv')
publisher_format_5 = tuple(publisher5['Publishers'].tolist())

# Reading publishers CSV
publisher6 = pd.read_csv('main_input_files\publisher_format_6.csv')
publisher_format_6 = tuple(publisher6['Publishers'].tolist())

# Reading publishers CSV
publisher7 = pd.read_csv('main_input_files\publisher_format_7.csv')
publisher_format_7 = tuple(publisher7['Publishers'].tolist())

# Reading publishers CSV
publisher8 = pd.read_csv('main_input_files\publisher_format_8.csv')
publisher_format_8 = tuple(publisher8['Publishers'].tolist())

# Reading publishers CSV
publisher9 = pd.read_csv('main_input_files\publisher_format_9.csv')
publisher_format_9 = tuple(publisher9['Publishers'].tolist())

# Reading publishers CSV
publisher10 = pd.read_csv('main_input_files\publisher_format_10.csv')
publisher_format_10 = tuple(publisher10['Publishers'].tolist())

# Reading publishers CSV
publisher11 = pd.read_csv('main_input_files\publisher_format_11.csv')
publisher_format_11 = tuple(publisher11['Publishers'].tolist())

# Reading publishers CSV
publisher12 = pd.read_csv('main_input_files\publisher_format_12.csv')
publisher_format_12 = tuple(publisher12['Publishers'].tolist())

# Reading publishers CSV
publisher13 = pd.read_csv('main_input_files\publisher_format_13.csv')
publisher_format_13 = tuple(publisher13['Publishers'].tolist())



# Retrieve Geo name from geo file
def get_geo(line_item_name):
    parts = re.split('_| - ', str(line_item_name))
    for part in parts:
        if part.strip().lower() in geo_data.strip().lower():
            return part
    return None

# Formatting the date for csv
def formating_date(df, campaign_name, publisher_name):
    try:
        # print(df)
        date_formats = ["%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d", "%Y/%m/%d", "%d.%m.%Y", "%Y.%m.%d", "%d-%m-%Y %H:%M:%S", "%d/%m/%Y %H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S", "%d.%m.%Y %H:%M:%S", "%Y.%m.%d %H:%M:%S","%d-%m-%y","%d.%m.%y"]
        # print(range(len(df['Date'])))

        for i in range(len(df['Date'])):
            parsed_date = None
            for date_format in date_formats:
                try:
                    # print(df['Date'][i])
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
    
        try:
            df['Date'] = pd.to_datetime(df['Date'], format="%d-%b-%Y")
            # print(df.dtypes)
            start_date_time = None
            end_date_time = None
            start_date_time = min(df['Date']).date()
            end_date_time = max(df['Date']).date()
            return start_date_time, end_date_time
            # start_date = start_date_time.strftime('%d-%m-%Y')
            # end_date = end_date_time.strftime('%d-%m-%Y')
        except ValueError as e:
            print(f'Error finding min and max date {e}')

    except Exception as e:
        print(f"error processing the date {e}")


# Retrieve a publisher from publisher_format_1 list based on given publisher_name
def get_publisher_1(publisher_name):
    for publisher in publisher_format_1:
        if publisher.strip().lower() == publisher_name.strip().lower():
            global publisher_name_file
            publisher_name_file = publisher
            return publisher
    return None

# Retrieve a publisher from publisher_format_2 list based on given publisher_name
def get_publisher_2(publisher_name):
    for publisher in publisher_format_2:
        if publisher.strip().lower() == publisher_name.strip().lower():
            global publisher_name_file_2
            publisher_name_file_2 = publisher
            return publisher
    return None

# Retrieve a publisher from publisher_format_3 list based on given publisher_name
def get_publisher_3(publisher_name):
    for publisher in publisher_format_3:
        if publisher.strip().lower() == publisher_name.strip().lower():
            global publisher_name_file_3
            publisher_name_file_3 = publisher
            return publisher
    return None

# Retrieve a publisher from publisher_format_4 list based on given publisher_name
def get_publisher_4(publisher_name):
    for publisher in publisher_format_4:
        if publisher.strip().lower() == publisher_name.strip().lower():
            global publisher_name_file_4
            publisher_name_file_4 = publisher
            return publisher
    return None
    
# Retrieve a publisher from publisher_format_5 list based on given publisher_name
def get_publisher_5(publisher_name):
    for publisher in publisher_format_5:
        if publisher.strip().lower() == publisher_name.strip().lower():
            global publisher_name_file_5
            publisher_name_file_5 = publisher
            return publisher
    return None

# Retrieve a publisher from publisher_format_6 list based on given publisher_name
def get_publisher_6(publisher_name):
    for publisher in publisher_format_6:
        if publisher.strip().lower() == publisher_name.strip().lower():
            global publisher_name_file_6
            publisher_name_file_6 = publisher
            return publisher
    return None

# Retrieve a publisher from publisher_format_6 list based on given publisher_name
def get_publisher_7(publisher_name):
    for publisher in publisher_format_7:
        if publisher.strip().lower() == publisher_name.strip().lower():
            global publisher_name_file_7
            publisher_name_file_7 = publisher
            return publisher
    return None

# Retrieve a publisher from publisher_format_6 list based on given publisher_name
def get_publisher_8(publisher_name):
    for publisher in publisher_format_8:
        if publisher.strip().lower() == publisher_name.strip().lower():
            global publisher_name_file_8
            publisher_name_file_8 = publisher
            return publisher
    return None

# Retrieve a publisher from publisher_format_9 list based on given publisher_name
def get_publisher_9(publisher_name):
    for publisher in publisher_format_9:
        if publisher.strip().lower() == publisher_name.strip().lower():
            global publisher_name_file_9
            publisher_name_file_9 = publisher
            return publisher
    return None

# Retrieve a publisher from publisher_format_9 list based on given publisher_name
def get_publisher_10(publisher_name):
    for publisher in publisher_format_10:
        if publisher.strip().lower() == publisher_name.strip().lower():
            global publisher_name_file_10
            publisher_name_file_10 = publisher
            return publisher
    return None

# Retrieve a publisher from publisher_format_9 list based on given publisher_name
def get_publisher_11(publisher_name):
    for publisher in publisher_format_11:
        if publisher.strip().lower() == publisher_name.strip().lower():
            global publisher_name_file_11
            publisher_name_file_11 = publisher
            return publisher
    return None

# Retrieve a publisher from publisher_format_9 list based on given publisher_name
def get_publisher_12(publisher_name):
    for publisher in publisher_format_12:
        if publisher.strip().lower() == publisher_name.strip().lower():
            global publisher_name_file_12
            publisher_name_file_12 = publisher
            return publisher
    return None

# Retrieve a publisher from publisher_format_13 list based on given publisher_name
def get_publisher_13(publisher_name):
    for publisher in publisher_format_13:
        if publisher.strip().lower() == publisher_name.strip().lower():
            global publisher_name_file_13
            publisher_name_file_13 = publisher
            return publisher
    return None

def create_new_csv_format_1(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name):
    try:
        
        # df = pd.read_excel(input_file_path)

        default_columns = list(df.columns)

        # Removing NA and total rows
        df = df[df[default_columns[0]] != 'Total']

        if 'Line item' in df.columns:
            # Split the "Line Item Name" column and get the "GEO" value
            df['GEO'] = df['Line item'].apply(get_geo)
        else:
            df['GEO'] = ''
            df['Line item'] = ''

        # Adding a column to dataframe
        df['Accrual campaign name'] = accrual_campaign_name
        df['Campaign Name'] = campaign_name
        df['Publisher'] = publisher_name
        # Renaming columns names to main format
        if publisher_name.strip().title() == 'Abp' or 'Ei Samay':
            df.rename(columns = {'Concept':'Concept Name', 'Ad server impressions':'Impressions', 'Ad server clicks':'Clicks'}, inplace = True)
        else:
            df.rename(columns = {'Creative':'Concept Name', 'Ad server impressions':'Impressions', 'Ad server clicks':'Clicks'}, inplace = True)

        # Formatting the date
        start_date_time, end_date_time = formating_date(df, campaign_name, publisher_name)

        # start_date_time = min(df['Date'])
        # end_date_time = max(df['Date'])
        # start_date = start_date_time.strftime('%d-%m-%Y')
        # end_date = end_date_time.strftime('%d-%m-%Y')

        output_file_path = f"final_cleaned_files/cleaned_{accrual_campaign_name}_{publisher_name_file}_{start_date_time}_{end_date_time}.csv"  # Replace this with the desired output CSV file path

        # Save the new DataFrame as a CSV file
        df.loc[:,['Date', 'Publisher', 'Campaign Name','Accrual campaign name', 'Concept Name', 'GEO', 'Impressions', 'Clicks']].to_csv(output_file_path, index=False)

        print("New CSV file created successfully.")
    except Exception as e:
        print(f"Error processing the Excel file: {e}")



def create_new_csv_format_2(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name):
    try:

        # Adding a column to dataframe
        df['Accrual campaign name'] = accrual_campaign_name

        # # Create the new DataFrame with the required columns
        # df = df[['Date', 'Publisher', 'Accrual campaign name', 'Concept', 'Geos', 'Impressions', 'Sum Of Clicks',]]

        # Rename the columns as per the user input
        df['Campaign Name'] = campaign_name
        df['Publisher'] = publisher_name

        df['GEO'] = df['Ad Name'].apply(get_geo)

        # Renaming columns names to main format
        df.rename(columns = {'Ad Name':'Concept Name'}, inplace = True)

        # Formatting the date
        start_date_time, end_date_time = formating_date(df, campaign_name, publisher_name)

        # start_date_time = min(df['Date'])
        # end_date_time = max(df['Date'])
        # start_date = start_date_time.strftime('%d-%m-%Y')
        # end_date = end_date_time.strftime('%d-%m-%Y')

        output_file_path = f"final_cleaned_files/cleaned_{accrual_campaign_name}_{publisher_name_file_2}_{start_date_time}_{end_date_time}.csv"

        # Save the new DataFrame as a CSV file
        df.loc[:,['Date', 'Publisher', 'Campaign Name','Accrual campaign name', 'Concept Name', 'GEO', 'Impressions', 'Clicks',]].to_csv(output_file_path, index=False)

        print("New CSV file created successfully.")
    except Exception as e:
        print(f"Error processing the Excel file: {e}")


def create_new_csv_format_3(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name):
    try:        
        
        # print(publisher_name_file_3)added
        default_columns = list(df.columns)
        view_columns = ['Publisher','Geo Targeting','Concept Name','Views', '25% Views', '50% Views', '75% Views', '100% Views','Spends']

        # check views column 
        for heads in view_columns:
            head_existence = False
            if heads in default_columns:
                head_existence = True
                if head_existence == True:
                    pass
            elif head_existence == False:
                df[heads] = ''  
            else:
                print("fu")


        # Removing NA and total rows
        df = df[df['Publisher'] != 'Total']
        df = df.dropna(how='all')
        df = df.dropna(subset = ['Date'])

         # Reset the index
        df.reset_index(drop=True, inplace=True)

        # Adding a column to dataframe
        df['Accrual campaign name'] = accrual_campaign_name
        df['Engagements'] = ''

        # # Create the new DataFrame with the required columns
        # df = df[['Date', 'Publisher', 'Accrual campaign name', 'Concept Name', 'Geo Targeting', 'Impressions', 'Engagements', 'Clicks', 'Views','25% Views', '50% Views', '75% Views', '100% Views','Spends']]

        # For jupiter sale - Mcanvas
        if publisher_name.strip().title() == 'Paytm':
            df['Concept Name'] = df['Concept']
            df['Geo Targeting'] = df['Geo']

        # For jupiter sale - Glance
        if publisher_name.strip().title() == 'Glance':
            df['Concept Name'] = df['Concept']

        # Rename the columns as per the user input
        df['Campaign Name'] = campaign_name
        df['Publisher'] = publisher_name

        # # Renaming columns names to main format
        # df = df.rename(columns = {'Geo Targeting':'GEO'}, inplace = True)

        # Split the "Line Item Name" column and get the "GEO" value
        # df['GEO'] = df['Geo Targeting'].apply(get_geo)

        # Renaming columns names to main format for Jupiter beauty - Mcanvas
        if 'Targeting' in df.columns:
            df['GEO'] = df['Targeting'] + ',' + df['Geo Targeting']
        else:
            df['GEO'] = df['Geo Targeting']

        # Renaming columns names to main format for Jupiter beauty - Hipi
        if publisher_name.strip().title() == 'Hipi':
            df['GEO'] = df['Line Item Name']

        # Formatting the date
        start_date_time, end_date_time = formating_date(df, campaign_name, publisher_name)

        # start_date_time = min(df['Date'])
        # end_date_time = max(df['Date'])
        # start_date = start_date_time.strftime('%d-%m-%Y')
        # end_date = end_date_time.strftime('%d-%m-%Y')

        output_file_path = f"final_cleaned_files/cleaned_{accrual_campaign_name}_{publisher_name_file_3}_{start_date_time}_{end_date_time}.csv"

        # Save the new DataFrame as a CSV file
        df.loc[:,['Date', 'Publisher', 'Campaign Name','Accrual campaign name', 'Concept Name', 'GEO', 'Impressions', 'Engagements', 'Clicks', 'Views', '25% Views', '50% Views', '75% Views', '100% Views', 'Spends']].to_csv(output_file_path, index=False)

        print("New CSV file created successfully.")
    except Exception as e:
        print(f"Error processing the Excel file: {e}")


def create_new_csv_format_4(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name):
    try:
        # Get the column names
        column_names = list(df.columns)
        first_column_name = column_names[0]
        date_column_name = column_names[1]

        # Find the index to drop rows up to "Line Item"
        index_to_drop_to = df[df[first_column_name] == 'Line Item'].index[0]
        df_cleaned = df.drop(range(index_to_drop_to))  # Adjust range to include the "Line Item" row

        # Reset the index
        df_cleaned.reset_index(drop=True, inplace=True)

        # Set the second row as the new header
        new_header = df_cleaned.iloc[0]
        df_cleaned = df_cleaned[1:]
        df_cleaned.columns = new_header.tolist()

        # Reset the index
        df_cleaned.reset_index(drop=True, inplace=True)

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

        # Create new columns
        df_cleaned['Campaign Name'] = campaign_name
        df_cleaned['Publisher'] = publisher_name
        df_cleaned['Accrual campaign name'] = accrual_campaign_name
        df_cleaned['Date'] = formatted_date
        df_cleaned['GEO'] = ''
        df_cleaned['25% Views'] = ''
        df_cleaned['50% Views'] = ''
        df_cleaned['Spends'] = ''

        # Rename columns
        df_cleaned.rename(columns={'Line Item': 'Concept Name', 'Ad server impressions': 'Impressions', 'Ad server clicks': 'Clicks'}, inplace=True)

        # Reset the index
        df_cleaned.reset_index(drop=True, inplace=True)

        # Doing this for Vogue/GQ
        for i in range(len(df_cleaned['Concept Name'])):
            line_split = df_cleaned['Concept Name'][i].split('_')
            # print (line_split)
            for publisher in publisher_format_4:
                if publisher in line_split:
                    df_cleaned['Publisher'][i] = publisher
                else:
                    print("no publisher in format 4")


        # Formatting the date
        start_date_time, end_date_time = formating_date(df_cleaned, campaign_name, publisher_name)

        # start_date_time = min(df['Date'])
        # end_date_time = max(df['Date'])
        # start_date = start_date_time.strftime('%d-%m-%Y')
        # end_date = end_date_time.strftime('%d-%m-%Y')

        output_file_path = f"final_cleaned_files/cleaned_{accrual_campaign_name}_{publisher_name_file_4}_{start_date_time}_{end_date_time}.csv"
           
        # Write the cleaned DataFrame to an output CSV file
        df_cleaned.loc[:, ['Date', 'Publisher', 'Campaign Name', 'Accrual campaign name', 'Concept Name', 'GEO', 'Impressions', 'Clicks','Spends']].to_csv(output_file_path, index=False)
        
        print("New CSV file created successfully.")

    except Exception as e:
        print(f"Error processing the Excel file: {e}")


def create_new_csv_format_5(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name):
    try:        
        
        column_names = list(df.columns)
        first_column_name = column_names[0]
        date_column_name = column_names[1]

        # Find the index to drop rows up to "Line Item"
        index_to_drop_to = df[df[first_column_name] == 'Roadblock'].index[0]
        df_cleaned = df.drop(range(index_to_drop_to))  # Adjust range to include the "Line Item" row

        # Reset the index
        df_cleaned.reset_index(drop=True, inplace=True)

        # Change the header of the file
        new_header = df_cleaned.iloc[0]
        df_cleaned = df_cleaned[1:]
        df_cleaned.columns = new_header.tolist()

        # Reset the index
        df_cleaned.reset_index(drop=True, inplace=True)

        # Removing the total row
        df_cleaned = df_cleaned[df_cleaned['Roadblock'] != 'Total']

        column_names = list(df_cleaned.columns)
        first_column_name_2 = column_names[0]

        if 'Roadblock' in publisher_name:
            df_cleaned['Concept Name'] = 'Roadblock'
        else:
            df_cleaned['Concept Name'] = 'Something Else'

        
        df_cleaned.rename(columns={first_column_name_2: 'Date', 'Ad Impressions': 'Impressions'}, inplace=True)

        df_cleaned['Campaign Name'] = campaign_name
        df_cleaned['Publisher'] = publisher_name
        df_cleaned['Accrual campaign name'] = accrual_campaign_name
        df_cleaned['GEO'] = ''
        df_cleaned['Spends'] = ''

        for i in range(len(df_cleaned['Date'])):
            for date in df_cleaned['Date']:
                day_without_suffix = date.split()[0].rstrip("stndrdth")
                parsed_date = datetime.strptime(day_without_suffix + " " + " ".join(date.split()[1:]), "%d %B %Y")
                formatted_date = parsed_date.strftime("%Y-%m-%d")
                df_cleaned[['Date'][i]] = formatted_date
        
        # Formatting the date
        start_date_time, end_date_time = formating_date(df_cleaned, campaign_name, publisher_name)

        # start_date_time = min(df['Date'])
        # end_date_time = max(df['Date'])
        # start_date = start_date_time.strftime('%d-%m-%Y')
        # end_date = end_date_time.strftime('%d-%m-%Y')

        output_file_path = f"final_cleaned_files/cleaned_{accrual_campaign_name}_{publisher_name_file_5}_{start_date_time}_{end_date_time}.csv"

        df_cleaned.loc[:, ['Date', 'Publisher', 'Campaign Name', 'Accrual campaign name', 'Concept Name', 'GEO', 'Impressions', 'Clicks', 'Reach', 'Spends']].to_csv(output_file_path, index=False)

        print("New CSV file created successfully.")

    except Exception as e:
        print(f"Error processing the Excel file: {e}")

def create_new_csv_format_6(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name):
    try:        
        # Split the "Line Item Name" column and get the "GEO" value
        df['GEO'] = df['Line item'].apply(get_geo)

        # Assigning the column values
        df['Accrual campaign name'] = accrual_campaign_name
        df['Campaign Name'] = campaign_name
        df['Publisher'] = publisher_name

        # Renaming specific columns in the DataFrame
        df.rename(columns = {'Creative':'Concept Name','Ad server impressions':'Impressions', 'Ad server clicks':'Clicks'}, inplace = True)
        
        # Formatting the date
        start_date_time, end_date_time = formating_date(df, campaign_name, publisher_name)

        # start_date_time = min(df['Date'])
        # end_date_time = max(df['Date'])
        # start_date = start_date_time.strftime('%d-%m-%Y')
        # end_date = end_date_time.strftime('%d-%m-%Y')

        output_file_path = f"final_cleaned_files/cleaned_{accrual_campaign_name}_{publisher_name_file_6}_{start_date_time}_{end_date_time}.csv"

        df.loc[:, ['Date', 'Publisher', 'Campaign Name', 'Accrual campaign name', 'Concept Name', 'GEO', 'Impressions', 'Clicks']].to_csv(output_file_path, index=False)

        print("New CSV file created successfully.")

    except Exception as e:
        print(f"Error processing the Excel file: {e}")


def create_new_csv_format_7(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name):
    try:        
        # Removing the total column
        df = df[df.iloc[:,0] != 'Total']

        # Reset the index
        df.reset_index(drop=True, inplace=True)

        # Assigning the column values
        df['Accrual campaign name'] = accrual_campaign_name
        df['Campaign Name'] = campaign_name
        df['Publisher'] = publisher_name
        df['GEO'] = ''

        # Renaming the columns
        df.rename(columns = {'Order':'Concept Name','Ad server impressions':'Impressions', 'Ad server clicks':'Clicks'}, inplace = True)

        # Entering missing columns names
        default_columns = list(df.columns)
        view_columns = ['Engagements', 'Views', '25% Views', '50% Views', '75% Views', '100% Views', 'Spends']

        # check views column 
        for heads in view_columns:
            head_existence = False
            if heads in default_columns:
                head_existence = True
                if head_existence == True:
                    pass
            elif head_existence == False:
                df[heads] = ''  
            else:
                print("fu")

        # Converting date to format
        for i in range(len(df['Date'])):
            df['Date'][i] = df['Date'][i].date()

        # Formatting the date
        start_date_time, end_date_time = formating_date(df, campaign_name, publisher_name)

        # start_date_time = min(df['Date'])
        # end_date_time = max(df['Date'])
        # start_date = start_date_time.strftime('%d-%m-%Y')
        # end_date = end_date_time.strftime('%d-%m-%Y')

        output_file_path = f"final_cleaned_files/cleaned_{accrual_campaign_name}_{publisher_name_file_7}_{start_date_time}_{end_date_time}.csv"
        
        # Df to CSV
        df.loc[:,['Date', 'Publisher', 'Campaign Name','Accrual campaign name', 'Concept Name', 'GEO', 'Impressions', 'Engagements', 'Clicks', 'Views', '25% Views', '50% Views', '75% Views', '100% Views', 'Spends']].to_csv(output_file_path, index=False)
        print("New CSV file created successfully.")

    except Exception as e:
        print(f"Error processing the Excel file: {e}")


def create_new_csv_format_8(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name):
    try:                
        df = df.dropna(axis = 1 , thresh=1)

        column_names = list(df.columns)
        first_column_name = column_names[0]

        if publisher_name == 'Airtel':
            # Find the index to drop rows up to "Line Item"
            index_to_drop_to = df[df[first_column_name] == 'Date'].index[0]
        else:
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
        df.columns = new_header.tolist()

        # Reset the index
        df.reset_index(drop=True, inplace=True)

        if 'Geo Targeting' in df.columns:
            # Split the "Line Item Name" column and get the "GEO" value
            df['GEO'] = df['Geo Targeting'].apply(get_geo)
        else:
            df['GEO'] = ''

        # Assigning the column values
        df['Accrual campaign name'] = accrual_campaign_name
        df['Campaign Name'] = campaign_name
        df['Publisher'] = publisher_name

        if 'Line Item Name' in df.columns:
            df['Concept Name'] = df['Line Item Name']
        else:
            df['Concept Name'] = ''

        # # Converting date to format
        # for i in range(len(df['Date'])):
        #     df['Date'][i] = df['Date'][i].date()

        # # Reset the index
        # df.reset_index(drop=True, inplace=True)
    
        # Formatting the date
        start_date_time, end_date_time = formating_date(df, campaign_name, publisher_name)

        # start_date_time = min(df['Date'])
        # end_date_time = max(df['Date'])
        # start_date = start_date_time.strftime('%d-%m-%Y')
        # end_date = end_date_time.strftime('%d-%m-%Y')

        # print(publisher_name_file_3)added
        default_columns = list(df.columns)
        view_columns = ['Geo Targeting','Concept Name','Views', '25% Views', '50% Views', '75% Views', '100% Views']

        # check views column 
        for heads in view_columns:
            head_existence = False
            if heads in default_columns:
                head_existence = True
                if head_existence == True:
                    pass
            elif head_existence == False:
                df[heads] = ''  
            else:
                print("fu")

        output_file_path = f"final_cleaned_files/cleaned_{accrual_campaign_name}_{publisher_name_file_8}_{start_date_time}_{end_date_time}.csv"

        # Df to CSV
        df.loc[:,['Date', 'Publisher', 'Campaign Name','Accrual campaign name', 'Concept Name', 'GEO', 'Impressions', 'Clicks', '25% Views', '50% Views', '75% Views', '100% Views', 'Spends']].to_csv(output_file_path, index=False)
        print("New CSV file created successfully.")        

    except Exception as e:
        print(f"Error processing the Excel file: {e}")

def create_new_csv_format_9(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name):
    try:                
        # Assigning the column values
        df['Accrual campaign name'] = accrual_campaign_name
        df['Campaign Name'] = campaign_name
        df['Publisher'] = publisher_name
    
        # Formatting the date
        start_date_time, end_date_time = formating_date(df, campaign_name, publisher_name)

        # Renaming specific columns in the DataFrame
        # df.rename(columns = {'Geo':'GEO','clicks':'Clicks', 'views':'Views'}, inplace = True)

        output_file_path = f"final_cleaned_files/cleaned_{accrual_campaign_name}_{publisher_name_file_9}_{start_date_time}_{end_date_time}.csv"

        # Df to CSV
        df.to_csv(output_file_path, index=False)
        print("New CSV file created successfully.")  

    except Exception as e:
        print(f"Error processing the Excel file: {e}")

def create_new_csv_format_10(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name):
    try:                
        # Assigning the column values
        df['Accrual campaign name'] = accrual_campaign_name
        df['Campaign Name'] = campaign_name
        df['Publisher'] = publisher_name
        # df['Brand'] = ''
        df['Device'] = ''

        # Fetching device values from Line Item
        for i in range(len(df)):
            line_item_split = df['Line Item'][i].split('-')
            df['Device'][i] = line_item_split[1].strip()

        # Renaming the columns
        df.rename(columns = {'Link clicks':'Clicks','Video plays at 100%':'Views','Amount spent (INR)':'Spends','Geo Targeting':'GEO'}, inplace = True)
   
        # Formatting the date
        start_date_time, end_date_time = formating_date(df, campaign_name, publisher_name)

        # Assigning output file path
        output_file_path = f"final_cleaned_files/cleaned_{accrual_campaign_name}_{publisher_name_file_10}_{start_date_time}_{end_date_time}.csv"

        # Df to CSV
        df.loc[:,['Date', 'Publisher','Accrual campaign name', 'Campaign Name','Device', 'GEO', 'Impressions', 'Clicks', 'Views', 'Spends']].to_csv(output_file_path, index=False)
        
        print("New CSV file created successfully.")  

    except Exception as e:
        print(f"Error processing the Excel file: {e}")

def create_new_csv_format_11(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name):
    try:
        # Dropping extra rows after final row
        df = df.dropna(subset = ['Line Item'])

        # Assigning the column values
        df['Accrual campaign name'] = accrual_campaign_name
        df['Campaign Name'] = campaign_name
        df['Publisher'] = publisher_name
        # df['Brand'] = ''
        df['Device'] = ''

        # Fetching device values from Line Item
        for i in range(len(df)):
            line_item_split = df['Line Item'][i].split('_')
            df['Device'][i] = line_item_split[1].strip()

        # # Renaming the columns
        # df.rename(columns = {'Link clicks':'Clicks','Video plays at 100%':'Views','Amount spent (INR)':'Spends','Geo Targeting':'GEO'}, inplace = True)
   
        # Formatting the date
        start_date_time, end_date_time = formating_date(df, campaign_name, publisher_name)

        # Assigning output file path
        output_file_path = f"final_cleaned_files/cleaned_{accrual_campaign_name}_{publisher_name_file_11}_{start_date_time}_{end_date_time}.csv"

        # Df to CSV
        df.loc[:,['Date', 'Publisher','Accrual campaign name', 'Campaign Name','Device', 'Impressions', 'Clicks']].to_csv(output_file_path, index=False)

        print("New CSV file created successfully.")  

    except Exception as e:
        print(f"Error processing the Excel file: {e}")


# Only Created for Jupiter Beauty
def create_new_csv_format_12(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name):
    try:
        
        df = df.dropna(subset = ['Creative'])

        df['Accrual campaign name'] = accrual_campaign_name
        df['Campaign Name'] = campaign_name
        df['Publisher'] = publisher_name
        df['Targeting'] = ''

        if publisher_name.strip().title() == 'Dsp2':
            df['Concept Name'] = df['Creative']
            df['Spends'] = ''
            # for i in range(len(df)):
            #     line_item_split = str(df['Line Item'][i]).split('_')
            #     df['Targeting'][i] = line_item_split[2].strip()

            df['GEO'] = df['Line Item']

        elif publisher_name.strip().title() == 'Dmp':
            df['Concept Name'] = df['Creative']
            df['GEO'] = ''
            df['Spends'] = df['Revenue (Adv Currency)']
        
        # elif publisher_name == 'Glance':
        else:
            print('not')
            # for i in range(len(df)):
            #     line_item_split = str(df['Line Item Name'][i]).split(' ')
            #     df['Targeting'][i] = line_item_split[2].strip()+' '+line_item_split[3].strip()

            # df['GEO'] = df['Targeting']+','+df['Geo Targeting']

        # Formatting the date
        start_date_time, end_date_time = formating_date(df, campaign_name, publisher_name)

        # Assigning output file path
        output_file_path = f"final_cleaned_files/cleaned_{accrual_campaign_name}_{publisher_name_file_12}_{start_date_time}_{end_date_time}.csv"

        # Df to CSV
        df.loc[:,['Date', 'Publisher','Accrual campaign name', 'Campaign Name','Concept Name','GEO','Impressions', 'Clicks','Spends',]].to_csv(output_file_path, index=False)

        print("New CSV file created successfully.")  

    except Exception as e:
        print(f"Error processing the Excel file: {e}")

def create_new_csv_format_13(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name):
    try:

        df['Accrual campaign name'] = accrual_campaign_name
        df['Campaign Name'] = campaign_name
        df['Publisher'] = publisher_name

        df.rename(columns=
            {"Reporting Starts": "Date", 
            "Ad Variant Name": "Concept Name", 
            "Impressions (SUM)":"Impressions",
            "Facebook Link Clicks (SUM)":"Clicks",
            "Spent in INR (SUM)":"Spends",
            "Facebook Video Plays to 25% (SUM)":"25% Views",
            "Facebook Video Plays to 50% (SUM)":"50% Views",
            "Facebook Video Plays to 75% (SUM)":"75% Views",
            "Facebook Video Plays to 100% (SUM)":"100% Views"}, inplace=True)
        
        df['GEO'] = df['Ad Set Name'].apply(get_geo)

        
        # Formatting the date
        start_date_time, end_date_time = formating_date(df, campaign_name, publisher_name)

        # Assigning output file path
        output_file_path = f"final_cleaned_files/cleaned_{accrual_campaign_name}_{publisher_name_file_13}_{start_date_time}_{end_date_time}.csv"

        # Df to CSV
        df.to_csv(output_file_path, index=False)

        print("New CSV file created successfully.")  

    except Exception as e:
        print(f"Error processing the Excel file: {e}")

def final_operation(dir_list):
    for i in range(len(dir_list)):
        # start_date_time = None
        # end_date_time = None

        excel_file_path = dir_list[i]
        
        if ".xlsx" in excel_file_path: 
            df = pd.read_excel(f"{path}{excel_file_path}")
        elif ".csv" in excel_file_path:
            df = pd.read_csv(f"{path}{excel_file_path}")
        else:
            print("File format recheck")   

        filename_without_extenstion = list(os.path.splitext(dir_list[i]))
        # print (f'Filename without extension - {filename_without_extenstion}')
        
        try:
            dir_list_split = str(filename_without_extenstion[0]).split('_')
            publisher_name = dir_list_split[2]
            campaign_name = dir_list_split[1]
            accrual_campaign_name = dir_list_split[0]
            df.columns = df.columns.str.strip()

            # print(publisher_name)

            print(f"File name - {dir_list_split}")
            if get_publisher_1(publisher_name) is not None:
                print("amazing 1 publisher found")
                create_new_csv_format_1(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name)

            elif get_publisher_2(publisher_name) is not None:
                print("amazing 2 publisher found")
                create_new_csv_format_2(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name)

            elif get_publisher_3(publisher_name) is not None:
                print("amazing 3 publisher found")
                create_new_csv_format_3(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name)

            elif get_publisher_4(publisher_name) is not None:
                print("amazing 4 publisher found")
                create_new_csv_format_4(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name)

            elif get_publisher_5(publisher_name) is not None:
                print("amazing 5 publisher found")
                create_new_csv_format_5(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name)

            elif get_publisher_6(publisher_name) is not None:
                print("amazing 6 publisher found")
                create_new_csv_format_6(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name)

            elif get_publisher_7(publisher_name) is not None:
                print("amazing 7 publisher found")
                create_new_csv_format_7(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name)

            elif get_publisher_8(publisher_name) is not None:
                print("amazing 8 publisher found")
                create_new_csv_format_8(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name)
            
            elif get_publisher_9(publisher_name) is not None:
                print("amazing 9 publisher found")
                create_new_csv_format_9(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name)

            elif get_publisher_10(publisher_name) is not None:
                print("amazing 10 publisher found")
                create_new_csv_format_10(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name)

            elif get_publisher_11(publisher_name) is not None:
                print("amazing 11 publisher found")
                create_new_csv_format_11(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name)
            
            elif get_publisher_12(publisher_name) is not None:
                print("amazing 12 publisher found")
                create_new_csv_format_12(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name)

            elif get_publisher_13(publisher_name) is not None:
                print("amazing 13 publisher found")
                create_new_csv_format_13(df, dir_list_split, campaign_name, accrual_campaign_name, publisher_name)

            else:
                print("failed")
            # df['check'] = dir_list_split[0]

            final_cleaned_files_list = os.listdir("final_cleaned_files/")

            if len(dir_list) == len(final_cleaned_files_list):
                for i in range(10):
                    print(f'Awesome * {len(final_cleaned_files_list)}')
            
        except Exception as e:
            print("errorrrrrrrr")
        # time.sleep(2)

if __name__ == "__main__":
    final_operation(dir_list)


