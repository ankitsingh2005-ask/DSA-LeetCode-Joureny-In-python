class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from typing import List
import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # Count frequency of each task
        freq = Counter(tasks)

        # Python heap is a min-heap,
        # so store negative frequencies to make it a max-heap
        pq = []

        for count in freq.values():
            heapq.heappush(pq, -count)

        # Stores tasks waiting for their cooldown
        # (available_time, remaining_frequency)
        q = deque()

        time = 0

        while pq or q:

            time += 1

            # Put tasks whose cooldown is over back into heap
            if q and q[0][0] == time:
                available_time, count = q.popleft()
                heapq.heappush(pq, count)

            # Execute the most frequent available task
            if pq:
                count = heapq.heappop(pq)

                # One occurrence completed
                count += 1

                # If task still has occurrences,
                # it becomes available after n intervals
                if count != 0:
                    q.append((time + n + 1, count))

        return time

#------------main program------------------------
sol = Solution()
tasks = ["A","A","A","B","B","B"]
n = 2

res = sol.leastInterval(tasks, n)

print(res)