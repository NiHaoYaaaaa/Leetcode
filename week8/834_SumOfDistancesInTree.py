from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        res = [0] * n
        count = [1] * n

        def postorder(node, parent):
            for child in tree[node]:
                if child != parent:
                    postorder(child, node)
                    count[node] += count[child]
                    res[node] += res[child] + count[child]

        def preorder(node, parent):
            for child in tree[node]:
                if child != parent:
                    res[child] = res[node] - count[child] + (n - count[child])
                    preorder(child, node)

        postorder(0, -1)
        preorder(0, -1)
        return res