class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ""
        order_sort = {}
        for i,index in enumerate(indices):
            order_sort[index] = s[i]
        
        for i in range(len(indices)):
            res += order_sort[i]
        
        return res
                