def merge_sorted_array(nums1,m,nums2,n):
    l = m+n-1
    m -=1
    n -=1
    while m >=0 and n >=0 :
        if nums1[m] > nums2[n]:
            nums1[l] = nums1[m]
            m -=1
        else:
            nums1[l] = nums2[n]
            n -=1
        l -=1
    if n >= 0:
        nums1[:n+1] = nums2[:n+1]
def test():
    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]
    merge_sorted_array(nums1,3,nums2,3)
    print(nums1)
