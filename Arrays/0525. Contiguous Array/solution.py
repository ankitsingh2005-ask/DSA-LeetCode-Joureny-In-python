from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) ->int:

        zero = 0
        one = 0
        res = 0
        vector = {}

        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                one += 1

            diff = zero - one

            if diff == 0:
                res = max(res, i + 1)
                continue

            elif diff not in vector:
                vector[diff] = i

            else:
                idx = vector[diff]
                len_ = i - idx
                res = max(len_, res)

        return res 
#----------------main program----------------------

if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,1,1,1,1,0,0,0]
    #nums = [0,1]
    res = sol.findMaxLength(nums)
    print(res)

