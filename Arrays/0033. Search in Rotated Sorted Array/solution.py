class Solution:
    def search(self, nums, target):

        n = len(nums)
        low = 0 
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            #part one
            elif nums[mid] > nums[n -1]:
                if nums[mid] < target:
                    low = mid + 1
                    
                else:
                    if nums[0] > target:
                        low = mid + 1
                    else:
                        high = mid -1
                continue

            #part two
            if nums[mid] > target:
                high = mid -1

            else:
                if nums[n-1] < target:
                    high = mid -1

                else:
                    low = mid + 1

        return -1

#----------------main program----------------------
if __name__ == "__main__":
    sol = Solution()
    nums = [4,5,6,7,0,1,2] 
    target = 1
    res = sol.search(nums, target)
    print(res)