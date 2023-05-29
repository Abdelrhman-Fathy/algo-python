def three_sum_sorting(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum2 = nums[left] + nums[right]
                if target == sum2:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum2 < target:
                    left += 1
                else:
                    right -= 1
    return result


def test():
    a = [-1,0,1,2,-1,-4]
    print("result: ",three_sum_sorting(a))

