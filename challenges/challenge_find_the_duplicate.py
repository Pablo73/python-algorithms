def find_duplicate(nums):
    if len(nums) <= 1 or not (isinstance(nums[0], int)) or nums[0] < 0:
        return False
    first_number = nums[0]

    for value in nums[1:]:
        if not (isinstance(value, int)) or value < 0:
            return False
        elif first_number == value:
            return value

    return find_duplicate(nums[1:])
