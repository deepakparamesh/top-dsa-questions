class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) +1)]
        rank = [1] * (len(edges)+1)
        
        def find(n):
            p = parent[n]
            
            while p != parent[p]:
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1, p2= find(n1), find(n2)
            
            if p1 == p2:
                return True
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return False
    
        for node1, node2 in edges:
            if union(node1, node2):
                return [node1, node2]
            