class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups={}
        for s in strs:
            w=sorted(s)
            key="".join(w)
            if key not in groups:

                groups[key]=[]

            groups[key].append(s)

        return list(groups.values())
