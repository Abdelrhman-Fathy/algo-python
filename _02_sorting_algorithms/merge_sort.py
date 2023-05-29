def helper(a, start, end):
    if start == end:
        return
    mid = start + (end-start) // 2
    helper(a, start, mid)
    helper(a, mid + 1, end)
    i = start
    j = mid + 1
    arr = []
    while i <= mid and j <= end:
        if a[i] <= a[j]:
            arr.append(a[i])
            i += 1
        else:
            arr.append(a[j])
            j += 1
    if i <= mid:
        arr +=a[i:mid+1]
    if j <= end:
        arr += a[j:end+1]
    a[start:end + 1] = arr
    return


def merge_sort(a):
    helper(a, 0, len(a) - 1)


def test():
    # a = [101,6,20,4,200,40,53]
    a = [200, 101, 53, 40, 20, 6, 4]
    print("unsorted " + str(a))
    merge_sort(a)
    print("sorted " + str(a))
