from typing import List

class Solution:
    def moveZero(self, nums: list[int]) ->int:

        i = 0
        l = 0

        while l < len(nums):
            if nums[l] == 0:
                l += 1
            else:
                nums[l], nums[i] = nums[i], nums[l]
                i += 1
                l += 1

#------------------main program-----------------

if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,0,3,12]

    res = sol.moveZero(nums)
    print(nums)
