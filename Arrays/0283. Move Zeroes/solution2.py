class Solution:
    def moveZeros(self, nums):

        l = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i] , nums[l] = nums[l], nums[i]
                l += 1

#---------------main program-------------------

if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,0,3,12]
    sol.moveZeros(nums)

    print(nums)