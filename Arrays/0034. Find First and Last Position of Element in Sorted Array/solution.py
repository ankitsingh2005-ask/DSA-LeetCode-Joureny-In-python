class Solution:
    def searchRange(self, nums, target):

        # first index
        low = 0
        high = len(nums) - 1
        first = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1

            else:
                first = mid
                high = mid - 1

        #second index
        low = 0
        high = len(nums) - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
                
            elif nums[mid] > target:
                high = mid - 1
                
            else:
                last = mid
                low = mid + 1

        return [first, last]

#---------------main Program----------------

if __name__ == "__main__":
    sol = Solution()
    nums = [5,7,7,8,8,10] 
    target = 8
    res = sol.searchRange(nums, target)
    print(res)
        
                

