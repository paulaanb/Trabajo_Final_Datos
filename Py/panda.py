import pandas as pd
#import matplotlib as plt
import numpy as np

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
df['EDAD'].count() #devuelve el numero de elementos que no son nulos en la columna 'EDAD'
df['EDAD'].sum() #devuelve la suma de los datos (si son numeros) o su concadenacion (si es string) en la columna 'EDAD'
df['EDAD'].cumsum() #devuelve una serie con la suma acumulada de los datos de la columna 'EDAD'
df['EDAD'].value_counts() #devuelve una serie con la frecuencia de aparecion de cada valor en la columna 'EDAD'
df['EDAD'].min() #devulve el valor minimo en la columna 'EDAD'
df['EDAD'].max() #devuelve el valor maximo en la columna 'EDAD'
df['EDAD'].mean() #devuelve la media de los datos (numericos) en la columna
df['EDAD'].std() #devuelve la desviacion tipica de los datos numericos
df['EDAD'].describe() #devuelve una serie con un resumen de algunos de los datos anteriores, como la media, la desviacion tipica...

#asiganción
print('--------------ASIGNACIÓN---------------')
df1 = df.copy()#copia del DataFrame, para no modificarlo
print(df1.equals(df)) #comprobamos que son iguales
print(df1.head(1))
df1.loc[0, 'EDAD'] = 3
print(df1.head(1))

#matplotlib
'''
La librería matplotlib no se nos instala, por eso no podemos comprobarlo. Hemos conseguido hacer hasta aquí.
'''
'''fig = plt.figure() #creamos la  figura, es donde se construyen todos los gráficos 
ax = fig.add_subplot(1, 1, 1) # marco
ax.set_title('Título del gráfico')
ax.set_xlabel('Etiqueta para el eje X')
ax.set_ylabel('Etiqueta para el eje Y')
ax.xaxis.grid(True) #Poner rejillas eje x
ax.yaxis.grid(True) #Poner rejillas eje y
'''

#agrupación
print('------------AGRUPACIÓN---------------')
print(df.groupby('PAIS_NACI')['EDAD'].sum())



