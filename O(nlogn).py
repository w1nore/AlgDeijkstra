import heapq


def dijkstra(graph, start):
    # Инициализация: расстояния до всех вершин бесконечны, кроме стартовой
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Очередь с приоритетом для хранения вершин и их расстояний
    priority_queue = [(0, start)]

    while priority_queue:
        # Извлекаем вершину с минимальным расстоянием
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если извлечённое расстояние больше текущего, продолжаем (старое значение)
        if current_distance > distances[current_vertex]:
            continue

        # Проходим по соседям текущей вершины
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Если найден более короткий путь, обновляем расстояние
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

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
