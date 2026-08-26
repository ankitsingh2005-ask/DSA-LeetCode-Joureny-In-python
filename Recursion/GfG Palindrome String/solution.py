class Solution:
    def isPallindrome(self, s, low, high):

        if low >= high:
            return True

        if s[low] != s[high]:
            return False

        return self.isPallindrome(s, low + 1, high - 1)


if __name__ == "__main__":
    sol = Solution()
    s = "abba"

    res = sol.isPallindrome(s, 0, len(s) - 1)
    print(res)