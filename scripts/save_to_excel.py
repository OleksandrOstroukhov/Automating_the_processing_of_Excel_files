import pandas as pd

def save_to_excel(dataframe, output_path):
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        dataframe.to_excel(writer, sheet_name='Summary', index=False)
