Este proyecto está desarrollado en Django 1.8, corresponde a la 
evaluación de parte datata para reclutamiento.

Está divido en 4 aplicaciones Django

1. La aplicación "asignación" se corresponde con la resolución del punto 1 
inciso maximizar felicidad colectiva. En la elección final del algoritmo 
que resuelve el problema fue elegida de diferentes estrategias y luego 
de probar diferentes librerías. En un comienzo pensé en resolverlo de 
forma concurrente y utilicé threads de python pero los tiempos de 
ejecución no eran mejores a la solución secuencial, tambien probé con 
las librerías pprocess, multithreading, programingparrallel, y 
los resultados no eran los esperados, el estudio y analisis lleva a la 
conclusión que el cambio de contexto (en un sistema operativo linux) es 
muy costoso junto a la coordinación de los procesos creados con las 
herramientas nombradas, además de limitar este la cantidad de procesos a 
crear por el usuario que fue otro inconveniente encontrado.
Luego de haber llegado a soluciones frustadas opte por la secuencial y utilizar las funciones max() y sum de python que tienen un orden de 
ejecución de Big-Oh O(n) está función calcula el valor máximo del elemento de una lista, dando los siguientes tiempos en el servidor:



8k*8k   Size   2,0 GB Ram   6.62133097649 seg TC   2.44758892059 seg TAR

9k*9k   Size   2,5 GB Ram   8.26022982597 seg TC   3.09848880768 seg TAR

10k*10k Size   3,1 GB Ram  10.0229918957  seg TC   3.83003997803 seg TAR

11k*11k Size  3,7 GB Ram   13.5811810493  seg TC   4.23024606705 seg TAR

12k*12k Size  4,4 GB Ram   15.7351219654  seg TC   4.97430205345 seg TAR

13k*13k Size  5,2 GB Ram   18.5389990807  seg TC   6.01450896263 seg TAR

14k*14k Size  6 GB   Ram   20.1895141602  seg TC  6.90269398689 seg  TAR


Size = es el tamaño en miles de la matriz 

Ram  = se refiere a la cantidad de Ram que ocupa la matriz creada

TC   = tiempo que tardo en construir la matriz en segundos

TAR  = tiempo del algoritmo en resolver el problema (calcular el maximo de cada persona y sumar los maximos) en segundos


Estos tiempos fueron obtenidos de correr el algoritmo en una máquina con un core i5 y 8GB Ram


Entonces empece a estudiar la posibilidad de tratar de ejecutar julia en python dado que en cuanto a tiempos de ejecución es mucho mejor, 
luego de varios intentos y usando la librería pyjulia no lo he logrado, tal vez con un poco más de tiempo esto se podría llevar a cabo 
reduciendo mucho el tiempo de ejecución.

También me encontré con problemas en el cliente para poder dibujar en el DOM tablas muy grandes, utilicé datatables paginadas con jqery y peticiones ajax,
para hacer la creación asincrónica y que el usuario pueda ir cangando datos, igualmente está limitado a cierta cantidad de filas, en este caso 1498,
es decir el valor máximo de la matriz no puede ser de 1498*1498,porque sino no funciona la carga, sin esta logica el navegador se colgaba.
 Con más tiempo tal vez pordría investigar para escribir de manera más eficiente en el DOM o buscar otro tipo de solución.

2. La aplicacion register que se corresponde con el registro y login de usuario, he agregado el recaptcha de google para evitar bots
tanto en el registro como en el login.

3. La aplicación derivada

4. La aplicación nombres
