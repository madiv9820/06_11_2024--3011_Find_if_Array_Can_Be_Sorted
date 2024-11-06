#include <vector>
#include <bitset>
#include <algorithm>
#include <iostream>
using namespace std;

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

int main() {
    vector<int> nums; int input; Solution sol;
    cin >> input;

    while(input != -1) {
        nums.emplace_back(input);
        cin >> input;
    }

    cout << ((sol.canSortArray(nums = nums)) ? "true": "false") << endl;
}