def sorted_squared_array(array):
    squared = [0 for _ in array]
    for index in range(len(array)):
        squared[index] = array[index]**2

    squared.sort()
    return squared

# Time complexity: O(n log(n)) || Space complexity: O(n)


A = [-1, -2, -3, 4, 5, 6]
print(sorted_squared_array(A))
