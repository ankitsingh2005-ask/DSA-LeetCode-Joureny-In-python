from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        
        res = 0
        sum_ = 0

        freq = {}
        freq[0] = 1

        for i in range(len(nums)):
            sum_ += nums[i]
            rem = sum_ % k
            if rem < 0:
                rem += k

            res += freq.get(rem,0)

            freq[rem] = freq.get(rem, 0) + 1

        return res 

#------------------main program---------------------------

if __name__ == "__main__":
    sol = Solution()
    nums = [4,5,0,-2,-3,1]
    k = 5       

    res = sol.subarraysDivByK(nums, k)
    print(res)