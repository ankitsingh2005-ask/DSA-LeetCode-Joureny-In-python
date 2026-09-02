class Solution:
    def sumOfDigits(self, n):
        if n == 0:
            return 0

        return n % 10 + self.sumOfDigits(n // 10)

#-------------main function to run the code----------------
if __name__ == "__main__":
    sol = Solution()
    n = 12345

    res = sol.sumOfDigits(n)
    print(res)