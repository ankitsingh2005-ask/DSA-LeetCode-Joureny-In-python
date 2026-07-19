from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""
        
        # Frequency array for ASCII charactor 

        freq = [0] * 128

        for ch in t:
            freq[ord(ch)] += 1

        left = 0
        right = 0
        required = len(t)
        min_len = float("inf")
        start = 0

        while right < len(s):
            r = s[right]
            
            if freq[ord(r)] > 0:
                required -= 1

            freq[ord(r)] -= 1
            right += 1

            while required == 0:
                if right - left < min_len:
                    min_len = right - left 
                    start = left

                l = s[left]

                freq[ord(l)] += 1

                if freq[ord(l)] > 0:
                    required += 1

                left += 1


        return "" if min_len == float("inf") else s[start:start + min_len]
    


#--------------main program-------------------------------------------------------

if __name__ == "__main__":
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"

    result = solution.minWindow(s, t)

    print(result)
