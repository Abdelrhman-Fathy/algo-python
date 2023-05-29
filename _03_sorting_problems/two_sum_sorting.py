import numpy as np

def two_sum_sorting(a, target):
    a.sort()
    left = 0
    right = len(a)-1
    while left<right:
        sum = a[left] + a[right]
        if sum == target:
            return [left, right]
        elif sum<target:
            left+=1
        else:
            right -=1
    return [-1]



def test():
    a = np.random.randint(-100,101, 20)
    print([a[0], a[1]])
    target = a[0] + a[1]
    result = two_sum_sorting(a, target)
    print([a[result[0]],a[result[1]]])