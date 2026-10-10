import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    print(f"Numpy version: {np.__version__}")

    # 1. Criação de Arrays e Atributos
    d = [1, 2, 3, 4, 5, 6]
    arr = np.array(d)
    print("\nArray simples:", arr)
    print("Dtype:", arr.dtype)
    print("Shape:", np.shape(arr))
    print("Size:", np.size(arr))

    # Arrays Multidimensionais
    d2 = [[1, 3, 5, 7], [3, 55, 6, 90]]
    arr1 = np.array(d2)
    print("\nArray 2D:\n", arr1)
    print("Shape 2D:", np.shape(arr1))

    # Indexação e Slicing
    print("\nElemento [1,2]:", arr1[1, 2])
    print("Primeira linha:", arr1[0, :])
    print("Slice [1, 1:3]:", arr1[1, 1:3])

    # Arrays Especiais e Aleatórios
    print("\nArray vazio (int32):", np.empty(6, dtype='int32'))
    print("Array aleatório (randint 0-57):\n", np.random.randint(0, 57, size=(3, 3)))
    print("Array aleatório (rand 3x3):\n", np.random.rand(3, 3))

    # Operações Matemáticas e Vetorização
    arr3 = arr1 * 2
    print("\nArray multiplicado por 2:\n", arr3)

    subarr = np.subtract(arr3, arr1)
    print("Subtração (arr3 - arr1):\n", subarr)

    # Estatísticas e Acumuladores
    print("\nMédia do arr1:", arr1.mean())
    print("Soma acumulada (axis=1):\n", arr1.cumsum(axis=1))
    print("Soma acumulada (axis=0):\n", arr1.cumsum(axis=0))

    # Manipulação de Shape (Reshape e Transposição)
    arr4 = np.arange(8)
    arr5 = arr4.reshape(4, 2)
    print("\nReshape (4,2):\n", arr5)

    arr6 = arr5.reshape(2, 4)
    arr7 = arr6.T
    print("\nTransposta da matriz:\n", arr7)

    # Concatenar e Split
    arr9 = np.concatenate((arr5, arr7), axis=1)
    print("\nConcatenado (axis=1):\n", arr9)

    split_arr = np.split(arr7, 2)
    print("\nSplit do arr7 em 2 partes:\n", split_arr)

if __name__ == "__main__":
    main()
