class Solution:

    def eatingSpeed(self, piles, speed):
        hour = 0
        for i in range(len(piles)):
            hour = hour + piles[i] // speed
            if piles[i] % speed != 0:
                hour += 1

        return hour

    def minEatingSpeed(self, piles, h):

        low = 1
        high = max(piles)
        res = -1

        while low <= high:
            mid = (low + high)// 2
            hour = self.eatingSpeed(piles, mid)
            if hour > h:
                low = mid + 1

            else:
                res = mid
                high = mid - 1

        return res

#------------------------main program--------------------
if __name__ == "__main__":
    sol = Solution()
    piles = [3,6,7,11]
    h = 8
    res = sol.minEatingSpeed(piles, h)
    print(res)



            