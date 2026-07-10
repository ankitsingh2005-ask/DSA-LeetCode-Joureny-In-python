from typing import List

class Solution(object):
    def sortedSquares(self, nums: List[int]) -> List[int]:

        siz = len(nums)
        neg = []
        pos = []

        # seperate negative positive element 
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        #Case1 no negative number 
        if len(neg) == 0:
            return [x * x for x in pos]
        
        #Case2 no positive number 
        if len(pos) == 0:
            res = [x * x for x in neg]
            res.reverse()
            return res
        
        #Case3 both Exist 
        neg = [x * x for x in neg][::-1]
        pos = [x * x for x in pos]
        n,m = len(neg), len(pos)

        res = []

        i = j = 0

        while i < n and j < m:
            if neg[i] < pos[j]:
                res.append(neg[i])
                i += 1
            else:
                res.append(pos[j])
                j += 1

        while i < n:
            res.append(neg[i])
            i += 1

        while j < m:
            res.append(pos[j])
            j += 1

        return res
    
#------Main Porgram-------
if __name__ == "__main__":
    solution = Solution()
    nums = [-14-4,-1,0,3,10]

    result = solution.sortedSquares(nums)
    print(result) 