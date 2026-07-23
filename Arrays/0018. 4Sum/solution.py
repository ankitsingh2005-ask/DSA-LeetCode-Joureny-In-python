from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        nums.sort()
        res = []


        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    sum_n = nums[i] + nums[j] + nums[left] + nums[right]
                            
                    if sum_n == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                                
                        left += 1
                        right -= 1

                        # skip the duplicate left 
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # skip the duplicate of right
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                            
                    # check if the sum is lessthen the target
                    elif sum_n < target:
                        left += 1

                    # else
                    else:
                        right -= 1

        
        return res

#--------------------main Program-------------------
if __name__ == "__main__":
    solution = Solution()
    nums = [1,0,-1,0,-2,2]
    target = 0

    res = solution.fourSum(nums,target)
    print(res)
                            

     



            
            

        