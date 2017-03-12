#https://leetcode.com/problems/find-peak-element/?tab=Description
# A peak element is an element that is greater than its neighbors.
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that num[-1] = num[n] = -∞.
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
class Peek(object):
	def findPeakElement1(self,nums):
		numsLen = len(nums)
		if numsLen <= 1 :
			return 0
		for index,num in enumerate(nums):
			peek=num
			if index>0:
				if index<numsLen-1:
					if(peek > nums[index-1] and peek > nums[index+1]):
						return index
				else:
					if num>nums[index-1]:
						return index
			elif peek > nums[index+1]:
				return index
	
	def findPeakElement1Optimization(self,nums):
		for i in range(1,len(nums)):
			if nums[i] < nums[i-1]:
				return i-1
		return len(nums)-1

	def findPeakElement2Optimization(self,nums):
		return self.findOptimization(0,len(nums)-1,nums)

	def findOptimization(self,start,end,nums):
		if start == end :
			return start
		midNum = (int)((start+end)/2)
		midNumNext = midNum+1
		if nums[midNumNext] < nums[midNum]:
			return self.findOptimization(start,midNum,nums)
		else:
			return self.findOptimization(midNumNext,end,nums)



	def findPeakElement2(self,nums):
		numsLen = len(nums)
		if numsLen <= 1 :
			return 0
		return self.find(0,numsLen,nums)

	def find(self,start,end,nums):
		if start==end:
			return start
		index = (int)((start+end)/2)
		midNum = nums[index]
		if index > start:
			if index < end-1 :
				if midNum > nums[index-1] and midNum > nums[index+1]:
					return index
				elif midNum > nums[index-1]:
					return self.find(index,end,nums)
				else:
					return self.find(0,index+1,nums)
			elif  midNum>nums[index-1]:
					return index
			else:
				return index-1;
		elif midNum>nums[index+1]:
			return index
		else:
			return index+1;

if __name__ == '__main__':
	peek = Peek();
	index=peek.findPeakElement2Optimization([1,2,3,1])
	print(index)