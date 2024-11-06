#include <vector>
#include <bitset>
#include <algorithm>
#include <climits>
#include <iostream>
using namespace std;

class Solution {
    private:
        // Helper function to count the number of 1-bits (set bits) in the binary representation of a number.
        int countBits(int val) {
            // Use bitset to count the number of set bits (1s) in val.
            return bitset<32>(val).count();  // bitset<32> creates a fixed-size bitset for 32-bit integers.
        }
    public:

        bool canSortArray(vector<int>& nums) {
            // Initialize variables:
            int current_min = nums[0];  // current minimum number in the segment
            int current_max = nums[0];  // current maximum number in the segment
            
            int previous_max = INT_MIN;  // previous maximum number from the last segment, initialized to negative infinity
            
            // Iterate over each number in the list
            for (int num : nums) {
                // If the current number has the same number of 1-bits as the current_min
                if (countBits(num) == countBits(current_min)) {
                    // Update current_min to the smallest number and current_max to the largest number in the current segment.
                    current_min = min(current_min, num);
                    current_max = max(current_max, num);
                } else {
                    // If we've reached a new segment (the number of 1-bits is different):
                    // Check if the current minimum is still greater than the previous maximum.
                    // If not, return false because we can't swap to sort the array.
                    if (current_min < previous_max) {
                        return false;
                    }

                    // Update the previous_max to the current_max (end of the previous segment)
                    previous_max = current_max;
                    
                    // Start a new segment with the current number as the new current_min and current_max
                    current_min = num;
                    current_max = num;
                }
            }

            // After processing all numbers, ensure the last segment can be placed after the previous one.
            return current_min > previous_max;
        }
};

int main() {
    vector<int> nums; int input; Solution sol;
    cin >> input;

    while(input != -1) {
        nums.emplace_back(input);
        cin >> input;
    }

    cout << ((sol.canSortArray(nums = nums)) ? "true": "false") << endl;
}