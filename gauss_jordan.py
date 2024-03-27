import pandas as pd
import numpy as np

number_columns = int(input('Escriba el número de incógnitas de las ecuaciones: '))
number_equation = number_columns
number_columns +=1
array = np.zeros((number_equation, number_columns))
print(array)
matriz_df = pd.DataFrame(array,columns=[f"x{i+1}" for i in range(number_columns)],index=[f"ec{i+1}" for i in range(number_equation)])
matriz_df.columns = matriz_df.columns[:-1].tolist() + ["res"]

print('range(number_equation)')
print(range(number_equation))
for row_index in range(number_equation):
    for column_index in range(number_columns):
        value = float(input(f'Ingrese el valor de [{row_index},{column_index}]: '))
        matriz_df.iloc[row_index, column_index] = value

def transform_pivot_to_1(matriz, pivot):
    print(f'F{pivot} => F{pivot} / {matriz.iloc[pivot,pivot]} ---------------')
    if (matriz.iloc[pivot,pivot] == 0): return (matriz,False)
    matriz.iloc[pivot] = matriz.iloc[pivot] / matriz.iloc[pivot,pivot]
    return (matriz,True)

def number_sign(number):
    # if number < 0:
    #     return 1
    return -1

def transform_to_0(matriz, pivot, row_index):
    if pivot == row_index: return (matriz,True)
    print(f'F{row_index} => F{row_index} +  (F{pivot} * {number_sign(matriz.iloc[row_index,pivot])} * {matriz.iloc[row_index,pivot]}) ---------------')
    matriz.iloc[row_index] = matriz.iloc[row_index] + (((matriz.iloc[pivot]) * number_sign(matriz.iloc[row_index,pivot])) * (matriz.iloc[row_index,pivot]))
    return (matriz,True)

def gauss_jordan(matriz, pivot):
    print(f'pivot => {pivot}--{range(matriz.shape[0]-1)}')
    pivote_transform = False
    isValid = True
    for row_count in range(matriz.shape[0]):
        print(f'row_count => {row_count}')
        if not pivote_transform:
            (matriz,isValid) = transform_pivot_to_1(matriz,pivot)
            if not isValid:
                return (matriz,False)
            print(matriz)
            pivote_transform = True
        (matriz,isValid) = transform_to_0(matriz,pivot,row_count)
        print(matriz)
    return (matriz,True)

print(matriz_df)
for count_column in range(matriz_df.columns.size-1):
    (matriz_df,isValid) = gauss_jordan(matriz_df, count_column)
    if not isValid:
        print('La matriz no tiene solución')
        break
# print(matriz_df)