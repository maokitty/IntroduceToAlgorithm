#https://leetcode.com/problems/find-peak-element/?tab=Description
# A peak element is an element that is greater than its neighbors.
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that num[-1] = num[n] = -∞.
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
class Peek(object):
	def findPeakElement(self,nums):
		numsLen = len(nums)
		if numsLen <= 1 :
			return 1
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




if __name__ == '__main__':
	peek = Peek();
	index=peek.findPeakElement([1,2])
	print(index)