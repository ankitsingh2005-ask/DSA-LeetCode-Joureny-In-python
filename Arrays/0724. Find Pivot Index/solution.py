from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) ->int:

        left = 0
        total = sum(nums)
    
        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i


            left += nums[i]
        return -1

#--------------main program----------------------

if __name__ == "__main__":
    sol = Solution()
    nums = [1,7,3,6,5,6]
    res = sol.pivotIndex(nums)

    print(res)


