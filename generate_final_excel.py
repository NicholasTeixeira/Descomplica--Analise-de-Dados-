import pandas as pd
import random

def generate():
    produtos = [
        'iPhone 15 Pro', 'iPhone 14', 'Samsung S24 Ultra', 'Samsung A54', 
        'Xiaomi Mi 13', 'Xiaomi Redmi Note 12', 'Motorola Edge 40', 'Motorola Moto G54',
        'Google Pixel 8', 'OnePlus 11'
    ]
    paises = ['Brasil', 'Estados Unidos', 'Canadá', 'Reino Unido', 'Alemanha', 'França', 'Japão', 'Coreia do Sul']
    
    data = []
    for i in range(100):
        produto = random.choice(produtos)
        garantia = random.choice(['Sim', 'Não'])
        pais = random.choice(paises)
        quantidade = random.randint(1, 5)
        if any(x in produto for x in ['iPhone', 'S24', 'Pixel']):
            valor_unitario = round(random.uniform(4000, 9000), 2)
        else:
            valor_unitario = round(random.uniform(800, 3000), 2)
        data.append([produto, garantia, pais, quantidade, valor_unitario])

    df = pd.DataFrame(data, columns=['produto', 'garantia extendida', 'pais', 'quantidade', 'valor unitário'])
    
    # Save directly to Excel using openpyxl engine
    output_path = 'data/planilha_vendas.xlsx'
    df.to_excel(output_path, index=False, engine='openpyxl')
    print(f"Success! File created: {output_path}")

if __name__ == "__main__":
    generate()
