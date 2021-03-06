import csv
from collections import Counter
from nntplib import GroupInfo
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

#Eliminar espacio en blanco
def borrar(fichero):
    for a in fichero:
        for key, value in a.items():
            if value == '':
                a[key] = 0

borrar(fichero)

#Tipos de datos en nuestro fichero
fichero1 = fichero[0]
print('\n')
print('Información sobre los datos')
for key, values in fichero1.items():
    print(str(key) + '\t' + str(type(values)))

#Agrupaciones
def grupo(col):
    grupos = []
    for a in fichero:
        g = a[col]
        grupos.append(g)
       
    total = Counter(grupos) 
    return total
print('\n')
genero = grupo('SEXO')
genero['Mujer'] = genero['2']
del(genero['2'])
genero['Hombre'] = genero['1']
del (genero['1'])
print('En nuestros dados tenemos: ' + '\n' + str(genero))
edad = grupo('EDAD')
edad['Menores de 30 años'] = edad['1']
edad['De 30 a 35 años'] = edad['2']
edad['Mayores de 35 años'] = edad['3']
del(edad['1'], edad['2'], edad['3'])
print(edad)

#Añadir columnas
fichero2 = fichero
def añadirdatos(genero):
    valor_genero = list(genero.values())
    for a in fichero2:
        a['Media de hombres'] = round((valor_genero[1]) / (len(fichero2)) * 100, 2)
    print('\n')
    print('Hemos añadido la siguiente columna "Media de hombres": '+ str(a['Media de hombres']))
    print(fichero2[0])
añadirdatos(edad)

#Eliminar columnas
def borrardatos():
    for a in fichero2:
        del (a['Media de hombres'])
    print('\n')
    print('Hemos eliminado la columna que hemos añadido antes')
    print(fichero2[0])

borrardatos()