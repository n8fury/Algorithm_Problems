def validate_subsequence(main_array, sub_array):
    main_index = 0
    sub_index = 0
    while main_index < len(main_array) and sub_index < len(sub_array):
        if sub_array[sub_index] == main_array[main_index]:
            sub_index += 1
        main_index += 1
    if sub_index == len(sub_array):
        return "Valid subsequence"
    else:
        return "Invalid subsequence"

# Time complexity: O(n)|| space complexity: O(1)


A = [0, 1, 5, 6, 8, 9, -1, -4, -7]
B = [6, 8, 9, -1, -4, -8]

print(validate_subsequence(A, B))
