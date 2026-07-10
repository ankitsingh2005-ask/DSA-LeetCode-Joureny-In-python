class Solution(object):
    def removeDuplicates(self, nums):

        i = 0
        res = 1
        j = 1

        # while j is lessthen length of nums
        while j < len(nums):

            # check if the number is same of their perivious then increment the j to +1 and continue
            if nums[j] == nums[j - 1]:
                j += 1
                continue
            
            # find the unique then swape the number to the i + 1 position 
            nums[i + 1] = nums[j]

            # increment the i 
            i += 1

            # incement the result if the unique number 
            res += 1

            # increment the j to check the unique number 
            j += 1

        # at the end return all the unique number
        return res
    
# Example usage

if __name__ == "__main__":
    solution = Solution()

    nums = [1,1,1,2,2,3,3,4]
    result = solution.removeDuplicates(nums)
    print(result)
    print(nums[:result])