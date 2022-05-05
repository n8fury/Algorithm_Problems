# Sorted Squared Array

## <u><i><b>Problem Statement</b></i></u>

The problem is to generate a sorted array of squares of all the numbers of a given array.

```
Input:[1,2,3,4,5] Output:[1,4,9,16,25]

Input:[-1,-2,-3,-4,-5] Output:[1,4,9,16,25]
```

In the problem a non-empty array will be provided.

## <u><i><b>Solution#1</b></i></u>

The first solution we can think of is to produce an array of squares of all the numbers of the given array and sort them. We can not sort the array first and produce the squares because of the possibility of having negative numbers in the array. Because we all know, square of a negative number is a positive number. Therefor, we have to produce an squared array and sort it.

Time complexity of this solution will be O(n log(n)). because we have use some sort of sorting algorithm. we are going to use time sort, which is default in python.

Space complexity of this solution will be O(n),n being the length of the given array, because we have to create the sorted array.

## <u><i><b>Solution#2</b></i></u>

Let's Assume the array given is sorted. We can use two pointers, one at the beginning of the array and one at the end of the array. We can compare the modulus of the two pointer integers. if the integer at the is bigger, the squared value of the integer will be placed at the end of output array, and the pointer will be moved to one position to the left. If the integer at the beginning is bigger, it's squared value will be placed at the end of the output array and the pointer will be moved to one position to the right. The comparison will go on until two pointer point same integer.

This solution will only work for already sorted array.
Time complexity for this solution will be O(n). because we have traverse through the array only once.
Space complexity for this solution will be O(n),n being the length of the given array, because we have to create the sorted array.