class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the numbers and their indices
        num_map = {}
        # Iterate through the list of numbers
        for i in range(len(nums)):
            comple = target - nums[i]
            # Check if the complement exists in the dictionary
            if comple in num_map:
                return [num_map[comple], i]
            # If the complement does not exist, add the current number and its index to the dictionary
            num_map[nums[i]] = i