#https://users.monash.edu/~lloyd/tildeAlgDS/Sort/Flag/
#https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation

def sort_colors(nums):
    smaller = -1
    mid = -1
    pivot = 1
    for bigger in range(0, len(nums)):
        if nums[bigger] == pivot:
            mid += 1
            nums[mid], nums[bigger] = nums[bigger], nums[mid]
        elif nums[bigger] < pivot:
            mid += 1
            nums[mid], nums[bigger] = nums[bigger], nums[mid]
            smaller += 1
            nums[mid], nums[smaller] = nums[smaller], nums[mid]


def sort_colors2(nums):
    smaller = 0
    middle = 0
    bigger = len(nums) -1
    pivot = 1
    while middle <= bigger:
        if nums[middle] < pivot:
            nums[smaller], nums[middle] = nums[middle], nums[smaller]
            smaller+=1
            middle+=1
        elif nums[middle] == pivot:
            middle+=1
        else:
            nums[middle],nums[bigger] = nums[bigger],nums[middle]
            bigger-=1

def test():
    nums = [2,0,1]
    sort_colors(nums)
    print(nums)