import pandas as pd
import random

def generate_sales_data():
    produtos = [
        'iPhone 15 Pro', 'iPhone 14', 'Samsung S24 Ultra', 'Samsung A54', 
        'Xiaomi Mi 13', 'Xiaomi Redmi Note 12', 'Motorola Edge 40', 'Motorola Moto G54',
        'Google Pixel 8', 'OnePlus 11'
    ]
    paises = ['Brasil', 'Estados Unidos', 'Canadá', 'Reino Unido', 'Alemanha', 'França', 'Japão', 'Coreia do Sul']
    num_rows = 100
    data = []
    for i in range(num_rows):
        produto = random.choice(produtos)
        garantia = random.choice(['Sim', 'Não'])
        pais = random.choice(paises)
        quantidade = random.randint(1, 5)
        if 'iPhone' in produto or 'S24' in produto or 'Pixel' in produto:
            valor_unitario = round(random.uniform(4000, 9000), 2)
        else:
            valor_unitario = round(random.uniform(800, 3000), 2)
        data.append([produto, garantia, pais, quantidade, valor_unitario])

    df = pd.DataFrame(data, columns=['produto', 'garantia extendida', 'pais', 'quantidade', 'valor unitário'])
    output_path = 'data/vendas_mobile.csv'
    df.to_csv(output_path, index=False)
    print(f"Arquivo criado com sucesso: {output_path}")

if __name__ == "__main__":
    generate_sales_data()
