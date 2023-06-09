def find_duplicate(nums):
    nums.sort()
    if not (isinstance(nums[0], int)) or nums[0] < 0:
            return False

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]

    return False

