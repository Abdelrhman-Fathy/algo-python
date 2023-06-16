import collections

def counting_sort(a):
    c = collections.Counter(a)
    result = []
    for i in range(-5000,50001):
        if i in c:
            for _ in range(c[i]):
                result.append(i)
    return result
def test():
    # a = [101,6,20,4,200,40,53]
    a = [200, 101, 53, 40, 20, 6, 4]
    print("unsorted counting sort" + str(a))
    a = counting_sort(a)
    print("sorted " + str(a))
