from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = max(nums)
        res = 0

        # Create a frequencyCount array to store the frequency of each value in nums
        frequency_count = [0] * (n + max_val + 1)

        # Populate frequencyCount array with the frequency of each value in nums
        for val in nums:
            frequency_count[val] += 1

        # Iterate over the frequencyCount array to make all values unique
        for i in range(len(frequency_count)):
            # If there is at most one occurrence, move to the next element
            if frequency_count[i] <= 1:
                continue

            # Calculate the excess occurrences of the current value
            duplicates = frequency_count[i] - 1

            # Carry over the excess occurrences to the next value
            frequency_count[i + 1] += duplicates

            # Ensure the current value has only one occurrence
            frequency_count[i] = 1

            # Increment res to account for the carry over
            res += duplicates

        # Return the total number of moves required
        return res
