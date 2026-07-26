from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        total = sum(nums)

        curr_max = best_max = nums[0]
        curr_min = best_min = nums[0]

        res = nums[0]

        # loop to iterate in the array nums 
        for i in range(1, len(nums)):

            # Maximum Sum Subarray 
            curr_max = max(nums[i], curr_max + nums[i])
            best_max = max(best_max, curr_max)

            # Minimum Sum Subarray 
            curr_min = min(nums[i], curr_min + nums[i])
            best_min = min(best_min, curr_min)

        # All the element is 0
        if best_max < 0:
            return best_max

        res = max(res, best_max, total - best_min)

        return res

#-------------main Program-------------------------

if __name__ == "__main__":
    sol = Solution()
    nums = [1,-2,3,-2]
    result = sol.maxSubarraySumCircular(nums)
    print(nums)
    print(result)



