from typing import Tuple

from numpy import stack

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        n = len(s)
        stack = []  # Stack to keep track of characters and their counts

        for c in s:

            # If the stack is empty or the top character is different from the current character, push the current character with a count of 1 onto the stack
            if not stack or stack[-1][0] != c:
                stack.append((c, 1))
            else:
                ch, count = stack.pop()
                count += 1
                # If the count is less than k, push the character and its updated count back onto the stack
                if count < k:
                    stack.append((ch, count))

        # Reconstruct the string from the stack
        result = []
        for char, count in stack:
            result.append(char * count)  # Append the character multiplied by its count
        return ''.join(result)  # Join the list of characters to form the final string

#-------------------------main Program--------------------
if __name__ == "__main__":  
    sol = Solution()
    s = "deeedbbcccbdaa"
    k = 3   
    result = sol.removeDuplicates(s, k)
    print(result)  # Output: "aa"
            

