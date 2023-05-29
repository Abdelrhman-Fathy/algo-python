def bubbleSort(a):
    for i in range(len(a)): #0
        for red in range(len(a) - 1, i, -1): #6,0
            if a[red] < a[red - 1]:
                a[red], a[red - 1] = a[red - 1], a[red]


def test():
    # a = [101,6,20,4,200,40,53]
    a = [200, 101, 53, 40, 20, 6, 4]
    print("unsorted " + str(a))
    bubbleSort(a)
    print("sorted " + str(a))