from typing import List

class Solution:
    def totalFruits(self, fruits: List[int]) -> int:

        low = 0
        freq = {}
        max_sum = 0

        for high in range(len(fruits)):
            fruit = fruits[high]
            freq[fruit] = freq.get(fruit, 0) + 1

            while len(freq) > 2:
                freq[fruits[low]] -= 1

                if freq[fruits[low]] == 0:
                    del freq[fruits[low]]

                low += 1
               
            
            max_sum = max(max_sum, high - low + 1)

        return max_sum
    

#-------------main program-----------------
if __name__ == "__main__":
    solution = Solution()

    fruits = [1,2,3,2,2]

    result = solution.totalFruits(fruits)
    print(result)
            
