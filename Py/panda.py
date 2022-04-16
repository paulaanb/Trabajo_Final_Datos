import pandas as pd
#leer con pandas
df = pd.read_csv('EILU_MAST_2019.csv', delimiter="\t", encoding='UTF-8')
print(df)

#escribir con pandas
df.to_csv('Perro')