class Solution:
    def prevSmallerElement(self, arr):
        # result array to store the previous smaller elements
        res = [-1] * len(arr)

        # stack to keep track of the previous smaller elements
        stack = []
        stack.append(arr[0])

        # iterate through the array starting from the second element
        for i in range(1, len(arr)):

            # pop element from the stack until we find a smaller element or the stack is empty
            while stack and stack[-1] >= arr[i]:
                stack.pop()

            # if the stack is not empty, the top element is the previous smaller element
            if not stack:
                res[i] = -1
            else:
                res[i] = stack[-1]

            # push the current element onto the stack
            stack.append(arr[i])

        return res

#-------------------------main Program--------------------
if __name__ == "__main__":  
    sol = Solution()
    arr = [1, 5, 0, 3, 4, 5]
    res = sol.prevSmallerElement(arr)
    print(res)