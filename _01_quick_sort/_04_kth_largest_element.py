#https://leetcode.com/problems/kth-largest-element-in-an-array/
#215. Kth Largest Element in an Array

import random
def kth_largest_element(nums,k):
    index = len(nums) - k
    helper(0, len(nums) - 1, nums, index)
    return nums[index]


def helper(start, end, nums, index):
    if start == end:
        return
    smaller = start-1
    middle = start-1
    pivot = nums[random.randint(start,end)]
    #print(pivot)
    for bigger in range(start, end+1):
        if nums[bigger] < pivot:
            middle +=1
            nums[bigger], nums[middle] = nums[bigger], nums[middle]
            smaller +=1
            nums[smaller], nums[middle] = nums[middle], nums[smaller]
        elif nums[bigger] == pivot:
            middle+=1
            nums[middle], nums[bigger] = nums[bigger], nums[middle]
    #print(nums)
    if smaller+1 <= index <= middle:
        return
    elif index < smaller+1:
        helper(start,smaller, nums, index)
    else:
        helper(middle+1, end, nums, index)

def helper2(start, end, nums, index):
    if start == end:
        return
    smaller = start
    pivote = random.randint(start,end)
    nums[pivote], nums[start] = nums[start], nums[pivote]
    for bigger in range(start+1, end+1):
        if nums[bigger] < nums[start]:
            smaller+=1
            nums[smaller], nums[bigger] = nums[bigger], nums[smaller]
    nums[smaller],nums[start] = nums[start], nums[smaller]
    if index == smaller:
        return
    elif index < smaller:
        helper2(start,smaller-1, nums, index)
    else:
        helper2(smaller+1, end, nums, index)
def test():
    nums = [3, 2, 1, 5, 6, 4]
    k = 3
    result = kth_largest_element(nums, k)
    print(result)