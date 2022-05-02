def solution_1(array, num):
    for i in range(len(array)-1):
        first_num = array[i]
        for j in range(i+1, len(array)):
            second_num = array[j]
            if first_num + second_num == num:
                return [first_num, second_num]
    return "No two numbers add up to the target number"

# Time complexity: O(n^2)|| space complexity: O(1)

a = [-4,5,9,15,2,1,6,4,8,11]
b = 17
print(solution_1(a,b))