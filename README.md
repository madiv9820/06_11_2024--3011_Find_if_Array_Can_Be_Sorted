- ## Approach 1:- Bubble Sort 

    - ### **Intuition**
        The problem involves sorting an array of integers under the constraint that two adjacent elements can only be swapped if they have the same number of `1` bits (set bits) in their binary representation. The challenge is to determine if it is possible to sort the array given this restriction.

        - The core idea is to use a **modified bubble sort** approach, where we repeatedly compare adjacent elements and swap them if:
        1. The elements are out of order (i.e., the current element is greater than the next element).
        2. They have the **same number of `1` bits** in their binary representation.
        
        - If two elements have different numbers of `1` bits, they cannot be swapped, and the sorting is not possible under the given constraints.

        - The problem boils down to checking if the array can be sorted using a bubble sort-like approach, but with a specific restriction on which pairs of elements can be swapped.

    - ### **Approach**
        1. **Bubble Sort Simulation**:
            - We simulate **bubble sort**, where we compare adjacent elements in the array.
            - If the current element is greater than the next one, we attempt to swap them, but only if they have the same number of `1` bits in their binary representation.
            - If any adjacent elements have different numbers of `1` bits, we immediately return `false` since we can't swap them.

        2. **Counting 1-bits**:
            - For each comparison, we need to determine if two elements have the same number of `1` bits in their binary representation. This can be done efficiently by counting the number of `1` bits in each element’s binary form.
        
        3. **Optimizing with Early Termination**:
            - If, during a full pass through the array, no swaps occur, it means the array is already sorted. We can break out of the loop early, improving performance in already sorted arrays.
        
        4. **Final Result**:
            - If we can successfully sort the array with the given condition (only swapping elements with the same number of `1` bits), return `true`.
            - If any swap is blocked because the `1` bit counts differ, return `false`.

    - ### **Time Complexity**
        - **Outer Loop (Bubble Sort)**: The outer loop of the algorithm simulates bubble sort and runs up to `n` times, where `n` is the number of elements in the array.
        
        - **Inner Loop**: The inner loop compares adjacent elements for each pass of the outer loop. In the worst case, it runs `(n - 1)` times in the first pass, `(n - 2)` times in the second pass, and so on.

        - **Counting 1-bits**: For each comparison, we need to calculate the number of `1` bits in the binary representation of each element. Counting bits can be done in constant time, __O(1)__, since the number of bits is fixed (32 or 64 bits for standard integer types).

        Thus, the time complexity is dominated by the nested loops: __O(n<sup>2</sup>)__, where `n` is the number of elements in the array.

    - ### **Space Complexity**
        - **Input Array Copy**: We create a copy of the input array to avoid modifying the original. This requires __O(n)__ space, where `n` is the number of elements.

        - **Auxiliary Space for Counting Bits**: The auxiliary space used for counting bits is constant, __O(1)__, since we use a fixed-size bitset or simple binary operations to count the bits of each number.

        Thus, the overall space complexity is: __O(n)__ due to the space required to store the copied array.

    - ### Code
        - **Python Solution**

            ```python3 []
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
            ```
        
        - **C++ Solution**
            
            ```C++ []
            class Solution {
                private:
                    // Helper function to count the number of 1-bits (set bits) in the binary representation of a number.
                    int countBits(int val) {
                        return bitset<32>(val).count();  // Use bitset to count the number of set bits (1s) in val.
                    }

                public:
                    bool canSortArray(vector<int>& nums) {
                        int n = nums.size();  // Length of the input array 'nums'
                        vector<int> arr = nums;  // Make a copy of the original array to work with

                        // Traverse the array from the beginning, simulating a bubble sort.
                        for (int currentIndex = 0; currentIndex < n; ++currentIndex) {
                            bool isAlreadySorted = true;  // Flag to check if the array is already sorted at this point.
                            
                            // Perform a modified bubble sort where we compare adjacent elements.
                            for (int i = 0; i < n - 1 - currentIndex; ++i) {  
                                // If the current element is greater than the next element, we need to swap them.
                                if (arr[i] > arr[i + 1]) {
                                    // But we can only swap if both numbers have the same number of 1-bits in their binary form.
                                    if (countBits(arr[i]) == countBits(arr[i + 1])) {
                                        swap(arr[i], arr[i + 1]);  // Swap the elements
                                        isAlreadySorted = false;  // Since we swapped, the array is not sorted yet.
                                    } else {
                                        // If they have different numbers of 1-bits, we cannot swap them, so return false.
                                        return false;
                                    }
                                }
                            }
                            
                            // If no swaps were made in this iteration, the array is already sorted.
                            if (isAlreadySorted) {
                                break;
                            }
                        }

                        return true;  // If we successfully sorted the array (or determined it can be sorted), return true.
                    }
            };
            ```