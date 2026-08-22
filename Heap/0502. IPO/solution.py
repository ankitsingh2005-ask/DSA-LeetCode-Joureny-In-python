import heapq
from typing import List

class Solution:
    def findMaximizedCapital(
        self,
        k: int,
        w: int,
        profits: List[int],
        capital: List[int]
    ) -> int:

        n = len(profits)

        projects = []

        for i in range(n):
            projects.append((capital[i], profits[i]))

        projects.sort()

        pq = []
        i = 0

        while k > 0:

            # Add all projects we can currently afford
            while i < n and projects[i][0] <= w:
                profit = projects[i][1]
                heapq.heappush(pq, -profit)
                i += 1

            # No affordable project
            if not pq:
                return w

            # Select maximum profit
            w += -heapq.heappop(pq)

            k -= 1

        return w

#--------------main program------------------------

sol = Solution()

k = 3
w = 0
profits = [1,2,3]
capital = [0,1,2]

res = sol.findMaximizedCapital(k, w, profits, capital)

print(res)