from typing import List

class Solution:
    def maxAbsSum(self, nums: List[int]) ->int:

        max_s = nums[0]
        min_s = nums[0]
        res = abs(nums[0])

        for i in range(1, len(nums)):

            max_s = max(nums[i], max_s + nums[i])
            min_s = min(nums[i], min_s + nums[i])

            res = max(res, max_s, abs(min_s) )

        return res

#-------------main program----------------

if __name__ == "__main__":
    sol = Solution()
    nums = [2,-5,1,-4,3,-2]

    result = sol.maxAbsSum(nums)
    print(result)


