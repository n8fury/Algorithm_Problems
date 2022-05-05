def two_numbers(array, sum):
    hashmap = {}  # declared hashmap as a python dictionary
    for num in array:
        if sum - num in hashmap:
            return [sum-num, num]
        else:
            hashmap[num] = True

    return "No two numbers add up to the target number"

# Time complexity: O(n)|| space complexity: O(n)


a = [-4, 5, 9, 15, 2, 1, 6, 4, 8, 11]
b = 17
print(two_numbers(a, b))
