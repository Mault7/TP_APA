# importacion de librerias 
import pandas as pd
from math import sqrt #importacion la funcion sqrt de la libreria match
import numpy as np 
import matplotlib.pyplot as plt



# realizamos la lectura de los datos
peliculas = pd.read_csv('movie.csv') #Peliculas de nuestra base da datos
rating= pd.read_csv('rating.csv') #las estadisticas de vistas de las peliculas


#Eliminamos datos que no son relevantes para este aplicacion 
#eliminams el ano del titulo

peliculas['year']= peliculas.title.str.extract('(\(\d\d\d\d\))',expand=False)
peliculas['year']= peliculas.title.str.extract('(\d\d\d\d)',expand=False) #eliminamos ()
peliculas['title']= peliculas.title.str.replace('(\(\d\d\d\d\))','')
peliculas['title']= peliculas['title'].apply(lambda x: x.strip())
#mostramos el el resumen de las peliculas para ver resultado
print('peliculas:\n',peliculas.head())

#******************************************
# se puede ver en la img1.png
#******************************************

#Ahora vamos a dividir los valores en columna de genero en una lista de generos 

peliculas['genres']=peliculas.genres.str.split('|')


# Con los generos en listas creamos columnas y utilizamos la tecnca One Hot encoding
# para codificar las peliculas


peliculas_co=peliculas.copy(); # realizamos una copia para no perder la info
for index, row in peliculas.iterrows(): #pasamos por toda la matriz original
    for genre in row['genres']: #asignamos 1 a cada genero correspondiente
        peliculas_co.at[index,genre]=1 #lo guardamos en la copia
        
        
peliculas_co = peliculas_co.fillna(0) # asignamos cero donde corresponda
print('Peliculas codificadas \n',peliculas_co) # mostramos data
#******************************************
# se puede ver en la img2.png
#******************************************

#mostramos en rating de las peliculas 
print('rating\n',rating.head())
#******************************************
# se puede ver en la img3.png
#******************************************

#eliminamos data innesesaria del rating como timestamp
rating=rating.drop('timestamp',1)
print('rating nuevo \n',rating.head())
#******************************************
# se puede ver en la img4.png
#******************************************
# ahora en esta etapa creamos nuestro algoritmo considerando nuestro perfil de usuario

# para este caso nos creamos un perfilde usuario simulando las peliculas que vimos

usuario_en=[
    {'title':'Toy Story','rating':5},
    {'title':'Casino','rating':3.5},
    {'title':'Bad Boys','rating':5},
    {'title':'Batman Forever','rating':5},
    {'title':'Fast and the Furious','rating':5}
    ]

entrada_peli=pd.DataFrame(usuario_en)
print('pleiculas usuario\n',entrada_peli)
#******************************************
# se puede ver en la img5.png
#******************************************
#ahora vamos a agregarle identificacion a cada pelicula que ingreso el usuario
#filtramos filas que contienene los titulos y luego fusionamos con nuestra matriz de peliculas originales

id=peliculas[peliculas['title'].isin(entrada_peli['title'].tolist())] # filtramos
entrada_peli=pd.merge(id,entrada_peli)#fusionamos las matrices

#filtramos informacion innecesaria
entrada_peli=entrada_peli.drop('genres',1).drop('year',1)

#ahora vamos a codificar las peliculas del usuario , para asignar los generos por medio del metodo on hot encoder
peli_usuario=peliculas_co[peliculas_co['movieId'].isin(entrada_peli['movieId'].tolist())]
print('peliculas de usuario codificadas\n',peli_usuario)
#******************************************
# se puede ver en la img6.png
#******************************************
#realizamos de igual forma la limpieza de informacion innecesaria

peli_usuario=peli_usuario.reset_index(drop=True)

tabla_generos=peli_usuario.drop('movieId',1).drop('title',1).drop('genres',1).drop('year',1)
print('tabla de generos\n',tabla_generos)
#******************************************
# se puede ver en la img7.png
#******************************************
# en esta seccion ya modelas el algoritmo  por lo cual tenemos que crear una matriz de peso , haciendo que basicamente sea un producto punto
# necestamos llamar la funcion de la libreria pandas para hacer eso

perfil_usu=tabla_generos.transpose().dot(entrada_peli['rating'])
print('Categoria que le usuario prefiere\n',perfil_usu)
#******************************************
# se puede ver en la img8.png
#******************************************

# ahora vamos a extraer los generos de la tabla original
generos=peliculas_co.set_index(peliculas_co['movieId'])

#mostramos la info necesaria


generos= generos.drop('movieId', 1 ).drop('title', 1).drop('genres', 1).drop('year', 1)

# generos=generos.drop('movieId',1).drop('title',1).drop('genre',1).drop('year',1)
print('generos\n',generos.head())
#******************************************
# se puede ver en la img9.png
#******************************************
generos.shape


# ahora procede a sacar lo que es el promedio ponderado para recomendar 20 peliculas que haya en la base de datos

recom= ((generos*perfil_usu).sum(axis=1))/(perfil_usu.sum())
print('recomendaciones\n',recom.head())
#******************************************
# se puede ver en la img10.png
#******************************************
# ordenamos las recomendaciones en oirden descendente
recom=recom.sort_values(ascending=False)
print('recomendaciones organizadas\n',recom.head())
#******************************************
# se puede ver en la img11.png
#******************************************

# aqui resultaria lo que es la tabla de recomendaciones final

final=peliculas.loc[peliculas['movieId'].isin(recom.head(20).keys())]
nfinal=final[['title']]
print('Nombre de peliculas recomendadas\n',nfinal)
#******************************************
# se puede ver en la img12.png
#******************************************