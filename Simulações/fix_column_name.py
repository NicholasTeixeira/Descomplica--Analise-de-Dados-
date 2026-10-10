import pandas as pd

try:
    # Read the existing excel file
    df = pd.read_excel('data/planilha_vendas.xlsx', engine='openpyxl')
    
    # Rename the column
    df = df.rename(columns={'valor unitário': 'valorunitario'})
    
    # Save it back to excel
    output_path = 'data/planilha_vendas.xlsx'
    df.to_excel(output_path, index=False, engine='openpyxl')
    print(f"Success! Column renamed and file saved: {output_path}")
except Exception as e:
    print(f"Error: {e}")
