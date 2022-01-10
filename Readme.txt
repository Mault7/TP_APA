# Trabajo final de materia aprendizaje automatico 

Este trabajo es sobre algoritmo de recomendaciones basado en contenido 

# introduccion 

Esto se basa en recomendar elementos al usuario en base a las similitudes de elementos a los que le usuario le da click o el mas buscado
podriamos considerar esto para las E-comerce como ejemplo que los elementos mas buscados pueden ser muebles para una casa donde segun el 
usuario este queriendo encontrar se le hacen sujerencias de los diferentes cosas que tengan que ver con el hogar tambien adornos, espejos, cuadros,etc
otro de los ejemplos podria ser una cartelera de series o peliculas donde segun los gustos del usuario en cuanto a comedia, drama, aventura. Se le recominda 
que es lo que le podria llegar a gustar ver

para mas claridad y llevarlo a punto practico vamos a realizar sugerencias de peliculas 


tenemos 

Iron man -> categoria: Aventura, Accion, super Heroes
spider man -> categoria: Aventura, Accion, super heroes
bad boys -> categoria: Accion, aventura, 


de las tres mencionadas tenemos el usuario le da una calificacion de:


ironn man -> ratind 10/10
spider man -> rating 8/10
bad boys -> rating 10/10


con esto considerando las categorias los gustos y lo que ya vio se recomienda una de estas tres siguientes peliculas 

Ant-Man -> categoria Aventura, accion, ciencia ficcion
X-men -> categoria Aventura ,accion, super heroes, ficcion
Duro de matar -> Aventura, accion


considerando esto lo que se debe realizar es construir el perfil del usuario


                            aventura            accion          super heroes            ficcion
                     |                  |                  |                    |                       |
                     |                  |                  |                    |                       |
                     |                  |                  |                    |                       |
                     |                  |                  |                    |                       |
                    -------------------------------------------------------------------------------------                                                         
                     |                  |                  |                    |                       |
    iron man    10   |         1        |         1        |          1         |          0            |
                     |                  |                  |                    |                       |
                     |                  |                  |                    |                       |
                     ------------------------------------------------------------------------------------
                     |                  |                  |                    |                       |
    bad boys    8    |         1        |        1         |         0          |           0           |
                     |                  |                  |                    |                       |
                     |                  |                  |                    |                       |
                     ------------------------------------------------------------------------------------
                     |                  |                  |                    |                       |
    spiderman   10   |         1        |         1        |         1          |             0         |
                     |                  |                  |                    |                       |
                     |                  |                  |                    |                       |





                     con esta matriz denominada one hot, podemos ver que se le pone un 1 a todas las catgorias de la pelicula para luego realizar una operacion producto punto 
                     con las puntuaciones que dio el usuario 

                     lo que nos entrega es lo siguiente 


                     ------------------------------------------------------------------------------------
                     |                  |                  |                    |                       |
    Usuario          |         28       |         28       |         20         |             0         |
                     |         0.368    |         0.368    |         0.263      |             0.00      |
                     |                  |                  |                    |                       |


                     en esta etapa se realiza una ponderacion y normalizacion para ver que es lo que mas le gusta al usuario que en este caso seria 

                     Aventura Y Accion



                    Ahora hay que codificar las peliculas que no han sido vistas y son sujeridas 




                            aventura            accion          super heroes            ficcion
                     |                  |                  |                    |                       |
                     |                  |                  |                    |                       |
                     |                  |                  |                    |                       |
                     |                  |                  |                    |                       |
                    -------------------------------------------------------------------------------------                                                         
                     |                  |                  |                    |                       |
    Ant-Man          |         1        |         1        |          0         |          1            |
                     |                  |                  |                    |                       |
                     |                  |                  |                    |                       |
                     ------------------------------------------------------------------------------------
                     |                  |                  |                    |                       |
    X-men            |         1        |        1         |         1          |           1           |
                     |                  |                  |                    |                       |
                     |                  |                  |                    |                       |
                     ------------------------------------------------------------------------------------
                     |                  |                  |                    |                       |
    duro de matar    |         1        |         1        |         0          |           0           |
                     |                  |                  |                    |                       |
                     |                  |                  |                    |                       |


multiplicamos esta matriz con el perfil del usuario 



                     ------------------------------------------------------------------------------------
                     |                  |                  |                    |                       |
    Usuario          |         28       |         28       |         20         |             0         |
                     |         0.368    |         0.368    |         0.263      |             0.00      |
                     |                  |                  |                    |                       |



                     quedando asi 


                     aventura            accion          super heroes            ficcion
                     |                  |                  |                    |                       |                   |           
                     |                  |                  |                    |                       |                   |
                     |                  |                  |                    |                       |                   |
                     |                  |                  |                    |                       |                   |
                    -------------------------------------------------------------------------------------                   |                                                         
                     |                  |                  |                    |                       |                   |
    Ant-Man          |         0.368    |         0.368    |          0         |          0            |          0.736    |      
                     |                  |                  |                    |                       |                   |
                     |                  |                  |                    |                       |                   |
                     ------------------------------------------------------------------------------------                   |
                     |                  |                  |                    |                       |                   |
    X-men            |         0.368    |        0.368     |         0.263      |           0           |          0.999    |
                     |                  |                  |                    |                       |                   |
                     |                  |                  |                    |                       |                   |
                     ------------------------------------------------------------------------------------                   |
                     |                  |                  |                    |                       |                   |
    duro de matar    |         0.368    |         0.368    |         0          |           0           |           0.736   |
                     |                  |                  |                    |                       |                   |
                     |                  |                  |                    |                       |                   |




                     recomendaciones que daria nuestro algoritmo 



                     1. X-men                   0.999
                     2. Ant-Man                 0.736
                     3. duro de matar           0.736




En la practica tenemos realizado un archivo python llamado "main.py" el cual ejecuta estas operaciones con manejo de las datas de 

-movie.csv
-rating.csv 


estas datas se sacaron de la pagina de Kaggle
Link = https://www.kaggle.com/blirinddanjolli/user-based-movie-recommendation/data?select=rating.csv



# Correr el trabajo 


Para poder correr este script primero hay que descargar los archivos y descomprimir los dos zip
-movie.csv.zip
-rating.csv.zip

estos dos se encuentran en la pagina 
Link = https://www.kaggle.com/blirinddanjolli/user-based-movie-recommendation/data?select=rating.csv
#!!!!estos archivos deben descargarse y descomprimirse dentro la carpeta ciencia de datos!!!!!!



luego de las descargas y descompresion es necesario instalar las librerias de python 
-pandas 
-matplotlib

para instalar estas librerias usamos los comandos 

-pip3 install pandas
-pip3 install matplotlib


con todas las librerias istaladas corremos el script con el comandos 

python3 main.py

y listo!!!!!!!!!!!!!!