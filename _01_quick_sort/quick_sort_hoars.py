import random
def helper(a, start, end):
    if start>=end:
        return
    pivot = random.randint(start,end)
    a[start],a[pivot] = a[pivot],a[start]
    smaller = start + 1
    bigger = end
    while smaller <= bigger:
        if a[smaller] <= a[start]:
            smaller +=1
        elif a[bigger] > a[start]:
            bigger -=1
        else:
            a[bigger],a[smaller] = a[smaller],a[bigger]
        a[bigger], a[start] = a[start], a[bigger]
        helper(a, start, bigger)
        helper(a, smaller, end )

def test():
    a = [200, 101, 53, 40, 20, 6, 4,1]
    #a = [5,3,1,6,2,4]
    print("unsorted "+ str(a))
    helper(a, 0, len(a)-1)  # a,0,5
    print("sorted " + str(a))
