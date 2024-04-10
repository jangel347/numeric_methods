import pandas as pd
import numpy as np

iteraciones = int(input('Escriba el número de iteraciones: '))

number_columns = 0
# while number_columns < 2:
#     number_columns = int(input('Escriba el número de incógnitas de las ecuaciones: '))
#     if number_columns < 2:
#         print("No válido, intente de nuevo")
array = np.array([
    [25,-0.9,-0.3,20.2],
    [3.7,-7.3,-0.1,-18.9],
    [0.7,0.1,-8.2,-56.4]
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
print("lista_independientes")
print(lista_independientes)
print("lista_diagonal")
print(lista_diagonal)
punto_matriz = [0,0,0,0]
convergence = False
print(matriz_df)
def gauss_seidel(matriz, punto, diagonal, independientes, cuenta, error):
    punto_anterior = punto.copy()
    new_error = []
    for row in range(matriz.shape[0]):
        res1 = 0
        for col in range(matriz.shape[1]):
            if (col < matriz.shape[1]-1):
                print ("RES1 = ",matriz.iloc[row,col]," * ",punto[col])
                res1 += matriz.iloc[row,col] * punto[col]
        # print("PUNTO => (",independientes[row]," - ",res1,")/",diagonal[row])
        punto[row] = (independientes[row] - res1)/diagonal[row]
        print(" PUNTO = (",independientes[row] ,"-", res1,")/",diagonal[row]," = ",punto[row])
        if (cuenta > 0):
            # print("ERROR (",punto[row]," - ",punto_anterior[row],")/",punto[row])
            new_error.append(np.abs((punto[row] - punto_anterior[row])/punto[row]))
    if new_error != []:
        error.append(new_error)
            
    return punto, error

row_count = 0
cuenta = 0
list_error = [[0,0,0]]
while cuenta < iteraciones:
    punto, list_error = gauss_seidel(matriz_df, punto_matriz, lista_diagonal, lista_independientes, cuenta, list_error)
    print('PUNTO => ', punto)
    row_count += 1
    cuenta += 1
    
import matplotlib.pyplot as plt
indices = list(range(cuenta))
print("list_error")
print(list_error)
error = np.array(list_error)
plt.plot(indices,error[:,0],'b-')
plt.plot(indices,error[:,1],'r*')
plt.plot(indices,error[:,2],'y--')
plt.show()