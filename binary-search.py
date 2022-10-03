# def search(nums, target):
#     start = 0
#     end = len(nums)-1

#     while start <= end:
#         mid = start + (end-start) // 2

#         if nums[mid] > target:
#             end = mid-1
#         elif nums[mid] < target:
#             start = mid+1
#         else:
#             return mid

#     return -1


# if __name__ == '__main__':
#     nums = [2, 12, 15, 17, 27, 29, 45]
#     target = 17
#     print(search(nums, target))

# Order-agnostic search approach
def search(nums, target):
    start = 0
    end = len(nums)-1

    is_ascending = nums[start] < nums[end]

    while start <= end:
        mid = start + (end-start)//2

        if target == nums[mid]:
            return mid

        if is_ascending:
            if target < nums[mid]:
                end = mid-1
            else:
                start = mid+1
        else:
            if target < nums[mid]:
                start = mid+1
            else:
                end = mid-1

    return -1


if __name__ == '__main__':
    nums1 = [-1, 2, 4, 6, 7, 8, 12, 15, 19, 32, 45, 67, 99]
    nums2 = [99, 67, 45, 32, 19, 15, 12, 8, 7, 6, 4, 2, -1]
    target = -1
    print(search(nums1, target))
    print(search(nums2, target))