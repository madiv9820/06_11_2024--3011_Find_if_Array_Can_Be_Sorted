from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # Helper function to count the number of 1-bits (set bits) in the binary representation of a number.
        def count_Bits(val):
            return bin(val).count('1')
        
        n = len(nums)  # Length of the input array 'nums'
        arr = nums.copy()  # Make a copy of the original array to work with
        
        # Traverse the array from the beginning, simulating a bubble sort.
        for current_index in range(n):
            is_already_sorted = True  # Flag to check if the array is already sorted at this point.
            
            # Perform a modified bubble sort where we compare adjacent elements.
            for index in range(n - 1 - current_index):  
                # If the current element is greater than the next element, we need to swap them.
                if arr[index] > arr[index + 1]:
                    # But we can only swap if both numbers have the same number of 1-bits in their binary form.
                    if count_Bits(arr[index]) == count_Bits(arr[index + 1]):
                        arr[index], arr[index + 1] = arr[index + 1], arr[index]  # Swap the elements
                        is_already_sorted = False  # Since we swapped, the array is not sorted yet.
                    else:
                        # If they have different numbers of 1-bits, we cannot swap them, so return False.
                        return False
            
            # If no swaps were made in this iteration, the array is already sorted.
            if is_already_sorted:
                break
        
        return True  # If we successfully sorted the array (or determined it can be sorted), return True.