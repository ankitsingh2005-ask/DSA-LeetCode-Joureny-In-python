from collections import deque

class Solution:
    def removeDuplicates(self, s: str) -> str:

        st = []

        res = []

        # Iterate through the string and use a stack to remove adjacent duplicates
        for i in range(len(s)):
            # If the stack is empty, push the current character onto the stack
            if not st:
                st.append(s[i])
                continue

            # If the current character is the same as the top of the stack, pop the top of the stack (remove the duplicate)
            if st[-1] == s[i]:
                st.pop()
                continue
            st.append(s[i])

        # Pop all the characters from the stack and append them to the result list
        while st:
            res.append(st.pop())

        # Reverse the result list to get the final string and return it
        res.reverse()
        return ''.join(res)

#-------------------------main Program--------------------
if __name__ == "__main__":
    sol = Solution()
    s = "abbaca"
    res = sol.removeDuplicates(s)
    print(res)

