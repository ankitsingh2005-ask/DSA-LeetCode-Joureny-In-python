from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        best_ending = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            v1 = best_ending + nums[i]
            v2 = nums[i]
            best_ending = max(v1,v2)

            ans = max(ans, best_ending)

        return ans


#----------main program-----------------------

if __name__ == "__main__":
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = sol.maxSubArray(nums)
    print(nums)
    print(res)
