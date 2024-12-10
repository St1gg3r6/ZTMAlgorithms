numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def merge_sort(nums):

    if len(nums) == 1:
        return nums
    
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    
    # i = 0
    # j = 0
    # merged = []
    # while i < len(left) or j < len(right):
    #     if j == len(right) and i < len(left):
    #         merged.append(left[i])
    #         i += 1
    #     elif i == len(left) and j < len(right):
    #         merged.append(right[j])
    #         j += 1
    #     elif left[i] <= right[j]:
    #         merged.append(left[i])
    #         i += 1
    #     else:
    #         merged.append(right[j])
    #         j += 1

    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left[0])
            left.pop(0)
        else:
            merged.append(right[0])
            right.pop(0)
    if left:
        merged += left
    if right:
        merged += right

    return merged


numbers = merge_sort(numbers)
print(numbers)
