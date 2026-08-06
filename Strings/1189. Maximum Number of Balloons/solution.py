class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Create a dictionary to count the frequency of each character in the input text
        have = {}
        for char in text:
            have[char] = have.get(char, 0) + 1

        need = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}  # Dictionary representing the required characters and their counts for the word "balloon"
        # Calculate the maximum number of times the word "balloon" can be formed
        result = float('inf')  # Initialize result to infinity
        for c, fneed in need.items():
            fhave = have.get(c, 0)  # Get the frequency of the required character in the input text
            times = fhave // fneed  # Calculate how many times the required character can be used to form "balloon"
            result = min(result, times)  # Update the result with the minimum value


        return result  # Return the maximum number of times the word "balloon" can be formed

#-------------------------main Program--------------------
if __name__ == "__main__":  
    sol = Solution()
    text = "loonbalxballpoon"
    result = sol.maxNumberOfBalloons(text)
    print(result)  # Output: 2