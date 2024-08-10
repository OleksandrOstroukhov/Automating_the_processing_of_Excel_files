from combine_sheets import combine_sheets
from sort_data import sort_data
from save_to_excel import save_to_excel

def main():
    file_path = "data/example_data.xlsx"
    output_path = "data/summary_data.xlsx"

    combined_data = combine_sheets(file_path)
    sorted_data = sort_data(combined_data, 'Date')
    save_to_excel(sorted_data, output_path)

if __name__ == "__main__":
    main()
