import pandas as pd

def convert():
    try:
        df = pd.read_csv('data/planilha_vendas.csv')
        output_path = 'data/planilha_vendas.xlsx'
        df.to_excel(output_path, index=False)
        print(f"Success! File converted to: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    convert()
