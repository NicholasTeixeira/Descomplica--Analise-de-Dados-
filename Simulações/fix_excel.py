import pandas as pd

try:
    # Read the original CSV
    df = pd.read_csv('data/planilha_vendas.csv')
    
    # Save as a real Excel binary file
    output_path = 'data/planilha_vendas.xlsx'
    df.to_excel(output_path, index=False, engine='openpyxl')
    
    print(f"Success! Real Excel file created at: {output_path}")
except Exception as e:
    print(f"Error: {e}")
