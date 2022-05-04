def alt_solution(main_array, sub_array):
    sub_index = 0
    for value in main_array:
        if sub_index == len(sub_array):
            return "Valid subsequence"
        if value == sub_array[sub_index]:
            sub_index += 1
    if sub_index == len(sub_array):
        return "Valid subsequence"
    else:
        return "Invalid subsequence"
