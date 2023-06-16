#https://leetcode.com/problems/intersection-of-two-arrays/
#leetcode 349 intersection of two arrays
def arrays_intersection2(nums1,nums2):
    set1 = {}
    set2 = {}
    if len(nums1) < len(nums2):
        set1 = set(nums1)
        set2 = set(nums2)
    else:
        set1 = set(nums2)
        set2 = set(nums1)
    return [x for x in set1 if x in set2]
def test():
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    arrays_intersection2(nums1, nums2)
    print(nums1)


