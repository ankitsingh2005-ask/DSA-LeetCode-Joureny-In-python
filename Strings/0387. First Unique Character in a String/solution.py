class solution:
    def firstUniqChar(self, s: str) -> int:

        freq = {}  # Dictionary to store the frequency of each character

        for char in s:
            freq[char] = freq.get(char, 0) + 1  # Increment the frequency count for the character

        for i, char in enumerate(s):
            if freq[char] == 1:  # Check if the character is unique (frequency is 1)
                return i  # Return the index of the first unique character
        return -1  # Return -1 if there are no unique characters

#-------------------------main Program--------------------
if __name__ == "__main__":
    sol = solution()
    s = "leetcode"
    result = sol.firstUniqChar(s)
    print(result)  # Output: 0