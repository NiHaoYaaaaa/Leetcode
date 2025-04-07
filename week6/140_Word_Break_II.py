class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        str_set = set(wordDict)

        def backtrack(current, tmp, remaining):
            if not remaining:
                if current:
                    current = current[:-1]
                    ans.append(current)
                return
            
            length = len(remaining)
            for i in range(length):
                tmp += remaining[i]
                if tmp in str_set:
                    backtrack(current + tmp + " ", "", remaining[i+1:])
        
        backtrack("", "", s)
        return ans