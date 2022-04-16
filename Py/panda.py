import pandas as pd
#leer con pandas
df = pd.read_csv('EILU_MAST_2019.csv', delimiter="\t", encoding='UTF-8')
print('---------------LEER---------------------')
print(df)

#escribir con pandas
prueba = pd.DataFrame(['Hola'], columns=['Prueba'])
prueba.to_csv('prueba.csv')

#Indexación
#filas
print('--------------FILAS----------------')
print (df.iloc[0])
#columnas
print('----------------COLUMNA----------------------')
print(df['EDAD'])

#seleccion
print('------------SELECCIÓN--------------------')
print(df['EDAD']== 1)

#resumen de funciones
print("---------------------------RESUMEN DE FUNCIONES----------------------")
df.count() #devuelve el numero de elementos que no son nulos
df.sum() #devuelve la suma de los datos (si son numeros) o su concadenacion (si es string)