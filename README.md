# Actividad 2 - Búsqueda y sistemas basados en reglas Ibero_ingenieria de software virtual VIII semestre
# por JORGE CHAMORRO ID BANNER 100080449

Networkx es un paquete para la creación manipulación, y estudio de la estructura
dinámicas y función de redes complejas, y se puede adaptar como motor de reglas, 
lo escogí por facilidad de uso

# BASE DEL CONOCIMIENTO
Para la base de conocimiento se toma como ejemplo hipotético el metro de una ciudad
de solo 4 estaciones, y se configura como un grafo siendo los nodos las estaciones
y las aritsas la distancia entre las estaciones, el peso de las aristas para el 
ejercicio se asume como la distancia en km entre estaciones

# Crear el grafo
Para poder gestionar las reglas y analizar la base de conocimiento se crea
el grafo de las rutas del metro y se utiliza el método Dijkstra para buscar
el camino más corto entre dos estaciones, aplicando las reglas

MOTOR DE REGLAS
El motor de reglas se crea como una función que toma como parametros
el inicio START y el final del recorrido END, la regla en general
aplica un condicional para reconocer los parametros y aplicar el algoritmo
Dijkstra con los mismos parametros por medio de un bucle
