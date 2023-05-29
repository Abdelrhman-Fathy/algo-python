def selectionSort(a):
    for i in range(len(a)):
        minIndex = i
        for red in range(i + 1, len(a)):
            if a[red] < a[minIndex]:
                minIndex = red
        a[i], a[minIndex] = a[minIndex], a[i]

def test():
    # a = [101,6,20,4,200,40,53]
    a = [200, 101, 53, 40, 20, 6, 4]
    print("unsorted " + str(a))
    selectionSort(a)
    print("sorted " + str(a))
