import pandas as pd

def combine_sheets(file_path):
    excel_data = pd.ExcelFile(file_path)
    combined_data = pd.DataFrame()

    for sheet in excel_data.sheet_names:
        if sheet != 'Summary':
            sheet_data = pd.read_excel(file_path, sheet_name=sheet)
            combined_data = pd.concat([combined_data, sheet_data], ignore_index=True)

    return combined_data
