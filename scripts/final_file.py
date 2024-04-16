import os
import csv
import pandas as pd
import time
from datetime import datetime
from dateutil import parser

path = "final_cleaned_files/"
dir_list = os.listdir(path)
geo_data = pd.read_csv('main_input_files/Geo.csv')
geo_target_data = pd.read_csv('main_input_files/Geo_Target.csv')


def missing_column_names(df):
    default_columns = list(df.columns)
    view_columns = ['Date','Publisher','Campaign Name','Accrual Campaign Name','Device','Line Item Name','Concept Name','Geo','Metro/Non Metro', 'Platform', 'Section', 'Ad Unit', 'Targeting', 'Deal Type','Impressions','Clicks','Engagements','Reach','Views', '25% Views', '50% Views', '75% Views', '100% Views', 'Spends']

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
    
    df = df.loc[:,['Date','Publisher','Campaign Name','Accrual Campaign Name','Device','Concept Name','Geo','Metro/Non Metro', 'Platform', 'Section', 'Ad Unit', 'Targeting', 'Deal Type','Impressions','Clicks','Engagements','Reach','Views', '25% Views', '50% Views', '75% Views', '100% Views', 'Spends']]

def column_value_to_int(value):
    try:
        # value = column_name
        delim = ','
        value = str(value)
        if value.isdigit() == True:
            return int(value)
            # value = int(float(value))
        elif value.isdigit() == False:
            value = value.replace(delim,'')
            return value
        else:
            print(f'no delim - {value}')
            return None
    except ValueError as e:
        print(f'problem in - {e}')

def apply_column_to_int(df):
    try:
        int_column_names = ['Impressions','Clicks','Engagements','Reach','Views', '25% Views', '50% Views', '75% Views', '100% Views', 'Spends']

        for column in int_column_names:
            df[column] = df[column].apply(column_value_to_int)
        
        return df
    except ValueError as e:
        print(f'problem in - {e}')

def extract_geo(df):
    try:
        df['Geo_Target'] = ''
        df['Geo'] = df['Geo'].astype(str)
        geo_data['Geos'] = geo_data['Geos'].astype(str)
        geo_target_data['Geo_Target'] = geo_target_data['Geo_Target'].astype(str)
        for i in range(len(df)):
            for j in range(len(geo_data)):
                if df['Geo'][i] in geo_data['Geos'][j]:
                    df['Geo'][i] = geo_data['Geos'][j]
                else:
                    pass
            for k in range(len(geo_target_data)):
                if df['Geo_Target'][i] in str(geo_target_data['Geo_Target'][k]):
                    df['Geo_Target'][i] = str(geo_target_data['Geo_Target'][k])
                else:
                    pass
        return df
    except ValueError as e:
        print(f'problem in - {e}')

def final_file_output():
    try:
        for files in dir_list:
            # Reading the files
            df = pd.read_csv(f"{path}{files}")
            # print(f"file name is:-{files}")

            df.columns = df.columns.str.title()
            
            # Calling the column function
            missing_column_names(df)

            # Writing again to CSV files
            output_file_path = f"{path}{files}"
            df.to_csv(output_file_path, index=False)

        # Creating the single file    
        df_concat = pd.concat([pd.read_csv(f'{path}{f}') for f in dir_list ], ignore_index=True)

        # Drop blank date values
        df_concat = df_concat.dropna(subset = ['Date'])

        # Renaming Campaign name to Phase
        df_concat = df_concat.rename(columns={'Campaign Name':'Identifiers'})

        # Extracting Geo
        # df_concat = extract_geo(df_concat)
        # df_concat['Geo_City'] = df_concat['Geo'].str.extract(r"(\w+)(?=\sT\d+)")
        # df_concat['Geo_Target'] = df_concat['Geo'].str.extract(r"(\w+\s\w+\sT\d+\s-\s\w+)$")
        # df_concat['Geo'].astype(str)

        if df_concat['Accrual Campaign Name'][1] == 'AMZ EA Thematic H1 24':
            # Extract Geo_Target
            df_concat['Geo_Target'] = df_concat['Geo'].str.extract(r'(\bT\d+\s*-\s*\w+\b)')
            # Extract Geo_city
            df_concat['Geo_City'] = df_concat['Geo'].str.extract(r'(AP/TL|Delhi|Goa|Gujarat|Karnataka|Kerala|Maharashtra|ROI|Tamilnadu|UP|Uttaranchal|West Bengal)') 
        else:
            df_concat['Geo_Target'] = ''
            df_concat['Geo_City'] = ''

        # Apply int colum function
        apply_column_to_int(df_concat)

        df_concat = df_concat.loc[:,['Date','Publisher','Identifiers','Accrual Campaign Name','Device','Line Item Name','Concept Name','Geo','Geo_City','Geo_Target','Metro/Non Metro', 'Platform', 'Section', 'Ad Unit', 'Targeting', 'Deal Type','Impressions','Clicks','Engagements','Reach','Views', '25% Views', '50% Views', '75% Views', '100% Views', 'Spends']]
        
        # Writing df_concat to single file
        df_concat.to_csv('output/files_combined.csv', index=False)
        print('Final file created')

        # # Deleting the files
        # for files in dir_list:
        #     os.remove(f'{path}{files}')
        #     print(f'files deleted-{path}{files}')
        

    except Exception as e:
        print(f"Error processing the Excel file: {e}")

if __name__ == "__main__":
    final_file_output()



  