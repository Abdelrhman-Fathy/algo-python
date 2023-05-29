#167. Two Sum II - Input Array Is Sorted

def two_sum_2(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        sum = numbers[left] + numbers[right]
        if target == sum:
            return [left+1, right+1]
        elif sum < target:
            left+=1
        else:
            right -=1
    return []

def test():
    a = [2,7,11,15]
    print(two_sum_2(a, 9))