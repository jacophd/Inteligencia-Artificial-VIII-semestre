# Actividad 2 - Búsqueda y sistemas basados en reglas Ibero_ingenieria de software virtual VIII semestre
# por JORGE CHAMORRO ID BANNER 100080449

import networkx as nx

"""Networkx es un paquete para la creación manipulación, y estudio de la estructura
dinámicas y función de redes complejas, y se puede adaptar como motor de reglas, 
lo escogí por facilidad de uso"""

# BASE DEL CONOCIMIENTO
"""Para la base de conocimiento se toma como ejemplo hipotético el metro de una ciudad
de solo 4 estaciones, y se configura como un grafo siendo los nodos las estaciones
y las aritsas la distancia entre las estaciones, el peso de las aristas para el 
ejercicio se asume como la distancia en km entre estaciones"""

#Datos del metro (grafo)
nodes = ['A', 'B', 'C', 'D']
edges = [('A', 'B', {'weight': 10}), 
        ('A', 'C', {'weight': 2}),
        ('B', 'C', {'weight': 5}), 
        ('B', 'D', {'weight': 15}), 
        ('C', 'D', {'weight': 3})]

# Crear el grafo
"""Para poder gestionar las reglas y analizar la base de conocimiento se crea
el grafo de las rutas del metro y se utiliza el método Dijkstra para buscar
el camino más corto entre dos estaciones, aplicando las reglas"""
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Calcular el camino más corto usando Dijkstra
def shortest_path(start, end):
    return nx.shortest_path(G, start, end, weight='weight')

# MOTOR DE REGLAS
"""El motor de reglas se crea como una función que toma como parametros
el inicio START y el final del recorrido END, la regla en general
aplica un condicional para reconocer los parametros y aplicar el algoritmo
Dijkstra con los mismos parametros por medio de un bucle"""
def rule_engine(start, end):
    # Reglas para seleccionar el camino más corto
    if start == 'A' and end == 'D':
        return shortest_path('A', 'D')
    elif start == 'B' and end == 'D':
        return shortest_path('B', 'D')
    elif start == 'C' and end == 'D':
        return shortest_path('C', 'D')
    elif start == 'D' and end == 'A':
        return shortest_path('D', 'A')
    elif start == 'A' and end == 'B':
        return shortest_path('A', 'B')
    elif start == 'A' and end == 'C':
        return shortest_path('A', 'C')
    elif start == 'B' and end == 'A':
        return shortest_path('B', 'A')
    elif start == 'B' and end == 'C':
        return shortest_path('B', 'C')
    elif start == 'C' and end == 'A':
        return shortest_path('C', 'A')
    elif start == 'C' and end == 'B':
        return shortest_path('C', 'B')
    elif start == 'D' and end == 'B':
        return shortest_path('D', 'B')
    elif start == 'D' and end == 'C':
        return shortest_path('D', 'C')
    else:
        return None

# INTERFAZ DE USUARIO
print("Ingresa la estación del metro donde te encuentras de la siguientes opciones (A, B, C, D): ")
start_point = input ()
print("Ingresa la estación del metro a la cual deseas llegar (A, B, C, D): ")
end_point = input ()

shortest_path = rule_engine(start_point, end_point)
if shortest_path:
    print(f"El camino más corto de {start_point} a {end_point} es: {shortest_path}")
else:
    print("No se encontró un camino válido.")
    