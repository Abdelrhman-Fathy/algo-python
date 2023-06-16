#https://leetcode.com/problems/top-k-frequent-elements/
#347. Top K Frequent Elements

import collections
import random

def top_k_frequent_elements(nums, k):
    freq = collections.Counter(nums)
    arr = list(freq.keys())
    index = len(arr) - k
    helper(arr, 0, len(arr)-1, freq, index)
    return arr[index:]



def helper(arr, start, end, freq, index):
    if start >= end:
        return
    pivot = arr[random.randint(start,end)]
    smaller = start - 1
    middle = start - 1
    for bigger in range(start, end+1):
        if freq[arr[bigger]] < freq[pivot]:
            middle +=1
            arr[middle], arr[bigger] = arr[bigger], arr[middle]
            smaller +=1
            arr[smaller],arr[middle] = arr[middle],arr[smaller]
        elif freq.get(arr[bigger]) == freq.get(pivot):
            middle +=1
            arr[middle], arr[bigger] = arr[bigger], arr[middle]
    if smaller+1<=index<=middle:
        return
    elif index < smaller+1:
        helper(arr, start, smaller, freq, index)
    else:
        helper(arr, middle+1, end, freq, index)



def helper2(arr, start, end, freq, index):
    if start >= end:
        return
    pivot = random.randint(start,end)
    arr[pivot], arr[start] = arr[start], arr[pivot]
    smaller = start
    for bigger in range(start+1, end+1):
        if freq.get(arr[bigger]) <= freq.get(arr[start]):
            smaller +=1
            arr[smaller],arr[bigger] = arr[bigger],arr[smaller]
    arr[start],arr[smaller] = arr[smaller],arr[start]
    if index == smaller:
        return
    elif index < smaller:
        helper2(arr, start, smaller-1, freq, index)
    else:
        helper2(arr, smaller+1, end, freq, index)




def test():
    nums = [1, 1, 1, 2,2, 2, 3,3,3]
    k = 2
    print(top_k_frequent_elements(nums, k))
