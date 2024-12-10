numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def quick_sort(nums):

    if len(nums) <= 1:
        return nums
    
    pivot = len(nums) // 2
    # pivot = 0
    # pivot = len(nums) - 1
    
    left = []
    right = []
    for num in nums:
        if num != nums[pivot]:
            if num <= nums[pivot]:
                left.append(num)
            else:
                right.append(num)

    return quick_sort(left) + [nums[pivot]] + quick_sort(right)


numbers = quick_sort(numbers)
print(numbers)
