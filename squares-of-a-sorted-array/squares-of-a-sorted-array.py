class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    	#Get size of range
        n=len(nums) 
        
        for i in range(n):
            nums[i] = (nums[i] **2) #square each index value
        nums.sort() #apply sort to list
        return nums
