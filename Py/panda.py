import pandas as pd
import matplotlib as plt
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

#asiganción
print('--------------ASIGNACIÓN---------------')
df1 = df.copy()#copia del DataFrame, para no modificarlo
print(df1.equals(df)) #comprobamos que son iguales
print(df1.head(1))
df1.loc[0, 'EDAD'] = 3
print(df1.head(1))

#matplotlib
fig = plt.figure() #creamos la  figura, es donde se construyen todos los gráficos 
ax = fig.add_subplot(1, 1, 1) # marco
ax.set_title('Título del gráfico')
ax.set_xlabel('Etiqueta para el eje X')
ax.set_ylabel('Etiqueta para el eje Y')
ax.xaxis.grid(True) #Poner rejillas eje x
ax.yaxis.grid(True) #Poner rejillas eje y
