# take-away-simulator

Simulador del juego "Take away!"
</br>

> Take Away! es un juego matemático de estrategia en el que dos jugadores se turnan para quitar objetos de una pila. El jugador que retire el último objeto (u objetos) de la pila gana el juego. Para jugar se necesitará una pila de nueve fichas y los jugadores se turnarán para quitar fichas de la pila. En cada turno, un jugador debe elegir quitar una o dos fichas de la pila.

</br>

# Variables del Simulador
Archivo principal: Simulation.py
</br>


| Variable o Clase | Descripción |
| ------ | ------ |
| maxMoves | Cantidad de fichas que un jugador puede retirar por turno. |
| dotsStock | Cantidad de fichas inicial en la partida. |
| order | Array que indica el orden de turno de los jugadores simulados. |
| Person(name, playerType)| name: nombre del jugador </br> playerType: tipo de jugador "random" o "smart"|

> Nota: La diferencia entre el playerType "random" y "smart" es que random siempre retirara un numero pseudoaleatorio, mientras que "smart" seguirá la estrategia ganadora identificada y expuesta en nuestra entrega. 



