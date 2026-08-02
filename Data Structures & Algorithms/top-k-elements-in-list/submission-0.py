class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
        

        pairs=list(freq.items())

        pairs.sort(key=lambda x:x[1] ,reverse=True)
        a=[]
        for i in range(k):
            a.append(pairs[i][0])
        return a



        