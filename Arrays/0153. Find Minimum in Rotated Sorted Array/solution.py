class Solution:
    def findMin(self, nums):

        n = len(nums)
        low = 0
        high = len(nums) - 1
        res = -1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] > nums[n -1]:
                low = mid +1

            else:
                res = mid
                high = mid - 1

        return nums[res]

#-----------------main Program----------------------
if __name__ == "__main__":
    sol = Solution()
    nums = [4,5,6,7,0,1,2]

    res = sol.findMin(nums)
    print(res)