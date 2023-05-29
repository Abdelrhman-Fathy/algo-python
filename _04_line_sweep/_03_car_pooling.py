import heapq


def car_pooling(trips, capacity):
    next_start: int
    trips.sort(key=lambda x:x[1])
    pq = []
    persons = 0
    for i in range(len(trips)):
        if i == len(trips) - 1:
            next_start = float('INF')
        else:
            next_start = trips[i + 1][1]
        heapq.heappush(pq, (trips[i][2], trips[i][0]))
        persons += trips[i][0]
        if persons > capacity:
            return False
        while len(pq) > 0 and pq[0][0] <= next_start:
            persons -= heapq.heappop(pq)[1]
    return True


def test():
    #trips = [[2, 1, 5], [3, 3, 7]]
    #capacity = 4

    #trips = [[2, 1, 5], [3, 3, 7]]
    #capacity = 5

    trips = [[7, 5, 6], [6, 7, 8], [10, 1, 6]]
    capacity = 16
    result = car_pooling(trips, capacity)
    print(result)
