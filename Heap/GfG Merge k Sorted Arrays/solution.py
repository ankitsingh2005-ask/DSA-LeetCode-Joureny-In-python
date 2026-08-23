import heapq

class Node:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row 
        self.col = col
        
    def __lt__(self, other):
        return self.value < other.value


class Solution:
    def mergeArrays(self, mat):
        # code here
        
        n = len(mat)
        
        pq = []
        
        for i in range(n):
            if len(mat[i]) > 0:
                pq.append(Node(mat[i][0], i, 0))
                
        
        heapq.heapify(pq)
        
        res = []
        
        while pq:
            node = heapq.heappop(pq)
            value = node.value
            row = node.row
            col = node.col
            
            res.append(value)
            
            if col < len(mat[row]) -1:
                next_node = Node(
                    mat[row][col + 1],
                    row,
                    col + 1
                    )
                    
                heapq.heappush(pq, next_node)
                
        return res

#-----------------MAIN PROGRAM-------------------

sol = Solution()

mat = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]

res = sol.mergeArrays(mat)

print(res)