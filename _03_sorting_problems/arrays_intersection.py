#https://leetcode.com/problems/intersection-of-three-sorted-arrays/
def arrays_intersection(arr1, arr2, arr3):
    i = 0
    j = 0
    k = 0
    result = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        #print([i,j,k], [arr1[i],arr2[j],arr3[k]])
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i+=1
            j+=1
            k+=1
        elif arr1[i] < arr2[j] or arr1[i] < arr3[k]:
            i+=1
        elif arr2[j] < arr1[i] or arr2[j] < arr3[k]:
            j+=1
        elif arr3[k] < arr1[i] or arr3[k] < arr1[k]:
            k+=1
    return result

def test():
    arr1 = [1,2,3,4,5,10,12]
    arr2 = [1,2,5,7,9,10,12,13]
    arr3 = [1,3,4,5,8,10,11,12,13]
    print(arrays_intersection(arr1, arr2, arr3))
