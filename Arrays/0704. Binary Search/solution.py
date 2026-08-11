class Solution:

    def binarySearch(self, nums, target):

        low = 0
        high = len(nums) -1

        #check for the condition where high is not less then or equal to low
        while low <= high:

            guess = (low + high) // 2

            if nums[guess] == target:
                return guess

            elif nums[guess] <= target:
                low = guess + 1

            else:
                high = guess - 1

        return -1

#-----------------main program-----------------------

if __name__ == "__main__":
    sol = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9

    res = sol.binarySearch(nums, target)

    print(res)
