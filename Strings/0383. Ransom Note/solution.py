class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        have = {}  # Dictionary to store the frequency of characters in the magazine
        need = {}  # Dictionary to store the frequency of characters needed for the ransom note

        for char in magazine:
            have[char] = have.get(char, 0) + 1  # Increment the frequency count for the character in the magazine

        for char in ransomNote:
            need[char] = need.get(char, 0) + 1  # Increment the frequency count for the character needed in the ransom note

        return self.fun(have, need)  # Call the helper function to check if the ransom note can be constructed

    def fun(self, have: dict, need: dict) -> bool:
        for c ,fneed in need.items():
            if have.get(c, 0) < fneed:  # Check if the magazine has enough of the character needed for the ransom note
                return False  # Return False if the magazine does not have enough characters
        return True  # Return True if the ransom note can be constructed    

#-------------------------main Program--------------------
if __name__ == "__main__":
    sol = Solution()
    ransomNote = "aa"
    magazine = "aab"
    result = sol.canConstruct(ransomNote, magazine)
    print(result)  # Output: True