# cartasGame

  Descripción
El juego utiliza una baraja de póker con los siguientes valores para las cartas:

As (A): 1 punto
Números del 2 al 10: Valor nominal (2 es 2 puntos, 3 es 3 puntos, etc.)
Jota (J), Reina (Q) y Rey (K): 11 puntos cada una
El objetivo del juego es obtener la mayor puntuación eligiendo cartas desde los extremos de la fila. Jugarás por turnos contra la máquina, que utiliza un algoritmo de poda alfa-beta para tomar decisiones estratégicas.

    Reglas del Juego
Inicio del Juego: Se distribuye una fila de cartas de forma aleatoria.
Turnos: Los jugadores (tú y la máquina) alternan turnos. El jugador humano siempre empieza primero.
Elección de Cartas: En tu turno, puedes elegir una carta desde el extremo izquierdo o derecho de la fila.
Movimiento de la Máquina: La máquina selecciona la carta óptima usando el algoritmo de poda alfa-beta.
Finalización del Juego: El juego termina cuando no quedan más cartas.
Ganador: El jugador con la puntuación más alta al final del juego es el ganador.

    Requisitos
Python 3.x
Tkinter (incluido en la mayoría de las distribuciones de Python)

Instalación
Clona este repositorio en tu máquina local:
git clone https://github.com/tu_usuario/puntaje-maximo.git

Algoritmo de Poda Alfa-Beta
El juego implementa el algoritmo de poda alfa-beta para que la máquina tome decisiones estratégicas al seleccionar cartas. Este algoritmo reduce la cantidad de nodos evaluados en el árbol de decisiones, permitiendo a la máquina tomar decisiones óptimas en tiempo razonable.
