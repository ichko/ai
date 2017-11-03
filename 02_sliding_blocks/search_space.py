from collections import defaultdict
import heapq as hq


class PriorityQueue:
    def __init__(self):
        self.data = []

    def empty(self):
        return len(self.data) == 0
    
    def put(self, item, priority):
        hq.heappush(self.data, (priority, item))

    def get(self):
        return hq.heappop(self.data)[1]


class SearchSpace:

    def get_neighbors(self, vertex):
        raise NotImplementedError()

    def heuristic(self, current, goal):
        return 0

    def get_path(self, start, end, predecessor):
        result = []
        while end != start:
            result.append(end)
            end = predecessor[end]

        return [start] + result[::-1]

    def a_star(self, start, end):
        predecessor = {}
        distance = defaultdict(lambda: float('inf'))
        distance[start] = 0
        visited = set()

        front = set()
        front.add(start)
        score = PriorityQueue()
        score.put(start, 0)

        while len(front) > 0:
            current = score.get()
            front.remove(current)
            visited.add(current)

            if current == end:
                return self.get_path(start, end, predecessor)

            for neighbor, weight in self.get_neighbors(current):
                if neighbor not in visited:
                    new_dist = distance[current] + weight
                    heuristic = new_dist + self.heuristic(current, end)

                    if neighbor not in front:
                        front.add(neighbor)
                        score.put(neighbor, heuristic)

                    if distance[neighbor] > new_dist:
                        distance[neighbor] = new_dist
                        predecessor[neighbor] = current

        return []
