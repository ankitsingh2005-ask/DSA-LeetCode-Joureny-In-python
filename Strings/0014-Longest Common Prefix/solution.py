class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""

        # If the input list is empty, return an empty string
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result
    
    # Example usage
if __name__ == "__main__":  
    
    solution = Solution()

    strs = ["flower", "flow", "flight"]
    result = solution.longestCommonPrefix(strs)
    print("Longest common prefix:", result)  # Output: "fl"

        