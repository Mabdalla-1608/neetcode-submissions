class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sortedStrs = ''.join(sorted(s))
            if not(sortedStrs in res.keys()):
                res[sortedStrs] = [s]
            else:
                res[sortedStrs].append(s)

        return list(res.values())