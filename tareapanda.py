

import pandas as pd

datos=pd.read_csv('musica.csv')

musicas= pd.DataFrame(datos, columns=['name','artists', 'tempo'])
musicas
# Ordenamos el DataFrame por la columna B de forma ascendente
martista = musicas.sort_values(by='artists')
# Mostramos las primeras tres filas y las columnas B, D y F del DataFrame ordenado
columns = martista
columns.iloc[[3,5,6]]