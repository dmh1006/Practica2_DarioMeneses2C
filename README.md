# Práctica 2 – Planificación de rutas hospitalarias  
**Sistemas Inteligentes – Universidad de Burgos**

Autor: **Darío Meneses**  
Convocatoria: **Segunda convocatoria**

---

## Descripción del proyecto

En esta práctica se aborda el problema de la planificación de rutas en un entorno hospitalario mediante el uso de algoritmos de búsqueda clásicos. El hospital se modela como una matriz bidimensional en la que cada celda representa un tipo de estancia (pasillos, consultas, quirófanos, UCI, etc.), asociándose a cada una de ellas una penalización de coste.

El objetivo principal es comparar distintos algoritmos de búsqueda, tanto no informados como informados, analizando el coste total del recorrido, la longitud del camino, el número de nodos expandidos, el tamaño máximo de la frontera y el tiempo de ejecución.

La práctica consta de dos ejercicios. En el primero se calcula una ruta básica entre dos puntos del hospital. En el segundo se resuelve una ruta de seguridad que debe recorrer varios servicios en un orden determinado, utilizando una planificación por tramos.

Además, el proyecto incluye un sistema de visualización gráfica que permite representar los recorridos obtenidos sobre el mapa del hospital.

---

## Algoritmos implementados

En el proyecto se han implementado y comparado los siguientes algoritmos de búsqueda:

La búsqueda en anchura (BFS), que es un algoritmo no informado y garantiza el menor número de pasos al explorar el espacio de estados por niveles.

La búsqueda voraz, que es un algoritmo informado que utiliza únicamente la heurística (distancia Manhattan) para guiar la búsqueda hacia el objetivo, priorizando la cercanía sin tener en cuenta el coste acumulado.

El algoritmo A*, que combina el coste acumulado del camino y la heurística para minimizar el coste total del recorrido, ofreciendo un equilibrio entre calidad de la solución y esfuerzo computacional.

Todos los algoritmos devuelven un resultado homogéneo que permite su comparación directa.

---

## Requisitos previos

Para ejecutar la práctica es necesario disponer de una instalación de Python versión 3.9 o superior. El proyecto es compatible con sistemas Windows, Linux y macOS. Se recomienda el uso de Jupyter Notebook o Visual Studio Code para la ejecución del notebook principal.

---

## Creación del entorno virtual

Para garantizar una ejecución correcta y reproducible del proyecto, se recomienda crear un entorno virtual de Python dentro de la carpeta del proyecto. Una vez creado, el entorno virtual debe activarse antes de instalar las dependencias y ejecutar la práctica.

---

## Instalación de dependencias

Con el entorno virtual activado, se deben instalar las dependencias del proyecto utilizando el archivo requirements.txt incluido en el repositorio. Este archivo contiene todas las librerías necesarias para la ejecución de los algoritmos y la visualización de los recorridos.

---

## Ejecución de la práctica

La ejecución principal del proyecto se realiza desde el archivo main.ipynb. Este notebook debe abrirse y ejecutarse de forma secuencial, asegurándose de que el kernel seleccionado corresponde al entorno virtual creado previamente.

El notebook se encarga de cargar el mapa del hospital y las penalizaciones, ejecutar los algoritmos de búsqueda para cada ejercicio, generar las tablas comparativas con las métricas obtenidas y mostrar la visualización gráfica de los recorridos.

---

## Visualización de rutas

La práctica incluye un visor gráfico que permite representar el mapa del hospital y el recorrido seguido por cada algoritmo. El visor permite identificar el punto de inicio y el objetivo, recorrer el camino paso a paso y visualizar rutas continuas incluso en el caso de la planificación multiobjetivo del segundo ejercicio.

Para que la visualización funcione correctamente, es importante ejecutar el notebook desde la carpeta raíz del proyecto, de forma que la carpeta images_hospital sea accesible mediante rutas relativas.

---

## Resultados y comparación

Los resultados obtenidos incluyen el coste total del recorrido, el número de pasos, el número de nodos expandidos, la frontera máxima alcanzada y el tiempo de ejecución. Estos datos se presentan en tablas comparativas que permiten analizar el comportamiento de cada algoritmo tanto en la ruta básica como en la ruta de seguridad.

---

## Observaciones finales

El proyecto ha sido desarrollado siguiendo una organización modular que separa claramente el modelado del problema, la implementación de los algoritmos de búsqueda, la gestión de métricas y la visualización de resultados. Esta organización facilita la comparación objetiva entre algoritmos y la extensión del proyecto a otros escenarios de planificación.

---

## Licencia

Proyecto desarrollado con fines académicos para la asignatura Sistemas Inteligentes de la Universidad de Burgos.
