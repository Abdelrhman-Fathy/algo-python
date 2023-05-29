import random
def helper(a, start, end):
    if start >= end:  # false
        return
    pivot = random.randint(start, end)
    a[pivot], a[start] = a[start], a[pivot]
    smaller = start  #0
    for bigger in range(start+1, end+1):  # 0,7
        if a[bigger] < a[start]:  # a[6]4,a[0]200
            smaller += 1  # 6
            a[smaller], a[bigger] = a[bigger], a[smaller]  # no change
    # [200, 101, 53, 40, 20, 6, 4]
    a[start], a[smaller] = a[smaller], a[start]
    helper(a, start, smaller-1)
    helper(a, smaller + 1, end)


def test():
    a = [200, 101, 53, 40, 20, 6, 4]
    #a = [5,3,1,6,2,4]
    print("unsorted "+ str(a))
    helper(a, 0, len(a)-1)  # a,0,5
    print("sorted " + str(a))
