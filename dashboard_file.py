import os
import csv
import pandas as pd
import time
from datetime import datetime
from dateutil import parser

final_file_input = "output/files_combined.csv"
campaign_details_input = "main_input_files\campaign_details.csv"
dashboard_output_file_path = "output/dashboard_file.xlsx"


def dashboard_file():
    try:
        # Load the final file and campaign details CSV data
        df_final_file = pd.read_csv(final_file_input)
        df_campaign_detail = pd.read_csv(campaign_details_input)

        # Convert Date column from dd-mm-yyyy to dd/mm/yyyy
        df_final_file['Date'] = pd.to_datetime(df_final_file['Date']).dt.strftime('%d-%m-%Y')

        # Convert campaign names to lowercase for case-insensitive merge
        df_final_file['Accrual Campaign Name'] = df_final_file['Accrual Campaign Name'].str.lower()
        df_campaign_detail['Accrual Campaign Name'] = df_campaign_detail['Accrual Campaign Name'].str.lower()

        # Merge the DataFrames on 'Accrual campaign name'
        df_merged = pd.merge(df_final_file, df_campaign_detail, how='left', on='Accrual Campaign Name', left_index=False, right_index=False)

        # Convert 'tacs_id' to uppercase and 'Accrual campaign name' to title case
        df_merged['tacs_id'] = df_merged['tacs_id'].str.upper()
        df_merged['Accrual Campaign Name'] = df_merged['Accrual Campaign Name'].str.title()

        # Create 'Campaign name' by combining 'tacs_id' and 'Accrual campaign name'
        df_merged['Campaign Name'] = df_merged['tacs_id'].astype(str) + "_" + df_merged['Accrual Campaign Name']

        # Change GEO column to GEO Targeting
        df_merged = df_merged.rename(columns={'Geo': 'Geo Targeting', 'Impressions':'Delivered Impressions', 'Clicks':'Delivered Clicks', 'Views':'Delivered Views', 'Spends':'Delivered Spends'})

        # Adding Planned Columns
        df_merged['Planned Impressions'] = 0
        df_merged['Planned Clicks'] = 0
        df_merged['Planned Views'] = 0
        df_merged['Planned Spends'] = 0

        # If geo is blank, then fill it with 'Pan India'abs
        df_merged['Geo Targeting'] = df_merged['Geo Targeting'].fillna('Pan India')

        # Initialize 'Brand', 'Line Item Name' columns
        df_merged['Brand'] = df_merged['Identifiers']
        df_merged['Line Item Name'] = df_merged['Publisher'] + "_" + df_merged['Accrual Campaign Name'] + "_" + df_merged['Geo Targeting']

        # Drop unnecessary columns
        df_merged = df_merged.drop(['Identifiers', 'Accrual Campaign Name', 'Engagements', 'Reach', 'tacs_id'], axis=1)

        # Deleting duplicates
        df_merged = df_merged.drop_duplicates(subset=df_merged.columns.to_list())

        # Write selected columns to CSV for dashboard output
        df_merged.loc[:,['POD', 'Campaign Name', 'Date', 'Publisher', 'Brand', 'Line Item Name', 'Concept Name', 'Geo Targeting','Planned Impressions' ,'Delivered Impressions', 'Planned Clicks','Delivered Clicks', 'Planned Views','Delivered Views', '25% Views', '50% Views', '75% Views', '100% Views', 'Planned Spends','Delivered Spends']].to_excel(dashboard_output_file_path, index=False)

        print('Congrats! Dashboard file created')
    except Exception as e:
        print(f'Error in dashboard file as {e}')


if __name__ == "__main__":
    dashboard_file()

# def date_format(df):
#     for date in df['Date']:
#         try:
