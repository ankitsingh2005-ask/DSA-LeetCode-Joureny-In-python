class Solution:
    def dailyTemperatures(self, temperatures):

        n = len(temperatures)

        # result array to store the number of days until a warmer temperature
        res = [0] * n

        # stack to keep track of the indices of the temperatures
        st = [n-1]

        for i in range(n-2, -1, -1):
            # pop elements from the stack until we find a warmer temperature or the stack is empty
            while st and temperatures[st[-1]] <= temperatures[i]:
                st.pop()

            # if the stack is not empty, the top element is the index of the next warmer temperature
            if st:
                res[i] = st[-1] - i

            # push the current index onto the stack
            st.append(i)

        return res

#-------------------------main Program--------------------
if __name__ == "__main__":
    sol = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    res = sol.dailyTemperatures(temperatures)
    print(res)