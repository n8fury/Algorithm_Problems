def sorted_squared_array(array):
    squared = [0 for _ in array]
    right_flag = 0
    left_flag = len(array) - 1

    for i in reversed(range(len(array))):
        right_value = array[right_flag]
        left_value = array[left_flag]
        if abs(right_value) > abs(left_value):
            squared[i] = right_value ** 2
            right_flag += 1
        else:
            squared[i] = left_value ** 2
            left_flag -= 1

    return squared

# Time complexity: O(n) || Space complexity: O(n)

A = [-1, -2, -3, 4, 5, 6]
print(sorted_squared_array(A))
