import pandas as pd
#leer con pandas
df = pd.read_csv('EILU_MAST_2019.csv', delimiter="\t", encoding='UTF-8')
print(df)

#escribir con pandas
prueba = pd.DataFrame(['Hola'], columns=['Prueba'])
prueba.to_csv('prueba.csv')

#Indexación
#filas
print (df.iloc[0])
#columnas
print(df['EDAD'])