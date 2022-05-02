def solution_2(array, sum):
    array.sort()  # uses time sort. Time complexity O(n log(n))
    left_flag = 0
    right_flag = len(array) - 1
    while left_flag < right_flag:  # when the two flag are identical
        if array[left_flag] + array[right_flag] == sum:
            return [array[left_flag], array[right_flag]]
        elif array[left_flag]+array[right_flag] > sum:
            right_flag -= 1
        elif array[left_flag]+array[right_flag] < sum:
            left_flag += 1
    return "No two numbers add up to the target number"

# Time complexity: O(n log(n))|| space complexity: O(1)

a = [-4, 5, 9, 15, 2, 1, 6, 4, 8, 11]
b = 17
print(solution_2(a, b))
