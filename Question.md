# [3011. Find if Array Can Be Sorted](https://leetcode.com/problems/find-if-array-can-be-sorted)

__Type:__ Medium <br>
__Topics:__ Array, Bit Manipulation, Sorting <br>
__Companies:__ Edelweiss Group
<hr>

You are given a __0-indexed__ array of __positive__ integers `nums`.

In one __operation__, you can swap any two __adjacent__ elements if they have the __same__ number of set bits (A set bit refers to a bit in the binary representation of a number that has a value of `1`). You are allowed to do this operation __any__ number of times __(including zero)__.

Return `true` _if you can sort the array, else return_ `false`.
<hr>

### Examples:

- __Example 1:__ <br>
__Input:__ nums = [8,4,2,30,15] <br>
__Output:__ true <br>
Explanation: Let's look at the binary representation of every element. The numbers 2, 4, and 8 have one set bit each with binary representation "10", "100", and "1000" respectively. The numbers 15 and 30 have four set bits each with binary representation "1111" and "11110".<br> 
We can sort the array using 4 operations: - Swap nums[0] with nums[1]. This operation is valid because 8 and 4 have one set bit each. The array becomes [4,8,2,30,15]. <br> - Swap nums[1] with nums[2]. This operation is valid because 8 and 2 have one set bit each. The array becomes [4,2,8,30,15]. <br> - Swap nums[0] with nums[1]. This operation is valid because 4 and 2 have one set bit each. The array becomes [2,4,8,30,15]. <br> - Swap nums[3] with nums[4]. This operation is valid because 30 and 15 have four set bits each. The array becomes [2,4,8,15,30]. <br>
The array has become sorted, hence we return true. <br>
Note that there may be other sequences of operations which also sort the array.

- __Example 2:__ <br>
__Input:__ nums = [1,2,3,4,5] <br>
__Output:__ true <br>
__Explanation:__ The array is already sorted, hence we return true.

- __Example 3:__ <br>
__Input:__ nums = [3,16,8,4,2] <br>
__Output:__ false <br>
__Explanation:__ It can be shown that it is not possible to sort the input array using any number of operations.
<hr>

### Constraints:
- `1 <= nums.length <= 100`
- <code>1 <= nums[i] <= 2<sup>8</sup></code>

### Hints:
- Split the array into segments. Each segment contains consecutive elements with the same number of set bits.
- From left to right, the previous segment’s largest element should be smaller than the current segment’s smallest element.