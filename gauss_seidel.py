import pandas as pd
import numpy as np

iteraciones = int(input('Escriba el número de iteraciones: '))

number_columns = 0
# while number_columns < 2:
#     number_columns = int(input('Escriba el número de incógnitas de las ecuaciones: '))
#     if number_columns < 2:
#         print("No válido, intente de nuevo")
array = np.array([
    [10,2,-1,0,26],
    [1,20,-2,3,-15],
    [-2,20,30,0,53],
    [1,2,3,20,47]
    ])
number_columns = array.shape[1]
number_equation = number_columns-1
_RES_COLUMN = "res"
matriz_df = pd.DataFrame(array,columns=[f"x{i+1}" for i in range(number_columns)],index=[f"ec{i+1}" for i in range(number_equation)])
matriz_df.columns = matriz_df.columns[:-1].tolist() + [_RES_COLUMN]
lista_diagonal = []
for row_index in range(number_equation):
    for column_index in range(number_columns):
        if column_index == row_index:
            lista_diagonal.append(matriz_df.iloc[row_index, column_index])   
            matriz_df.iloc[row_index, column_index] = 0
lista_independientes = matriz_df.iloc[:,-1].to_list()
punto_matriz = [1,2,3,4]
convergence = False
print(matriz_df)
def gauss_seidel(matriz, punto, diagonal, independientes):
    for row in range(matriz.shape[0]):
        res1 = 0
        for col in range(matriz.shape[1]):
            if (col < matriz.shape[1]-1):
                # print ("RES1 = ",matriz.iloc[row,col]," * ",punto[col])
                res1 += matriz.iloc[row,col] * punto[col]
        punto[row] = (independientes[row] - res1)/diagonal[row]
        # print(" PUNTO = (",independientes[row] ,"-", res1,")/",diagonal[row]," = ",punto[row])
    return punto

row_count = 0
cuenta = 0
while cuenta < iteraciones:
    punto = gauss_seidel(matriz_df, punto_matriz, lista_diagonal, lista_independientes)
    print('PUNTO => ', punto)
    row_count += 1
    cuenta += 1