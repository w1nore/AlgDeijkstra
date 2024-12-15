def dijkstra(graph, start):
    # Инициализация: расстояния до всех вершин бесконечны, кроме стартовой
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Множество посещённых вершин
    visited = set()

    while len(visited) < len(graph):
        # Поиск вершины с минимальным расстоянием среди непосещённых
        min_vertex = None
        for vertex in graph:
            if vertex not in visited:
                if min_vertex is None or distances[vertex] < distances[min_vertex]:
                    min_vertex = vertex

        # Добавляем вершину в посещённые
        visited.add(min_vertex)

        # Обновляем расстояния до соседей
        for neighbor, weight in graph[min_vertex].items():
            if neighbor not in visited:
                new_distance = distances[min_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances


# Пример графа
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Вызов функции для поиска кратчайших путей от вершины 'A'
distances = dijkstra(graph, 'A')
print(distances)
