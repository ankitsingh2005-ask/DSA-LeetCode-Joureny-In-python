class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 0

        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1   

        return i
        

    # Example usage

if __name__ == "__main__":
    solution = Solution()

    nums = [3,2,2,3] 

    val = 3

    result = solution.removeElement(nums, val)
    print(result)