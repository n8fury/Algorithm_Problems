# Validate Subsequence

## <u><i><b>Problem Statement </b></i></u>

The problem is Validating subsequences.
We can call a sequence, a subsequence if it is a subset of another sequence and derived by deleting some of the members of the main sequence but keeping the order.

```
A = [0,1,5,6,8,9,-1,-4,-7]
B = [6,8,9,-1,-7]
```

We can see that B is array which is formed by deleting some of the members of A but the order is maintained. So, we can say that, B is a subsequence of A.

In the problem two non empty arrays will be given. we have to find out if the second array is a subsequence of the first array or not.

## <u><i><b>Solution#1</b></i></u>

To solve this problem we'll be using two pointers. one in the main array and one in the subsequence array. First, we'll find the first element of the subsequence array and it's index in the main array. After that, we'll traverse through the main array for the next element and so on , until we reach the end of the subsequence array. We'll start traversing from the index of the first element of the subsequence array because to find and validate the subsequence, order is important.

Time complexity of this solution will be O(n). Here n is the length of the main array. It will be O(n) because we have to traverse through the main array only and once.In some cases, the main will not be fully traversed because the subsequence will be found early or order will be violated.

Space complexity of this solution will be O(1),because we are not using any extra space.

## <u><i><b>Short Summary</b></i></u>

| Solution | Solution Description |Time Complexity | Space Complexity |
| :---: | :---: | :---: | :---: |
|Solution#1|Using two pointer. One in the main array, another in the subsequent array |O(n)|O(1)
