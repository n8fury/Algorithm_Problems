# Two Numbers

## <u><i><b>Problem Statement</b></i></u>

The problem is Two numbers Sum.
In the problem an Array and an integer will be given.

```
[3,5,-4,8,9,1,2,11,-1],10
```

The given integer represents a sum which we have find combining two numbers from the given Array.
Meaning, if we take 11 and -1 and add them we'll get 10,the desired sum.

## <u><i><b>Solution #1</b></i></u>

We can take two for loops. run them through the array, iterate through each integer and keep adding them until we find our desired sum.

As we have to run Two for loops, time complexity for this solution will be O(n<sup>2</sup>).

## <u><i><b>Solution #2</b></i></u>

Another way to solve this problem is to sort the array first. Because no data is given whether the array is sorted or not, we can use any sorting algorithms such as merge sort, quick sort, heap sort, etcetera.

After the array is sorted, we can use two pointers, one at the beginning of the array and one at the end of the array. We can add the pointer integer. As we know, the array is sorted; if the summation of two pointed integers is greater than our desired sum, we can move the pointer at the end to one position to the left.

And if the summation of two pointed integers is less than our desired sum, we can move the pointer at the beginning to one position to the right.

The time complexity of these sorting algorithms is O(n log(n)). After the sorted array, we have to iterate through the array once. Therefore, we can have the pair of numbers in O(n)time.

And as we have not used any extra space, space complexity will be O(1).

## <u><i><b>Solution #3</b></i></u>

A better way to solve this problem would be to throw a hashtable into the problem. As we know
we can search through the hashtable for a number in constant time. As our desired sum is already given,we can iterate through the array and check if the difference between the current number and the desired sum is in the hashtable. If it is present then we have  our pair and can return them. But if not,we can pass the current number to the hashtable.This way, we have to iterate through the array only once.

Of course, it would mean extra space but our program will run faster than solution#1.

As we have iterate through the array only once, time complexity for this solution will be O(n).

And as we are only adding values to the hashtable, space complexity also will be O(n).
