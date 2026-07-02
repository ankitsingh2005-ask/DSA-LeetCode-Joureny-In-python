class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        # Iterate through the sorted list of numbers
        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            # Use two pointers to find the triplets that sum up to zero
            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total > 0:
                    right -= 1

                elif total < 0:
                    left += 1

                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    
                    # Skip duplicates for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()

    nums = [-1, 0, 1, 2, -1, -4]

    result = solution.threeSum(nums)

    print("The unique triplets that sum up to zero are:", result)


        