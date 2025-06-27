

import pandas as pd

# Creo la tabla

tabla = {
         "pelicula" : ["la odisea de los giles","kung fu panda", "cars", "esperando la carroza", "nueve reinas", "relatos salvajes"],
         "puntuacion" : [9,7,8,6,8,10],
         "duracion" : [116, 92, 117, 87, 114, 122]
         }

# Convierto a Dataframe

df = pd.DataFrame(tabla)
print(df)

# 0  la odisea de los giles             9       116
# 1           kung fu panda             7        92
# 2                    cars             8       117
# 3    esperando la carroza             6        87
# 4            nueve reinas             8       114
# 5        relatos salvajes            10       122


# Para seleccionar filas o columnas hay dos funciones "loc" e "iloc"
"loc: usa como parametro el nombre , en cambio iloc: usa el numero de posicion"

# Accedemos a la primera fila
df.loc[0]   #En este caso loc e iloc es lo mismo, xq el nimbre de la fila son numeros(indice)
df.iloc[0]

# Si quiero acceder a una columna (por ej: duracion)
"Usamos dos puntos(:) en fila si queremos ver todas las filas y el culumna la que deseamos"
df.loc[:,"duracion"]   # con loc

df.iloc[:,2]   # con iloc

# Ahora ordenemos por puntuacion las peliculas, de mayor a menor y al reves tambien, dale q se puede!
"Usamos funcion sort_values"
ordenado_ascendente = df.sort_values("puntuacion")

ordenado_descendente = df.sort_values("puntuacion", ascending=False)