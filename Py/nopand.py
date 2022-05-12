import csv
'''
Cómo funcionan los modelos(El primer paso si eres nuevo en el aprendizaje automático)
Exploración básica de datos(Cargue y comprenda sus datos)
Su primer modelo de aprendizaje automático (Construyendo tu primer modelo)
Modelo de validación(Mida el rendimiento de su modelo, para que pueda probar y comparar alternativas)
Underfitting y Overfitting(Ajuste su modelo para un mejor rendimiento)
Bosques aleatorios(Usando un algoritmo de aprendizaje automático más sofisticado)
'''
#abrir el fichero csv
fichero = []
with open('EILU_MAST_2019.csv', encoding='UTF-8') as f:
    leer = csv.DictReader(f, delimiter = '\t')
    for i in leer:
        fichero.append(i)
# Bucle para leer el fichero de una manera más ordenada
'''for x in range(len(fichero)):
    print(fichero[x])
    print('\n')'''
#Columnas del fichero
datos = fichero[0].keys()
print('Las columnas de nuestro fichero son en total: ' + str(len(datos)))
print('Columnas:')
print(datos)

#Filas
print('\n')
n = len(fichero)
print('Tenemos ' + str(n) + ' datos para analizar')

        