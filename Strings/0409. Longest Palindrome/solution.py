class Solution:
    def longestPalindrome(self, s: str) -> int:

        f = {}  # Dictionary to store the frequency of each character
        for char in s:
            f[char] = f.get(char, 0) + 1  # Increment the frequency count for the character

        odd = False  # Flag to indicate if there is an odd frequency character
        ans = 0  # Variable to store the length of the longest palindrome
        for freq in f.values():
            if freq % 2 == 0:  # If the frequency is even
                ans += freq  # Add the entire frequency to the answer
            else:
                odd = True  # Set the odd flag to True
                ans += freq - 1  # Add the largest even number less than the frequency to the answer

        if odd:  # If there was an odd frequency character
            ans += 1  # Add 1 to the answer to account for the center character of the palindrome
        return ans  # Return the length of the longest palindrome   

#-------------------------main Program--------------------
if __name__ == "__main__":  
    sol = Solution()
    s = "abccccdd"
    result = sol.longestPalindrome(s)
    print(result)  # Output: 7
