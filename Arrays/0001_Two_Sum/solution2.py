class Solution(object):
    #function to return the target
    def twoSum(self, nums, target):

        nums.sort()

        # two pointer to itrate on the nums
         
        i = 0
        j = len(nums) -1

        #while i is less then j 
        while i < j:
            
            sum = nums[i] + nums[j]

                #check it the i + j == target then return i and j
            if sum == target:
                return [i,j]
            
            # it the sum is less then target then increment the i to +1
            elif sum < target:
                i += 1
            
            # if the sum is greter then sum then decriment the j to -1
            else:
                j -= 1

# Example usage 

if __name__ == "__main__":
    solution = Solution()

    nums = [3,2,4]
    target = 6

    #function calling 
    result = solution.twoSum(nums, target)
    print(result)

