class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:

            # Find next charactor in s
            skipS = 0
            while i >= 0:
                if s[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break

            # find next charactor in t
            skipT = 0
            while j >= 0:
                if t[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else: 
                    break

            # champair both s and t
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False

            elif i >= 0 or j >= 0:
                return False

            i -= 1
            j -= 1

        return True

#---------------Main Program-----------------

if __name__ == "__main__":
    sol = Solution()
    s = "ab#c" 
    t = "ad#c"

    res = sol.backspaceCompare(s,t)
    print(res)