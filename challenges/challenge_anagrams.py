def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left_half = string[:mid]
    right_half = string[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    sorted_string = "".join(merged)

    return sorted_string


def is_anagram(first_string, second_string):
    sorted_first_string = merge_sort(first_string.lower())
    sorted_second_string = merge_sort(second_string.lower())

    if len(sorted_first_string) == 0 and len(sorted_second_string) == 0:
        return sorted_first_string, sorted_second_string, False

    elif sorted_first_string == sorted_second_string:
        return sorted_first_string, sorted_second_string, True

    else:
        return sorted_first_string, sorted_second_string, False
