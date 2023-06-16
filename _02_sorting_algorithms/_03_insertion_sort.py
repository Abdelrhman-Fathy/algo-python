def insertionSort(a):
    for i in range(len(a)):
        temp = a[i]
        red = i - 1
        while red >= 0 and temp < a[red]:
            a[red + 1] = a[red]
            red -= 1
        a[red + 1] = temp


def test():
    # a = [101,6,20,4,200,40,53]
    a = [200, 101, 53, 40, 20, 6, 4]
    print("unsorted " + str(a))
    insertionSort(a)
    print("sorted " + str(a))
