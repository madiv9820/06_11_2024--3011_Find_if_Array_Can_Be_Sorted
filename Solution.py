from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # Helper function to count the number of 1-bits (set bits) in the binary representation of a number.
        def count_Bits(val):
            # Convert the number to binary and count the number of '1's in its binary representation.
            return bin(val).count('1')
        
        # Initialize variables:
        # 'current_min' tracks the current smallest number with the same number of 1-bits.
        # 'current_max' tracks the largest number with the same number of 1-bits.
        current_min, current_max = nums[0], nums[0]
        
        # 'previous_max' keeps track of the maximum number encountered in the previous segment with the same number of 1-bits.
        previous_max = float('-inf')  # Set to negative infinity initially to ensure the first segment passes the comparison.

        # Iterate over each number in the list
        for num in nums:
            # If the current number has the same number of 1-bits as the current minimum number in the segment
            if count_Bits(num) == count_Bits(current_min):
                # Update 'current_min' to the smallest number and 'current_max' to the largest number in the current segment.
                current_min = min(current_min, num)
                current_max = max(current_max, num)
            else:
                # If we've reached a new segment (i.e., the number of 1-bits is different)
                # Check if the current minimum is still greater than the previous maximum.
                # If not, the array cannot be sorted under the given condition, so return False.
                if current_min < previous_max:
                    return False

                # Update 'previous_max' to the current maximum (end of the previous segment)
                previous_max = current_max
                
                # Start a new segment with the current number as the new 'current_min' and 'current_max'
                current_min, current_max = num, num
        
        # After processing all numbers, the last segment should have 'current_min' greater than 'previous_max'.
        return current_min > previous_max