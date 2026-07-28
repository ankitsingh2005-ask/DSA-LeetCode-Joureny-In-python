from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_ = 0
        count = 0
        fre = {}
        fre[0] =  1

        for i in range(len(nums)):
            sum_ += nums[i]

            ques = sum_ - k

            count +=  fre.get(ques, 0)

            fre[sum_] = fre.get(sum_, 0) + 1

        return count

#--------------mian program-------------------------

if __name__ == "__main__":
    sol = Solution()

    nums = [1,2,3]
    k = 3

    res = sol.subarraySum(nums, k)

    print(res)
        