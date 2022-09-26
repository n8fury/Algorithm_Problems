def validate_subsequence(main_array, sub_array):
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


        
A = [0, 1, 5, 6, 8, 9, -1, -4, -7]
B = [6, 8, 9, -1, -4, -8]

print(validate_subsequence(A, B))