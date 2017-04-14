#! python3
"""
excel2csv.py - saves copies of .xlsx documents in current working directory as .csv files in ./csv
"""

import os
import csv
import openpyxl

os.makedirs('csv', exist_ok=True)

# loop through each .xlsx file
for filename in os.listdir('.'):
    if not filename.endswith('.xlsx'):
        continue  # skip non-excel files
    wb = openpyxl.load_workbook(filename)
    list_of_sheets = wb.get_sheet_names()

    # loop through each sheet
    for sheetname in list_of_sheets:
        # loop: read rows into list of rows
        sheetData = []
        ws = wb.get_sheet_by_name(sheetname)
        for row in ws.iter_rows():
            sheetData.append([cell.value for cell in row])

        # create csv output file
        csvFilename = '{}_{}.csv'.format(filename.rsplit('.')[0], sheetname)
        output_file = open(os.path.join('csv', csvFilename), 'w', newline='')
        csvWriter = csv.writer(output_file)

        # loop: write rows into CSV
        for row in sheetData:
            csvWriter.writerow(row)

        output_file.close()

print('Done')
