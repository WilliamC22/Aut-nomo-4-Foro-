Explicación de Principales Funcionalidades del Programa

1.- Lista de Dibujos del Ahorcado
    - Este punto contiene las imagenes clasicas que representan el progreso del juego 
    en este mismo se evidencian las letras adivinadas y de igual manera los graficos 
    representan el fin del juego.

2.- Función "obtener_palabra()"
    - Esta función se encarga de obtener una palabra para iniciar el juego.
    - Tiene una lista de palabras predefinidas.
    - De igual manera si el usuario desea que se adivine una palabra escogida por el mismo, puede hacerlo
      de manera personalizada y este es uno de los punto smas importantes del código.

3.- Función jugar_ahorcado():

  -Comienza el juego del ahorcado.
  -Llama a obtener_palabra() para obtener la palabra que el jugador debe adivinar.
  -Inicializa las variables:
    -palabra: La palabra a adivinar.
    -palabra_adivinada: Una cadena de guiones bajos _ del mismo tamaño que la palabra a adivinar, para mostrar las letras adivinadas.
    -intentos_restantes: Inicializado en 6, que representan los intentos del jugador.
    -letras_adivinadas: Una lista vacía para almacenar las letras que el jugador ha intentado adivinar.

4.- Bucle principal del juego (while):

  -Mientras haya intentos restantes (intentos_restantes > 0) y la palabra a adivinar tenga guiones bajos sin reemplazar ("_" in palabra_adivinada), el juego continuará.
  -En cada iteración del bucle:
    -Muestra el dibujo correspondiente al número de intentos restantes, la palabra parcialmente adivinada, los intentos restantes y las letras adivinadas.
    -Solicita al jugador que ingrese una letra.
    -Verifica si la letra ya ha sido ingresada antes. Si es así, pide al jugador que ingrese otra letra.
    -Agrega la letra ingresada a la lista de letras adivinadas.
    -Si la letra está en la palabra a adivinar, actualiza la palabra adivinada mostrando la(s) letra(s) en la posición correspondiente.
    -Si la letra no está en la palabra a adivinar, reduce los intentos restantes y muestra un mensaje de letra incorrecta.
    
5.- Condición de finalización del juego (if):

  -Si ya no hay guiones bajos en palabra_adivinada, significa que el jugador ha adivinado todas las letras de la palabra. Muestra un mensaje de victoria.
  -Si todavía hay guiones bajos en palabra_adivinada, significa que el jugador ha agotado sus intentos. Muestra la palabra que debía adivinar.
  
6.- Llamada inicial a jugar_ahorcado():

   -Inicia el juego llamando a la función jugar_ahorcado().

Objetivo del Programa:
* Este código tiene como objetivo brindar una experiencia completamente placentera al jugar el juego del ahorcado, tomando varias similitudes de otros programas,
  con funcionalidades como permitir al jugador intentar adivinar una palabra seleccionada aleatoriamente o ingresada por el usuario, mostrando visualmente el progreso del
  ahorcado y las letras adivinadas. Esto logrando que la experiencia de juego sea lo mas similar posible al clásico juego del ahorcado.
