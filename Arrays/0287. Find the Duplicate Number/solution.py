from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = fast = 0
        while True:

            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if slow == fast:
                slow = 0

                while slow != fast:
                    slow = nums[slow]  # to find the starting point
                    fast = nums[fast]

                return slow

        return 0

#----------------main program------------------------

if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,4,2,2]

    res = solution.findDuplicate(nums)
    print(res)  