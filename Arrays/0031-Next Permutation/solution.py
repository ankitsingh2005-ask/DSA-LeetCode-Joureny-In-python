class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # Find the first decreasing element from the right
        i = len(nums) - 2
        
        # Move leftwards to find the first element that is smaller than its next element
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # If such an element is found, find the next larger element to swap with
        if i >= 0:

            j = len(nums) - 1

            # Find the largest element to the right of i that is greater than nums[i]
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # Swap the found elements
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the elements to the right of i to get the next permutation
        nums[i + 1:] = reversed(nums[i + 1:])

        return nums
    
# Example usage
if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3]
    result = solution.nextPermutation(nums)
    print("Next permutation:", result)  # Output: [1, 3, 2]

    nums = [3, 2, 1]
    result = solution.nextPermutation(nums)
    print("Next permutation:", result)  # Output: [1, 2, 3]

    nums = [1, 6, 5]
    result = solution.nextPermutation(nums)
    print("Next permutation:", result)  # Output: [1, 5, 6]
        