from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)

        result = [-1] * n  # Initialize the result array with -1

        st = []  # Stack to keep track of indices
        for i in range(n-2, -1, -1):
            st.append(nums[i])

        # Iterate through the array in reverse order to find the next greater elements
        for i in range(n-1, -1, -1):
            while st and st[-1] <= nums[i]:
                st.pop()  # Pop elements from the stack that are less than or equal to the current element
            if st:
                result[i] = st[-1]  # The next greater element is the top of the stack
            st.append(nums[i])  # Push the current element onto the stack

        return result


#-------------------------main Program--------------------
if __name__ == "__main__":  
    sol = Solution()
    nums = [1,2,3,4,3]
    result = sol.nextGreaterElements(nums)
    print(result)  # Output: [2, 3, 4, -1, 4]
