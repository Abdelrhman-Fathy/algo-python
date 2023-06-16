import heapq
def heap_sort(a):
   heapq.heapify(a)
   result = []
   while len(a) > 0 :
       result.append(heapq.heappop(a))
   return result

def test():
    a = [200, 101, 53, 40, 20, 6, 4]
    #a = [5,3,1,6,2,4]
    print("unsorted "+ str(a))
    a = heap_sort(a)
    print("sorted " + str(a))