import pandas as pd
import matplotlib.pyplot as plt
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


#valores perdidos
print('----------VALORES-PERDIDOS--------------')
df.fillna('0', inplace=True)
print(df)

#matplotlib
print("--------------------GRAFICAS-------------------------")
def g_barras(lista, x):
    plt.subplots()
    ejey = df[x].value_counts()
    ejex = lista
    plt.bar(ejex, ejey)
    plt.show()
    #con esta funcion hacemos graficas de barras sencillas para clasificar a los universitarios estudiados

sexos = ["MUJERES", "HOMBRES"]
print(df["SEXO"].value_counts())
g_barras(sexos, 'SEXO')

edades = ["ENTRE 30 Y 35", "MAYORES DE 35", "MENORES DE 30"]
print(df["EDAD"].value_counts())
g_barras(edades, 'EDAD')

nacionalidades = ["ESPAÑOLA", "OTRA", "ESPAÑOLA Y OTRA"]
print(df["NACIO"].value_counts())
g_barras(nacionalidades, 'NACIO')

ramas = ["C.SOCIAL/JURID.", "ING/ARQ", "C. SALUD", "ART/HUMAN", "CIENCIAS"]
print(df["RAMA"].value_counts())
g_barras(ramas, "RAMA")

tipo_uni = ["PUB. PRES", "PRIV. PRES", "PRIV. DIST", "PUB. DIST."]
print(df["T_UNIV"].value_counts())
g_barras(tipo_uni, "T_UNIV")

estudio_extrangero = ["NO EST EXTRANGERO", "SI EST EXTRANGERO", "NS/NC"]
print(df["EST_B1"].value_counts())
g_barras(estudio_extrangero, "EST_B1")



#agrupación
print('------------AGRUPACIÓN---------------')
print(df.groupby('PAIS_NACI')['EDAD'].sum())

#clasificación
print('-----------CLASIFICACIÓN-----------------')
print(df.rank()) #rank(), nos devuelve la clasificación de cada valor a lo largo de un eje determinado


#tipo de datos
print('------------TIPO-DE-DATOS------------')
print(df.dtypes)

