class Solution(object):

    def binarySearch(self, nums, target, leftBias):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Initialize pointers for binary search
        left = 0
        right = len(nums) - 1

        # Initialize the index to -1, which will be returned if the target is not found
        i = -1

        # Perform binary search to find the target in the sorted array
        while left <= right:

            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1

            elif target < nums[mid]:
                right = mid - 1

            else:
                i = mid

                if leftBias:
                    right = mid - 1      # Search on the left
                else:
                    left = mid + 1       # Search on the right

        return i

    # Find the first and last positions of the target in the sorted array
    def searchRange(self, nums, target):

        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)

        return [left, right]
    
# Example usage
if __name__ == "__main__":
    solution = Solution()

    nums = [5, 7, 7, 8, 8, 10]
    target = 8

    result = solution.searchRange(nums, target)

    print("The first and last positions of the target are:", result)