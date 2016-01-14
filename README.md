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
Luego de haber llegado a soluciones frustadas empece a estudiar la posibilidad de tratar de ejecutar julia en python 
dado que en cuanto a tiempos de ejecución es mucho mejor, 
Después de varios intentos y usando la librería pyjulia no lo he logrado, tal vez con un poco más de tiempo esto se podría llevar a cabo 
reduciendo mucho el tiempo de ejecución.

Entonces comencé a evaluar la posibilidad de una MaxHeap de Articulos para cada Persona sabiendo que en el peor de los casos en la inserción de la misma 
es de orden O(log N) combinando con la iteración sobre los valores  enviados por parámetro del request da un orden final de O(N*log N)
En cuanto al procesamiento de los datos termina dando de orden O(N) dado que itero sobre todas la MaxHeap de las personas y luego hago un pop sobre 
cada una. El pop es de orden O(1)

También me encontré con problemas en el cliente para poder dibujar en el DOM tablas muy grandes, utilicé datatables paginadas con jquery y peticiones ajax,
para hacer la creación asincrónica y que el usuario pueda ir cargando datos mientras se termina de dibujar el resto de la tabla, igualmente está limitado a cierta cantidad de filas, en este caso 1498,
es decir el valor máximo de la matriz no puede ser de 1498*1498,porque sino no funciona la carga, sin esta logica el navegador se colgaba.
 Con más tiempo tal vez pordría investigar para escribir de manera más eficiente en el DOM o buscar otro tipo de solución o que la entrada sea otra, por ejemplo un archivo csv

2. La aplicacion register que se corresponde con el registro y login de usuario, he agregado el recaptcha de google para evitar bots
tanto en el registro como en el login.

3. La aplicación derivada : utilicé la libreria sympy de python para calcular la deriva de la función enviada por parámetros, estuve probando y funciona aparentemente para cualquier tipo de función incluyendo seno, coseno, etc.
Los gráficos aplican al resultado espero, en lo cual en el cliente para hacerlo use canvas, el punto no lo pude dibujar dado que es la primera vez que dibujo en el navegador funciones matemáticas, lo que si
el punto en cuestión se indica con la informacion x,y
	
4. La aplicación nombres: utilicé angular para que lo cambios aplicados en los inputs se vean dinamicamente en el menu.
