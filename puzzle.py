from collections import deque

def solucion_a_star(estado_inicial, estado_final):
    frontera = deque([(estado_inicial, 0, [])])  # (estado, costo, camino)
    visitados = set()
    visitados.add(estado_inicial)

    while frontera:
        estado_actual, costo_actual, camino_actual = frontera.popleft()

        if estado_actual == estado_final:
            print("Movimientos realizados:")
            for movimiento in camino_actual:
                print_matriz(movimiento)
            return camino_actual

        for movimiento in movimientos_validos(estado_actual):
            if movimiento not in visitados:
                costo_nuevo = costo_actual + 1
                camino_nuevo = camino_actual + [movimiento]
                frontera.append((movimiento, costo_nuevo, camino_nuevo))
                visitados.add(movimiento)

    return []  # No se encontró solución

# Función para obtener el índice de la pieza vacía
def indice_vacio(estado):
    return estado.index(0)

# Función para obtener las coordenadas de la pieza vacía
def coordenadas_vacio(estado):
    indice = indice_vacio(estado)
    fila = indice // 3  # Asumiendo un rompecabezas 3x3
    columna = indice % 3
    return fila, columna

# Función para generar los movimientos válidos
def movimientos_validos(estado):
    movimientos = []
    fila, columna = coordenadas_vacio(estado)

    # Movimiento hacia arriba
    if fila > 0:
        nuevo_estado = list(estado)
        indice_swap = (fila - 1) * 3 + columna
        nuevo_estado[indice_vacio(estado)], nuevo_estado[indice_swap] = nuevo_estado[indice_swap], nuevo_estado[indice_vacio(estado)]
        movimientos.append(tuple(nuevo_estado))

    # Movimiento hacia abajo
    if fila < 2:
        nuevo_estado = list(estado)
        indice_swap = (fila + 1) * 3 + columna
        nuevo_estado[indice_vacio(estado)], nuevo_estado[indice_swap] = nuevo_estado[indice_swap], nuevo_estado[indice_vacio(estado)]
        movimientos.append(tuple(nuevo_estado))

    # Movimiento hacia la izquierda
    if columna > 0:
        nuevo_estado = list(estado)
        indice_swap = fila * 3 + columna - 1
        nuevo_estado[indice_vacio(estado)], nuevo_estado[indice_swap] = nuevo_estado[indice_swap], nuevo_estado[indice_vacio(estado)]
        movimientos.append(tuple(nuevo_estado))

    # Movimiento hacia la derecha
    if columna < 2:
        nuevo_estado = list(estado)
        indice_swap = fila * 3 + columna + 1
        nuevo_estado[indice_vacio(estado)], nuevo_estado[indice_swap] = nuevo_estado[indice_swap], nuevo_estado[indice_vacio(estado)]
        movimientos.append(tuple(nuevo_estado))

    return movimientos

# Función para imprimir una matriz 3x3
def print_matriz(estado):
    matriz = [estado[i:i+3] for i in range(0, len(estado), 3)]
    for fila in matriz:
        print(' '.join(str(x) if x != 0 else ' ' for x in fila))
    print()

# Ejemplo de uso
estado_inicial = tuple([4, 1, 2,
                        5, 8, 3,
                        7, 0, 6])
estado_final = tuple([1, 2, 3,
                      4, 5, 6,
                      7, 8, 0])

solucion = solucion_a_star(estado_inicial, estado_final)

if solucion:
    print("Solución encontrada:")
else:
    print("No se encontró solución.")