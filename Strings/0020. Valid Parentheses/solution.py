class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Iterate through the string and use a stack to check for valid parentheses
        for char in s:
            # if the character is an opening bracket, push it onto the stack
            if char in ['(', '{', '[']:
                stack.append(char)
            # if the character is a closing bracket, check if it matches the top of the stack
            elif char in [')', '}', ']']:
                if not stack:
                    return False
                top = stack.pop()
                if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                    return False

        # If the stack is empty, all the parentheses are valid
        return not stack

#-------------------------main Program--------------------
if __name__ == "__main__":
    sol = Solution()
    s = "()[]{}"
    res = sol.isValid(s)
    print(res)