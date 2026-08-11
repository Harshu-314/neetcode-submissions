class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for char in nums:
            freq[char]=freq.get(char,0)+1
        arr=[]
        for char,count in freq.items():
            arr.append([count,char])
            arr.sort()
        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
         
        