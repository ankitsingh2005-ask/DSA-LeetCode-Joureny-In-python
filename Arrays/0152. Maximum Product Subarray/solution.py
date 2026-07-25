from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> List:

        max_end = nums[0]
        min_end = nums[0]
        res = nums[0]

        # loop to iterate on nums 1 to n
        for i in range(1, len(nums)):
            v1 = nums[i]
            v2 = max_end * nums[i]
            v3 = min_end * nums[i]

            max_end = max(v1, max(v2,v3))
            min_end = min(v1, min(v2, v3))

            res = max(res, max(max_end, min_end))

        return res

#-------------------main program-----------------
if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,-2,4]

    res = sol.maxProduct(nums)
    print(nums)
    print(res)

