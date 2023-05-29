import numpy as np
def two_sum_hash_table(a, target):
    hash_table = {}
    for i in range(len(a)):
        complement = target - a[i]
        if complement in hash_table:
            return [i, hash_table[complement]]
        else:
            hash_table[a[i]] = i


def test():
    a = np.random.randint(-100,101, 20)
    print([a[0], a[1]])
    target = a[0] + a[1]
    result = two_sum_hash_table(a, target)
    print([a[result[0]],a[result[1]]])