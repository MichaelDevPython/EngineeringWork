import tabula
import pandas as pd

hostname = "michael"
pdf_file_path = f"/home/{hostname}/SIWB/TEST_XLSX/inf-s1.pdf"
excel_file_path = f"/home/{hostname}/SIWB/TEST_XLSX/plik.xlsx"

def pdf_to_excel(pdf_file_path, excel_file_path):
    # Read PDF file
    tables = tabula.read_pdf(pdf_file_path, pages='all')

    # Write each table to a separate sheet in the Excel file
    with pd.ExcelWriter(excel_file_path) as writer:
        for i, table in enumerate(tables):
            # Rename the 'Unnamed: 0' column to 'Godzina'
            table = table.rename(columns={'Unnamed: 0': 'Godzina'})

            # Write the table to the Excel file
            table.to_excel(writer, sheet_name=f'Sheet{i+1}', index=False)

# Correct usage of the function with actual file paths
pdf_to_excel(pdf_file_path, excel_file_path)
