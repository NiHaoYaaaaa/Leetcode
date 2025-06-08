class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        candidates = []
        for u, v in edges:
            if v in parent:
                candidates.append([parent[v], v])
                candidates.append([u, v])
                break
            parent[v] = u
    
        def find(x):
            while uf[x] != x:
                uf[x] = uf[uf[x]]
                x = uf[x]
            return x
    
        def union(x, y):
            xr, yr = find(x), find(y)
            if xr == yr:
                return False  
            uf[yr] = xr
            return True
    
        if candidates:
            for edge in reversed(candidates):
                uf = list(range(len(edges) + 1))
                valid = True
                for u, v in edges:
                    if [u, v] == edge:
                        continue  
                    if not union(u, v):
                        valid = False
                        break
                if valid:
                    return edge
    
        uf = list(range(len(edges) + 1))
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        