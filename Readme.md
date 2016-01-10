Este proyecto está desarrollado en Django 1.8, corresponde a la 
evaluación de parte datata para reclutamiento.

Está divido en 4 aplicaciones Django

1. La aplicación "asignación" se correcponde con la resolución del punto 1 
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
ejecución de Big-Oh O(n) está función calcula el valor máximo del elemento de una lista, dando los siguientes tiempos:

Size      Ram           TC                TAR
8k*8k   = 2,0 GB   6.62133097649 s  2.44758892059 s
9k*9k   = 2,5 GB   8.26022982597 s  3.09848880768 s
10k*10  = 3,1 GB  10.0229918957  s  3.83003997803 s
11k*11k = 3,7 GB  13.5811810493  s  4.23024606705 s
12k*12k = 4,4 GB  15.7351219654  s  4.97430205345 s
13k*13k = 5,2 GB  18.5389990807  s  6.01450896263 s
14k*14k  = 6 GB   20.1895141602  s  6.90269398689 s

Size = es el tamaño en miles de la matriz 
Ram  = se refiere a la cantidad de Ram que ocupa la matriz creada
TC   = tiempo que tardo en construir la matriz
TAR  = tiempo del algoritmo en resolver el problema (calcular el maximo de cada persona y sumar los maximos)

Estos tiempos fueron obtenidos de correr el algoritmo en una máquina con un core i5 y 8GB Ram


Entonces empece a estudiar la posibilidad de tratar de ejecutar julia en python dado que en cuanto a tiempos de ejecución es mucho mejor, 
luego de varios intentos y usando la librería pyjulia no lo he logrado, tal vez con un poco más de tiempo esto se podría llevar a cabo 
reduciendo mucho el tiempo de ejecución.


2. La aplicacion register


3. La aplicación derivada

4. La aplicación nombres
