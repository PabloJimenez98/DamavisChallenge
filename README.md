# Damavis Challenge Explanation

### Pablo Jiménez Cruz

ENG:

Data Structure:

I have used a circular doubly linked list, since to simulate the movement of the snake I will need to constantly access the head and tail, so a simple linked list would not be as optimal. The cost of creating, inserting and deleting elements in the list will be constant, O(1), while the cost of checking for the next movement will be linear, O(n), since I haven't come up with an integer cost method that checks if the new element will collide with another. I tried adding a set to the list structure where the values are stored, duplicating them, since their access is faster than that of the linked list, but the execution time did not improve the one previously obtained and the memory cost increased.



Algorithm used:

I have used an algorithm with tree structure in which each level of the tree is a turn, which go from zero to "depth" - 1 and each branch are the possible moves, 'u', 'd', 'l', 'r'. To optimize the algorithm I have cut the branches in which it is checked that the snake has collided with itself or has left the board. I have taken into account constraints such as that the tail can occupy the space that the head had had in the previous turn.


Remarks:

For this implementation I have not added functionalities such as saving the path that the snake has followed in each branch of the tree in order to be able to all the different successful paths obtained, as I considered that it would significantly slow down the execution. For its implementation a list would be added, which would be passed by reference, as Python does by default, in which each time the correct path criterion is met a new record would be added to the list.
For the data input I read them from a txt file which parses the first three lines and transforms the data with the structure described in the statement. Probably it could have been done in a more elegant way, but I did not consider it a priority in the test.
The program output shows only the number of possible paths on one line and the time in seconds it took to run the program, including reading data from the txt, on the next line.




ESP:

Estructura de Datos:

He empleado una lista doblemente enlazada circular, ya que para simular el movimiento de la serpiente voy a necesitar acceder constantemente a la cabeza y a la cola, por lo que una lista enlazada simple no sería tan óptima. El coste de crear, insertar y eliminar elementos en la lista será constante, O(1), mientras que el coste de comprobar el siguiente movimiento será lineal, O(n), ya que no se me ha ocurrido un método de coste entero que compruebe si el nuevo elemento colisionará con otro. Probé a añadir un set a la estructura de la cola donde se guarden los valores, duplicándolos, puesto que su acceso es mas rápido que el de la lista enlazada, pero el tiempo de ejecución no mejoraba el obtenido previamente y el coste de memoria aumentaba.



Algoritmo empleado:

He empleado un algoritmo con estructura de árbol en el cual cada nivel del árbol es un turno, los cuales van de cero a "depth" - 1 y cada ramificación son los posibles movimientos, 'u', 'd', 'l', 'r'. Para optimizar el algoritmo he cortado las ramas en las cuales se revisa que la serpiente ha colisionado consigo misma o ha salido del tablero. He tenido en cuenta restricciones como que la cola puede ocupar el espacio que había tenido la cabeza en el turno anterior.


Observaciones:

Para esta implementación no he añadido funcionalidades como guardar el camino que ha seguido la serpiente en cada rama del árbol para poder todos los diferentes caminos exitosos obtenido, ya que consideré que ralentizaría significativamente la ejecución. Para su implementación se añadiría una lista, la cual se pasaría por referencia, como hace Python por defecto, en la cual cada vez que se cumpla el criterio de camino correcto se añadiría un nuevo registro a la lista.
Para la entrada de datos los leo de un archivo txt el cual analiza las tres primeras líneas y transforma los datos con la estructura que se describe en el enunciado. Probablemente se podría haber hecho de manera mas elegante, pero no lo consideré prioritario en la prueba.
La salida del programa muestra únicamente el número de posibles rutas en una línea y el tiempo en segundos que ha tardado en ejecutarse el programa, incluyendo la lectura de datos del txt, en la siguiente línea.