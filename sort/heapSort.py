import sys
class HeapSort(object):
	"""核心思想:
	构建堆
		维持堆的特性，以最大堆来讲,左右子节点都要比父节点要小，所以先找到当前节点的子节点最大的下标，如果当前节点不是最大的，则交换
		，对交换过的节点再次循环以防堆结构被破坏【被替换节点数】
	"""
	def __init__(self, toSortFile):
		super(HeapSort, self).__init__()
		self.tsf = toSortFile

	def loadData(self,fileName):
		try:
			f=open(fileName)
			lines = f.readlines()
			data = []
			for line in lines:
				nums = line.replace('\n','').split(',')
				data.extend([int(num) for num in nums])
			return data
		except Exception as e:
			print(e)
	
	def maxHeapify(self,i,data,heapSize):
		lChild = 2*i+1
		rChild = lChild+1
		largeIndex = i
		if lChild <= heapSize and data[lChild] > data[i] :
			largeIndex = lChild
		if rChild <= heapSize and data[rChild] > data[largeIndex]:
			largeIndex = rChild
		if largeIndex != i:
			temp = data[i]
			data[i]=data[largeIndex]
			data[largeIndex]=temp
			self.maxHeapify(largeIndex,data,heapSize)

	def sort(self,data):
		for i in range(len(data)-1,0,-1):
			temp=data[0]
			data[0]=data[i]
			data[i]=temp
			self.maxHeapify(0,data,i-1)

	def buildMaxHeap(self,data):
		length=len(data)
		# python3 语法，-1不会输出
		for i in range(length//2,-1,-1):
			self.maxHeapify(i,data,length-1)

	def maxHeap(self):
		data = self.loadData(self.tsf)
		# 1构建堆
		self.buildMaxHeap(data)
		# 2排序
		self.sort(data)
		print(data)

	def minHeapify(self,i,data,heapSize):
		lChild = 2*i+1
		rChild = lChild+1
		minIndex = i
		if lChild<=heapSize and data[lChild] < data[minIndex]:
			minIndex = lChild
		if rChild <= heapSize and data[rChild] < data[minIndex]:
			minIndex = rChild
		if  i!=minIndex:
			temp=data[i]
			data[i] = data[minIndex]
			data[minIndex]=temp
			self.minHeapify(minIndex,data,heapSize)


	def buildMinHeap(self,data):
		for i in range(len(data)//2,-1,-1):
			self.minHeapify(i,data,len(data)-1)

	def minHeap(self):
		data = self.loadData(self.tsf)
		self.buildMinHeap(data)
		self.rSort(data)
		print(data)

	def rSort(self,data):
		for i in range(len(data)-1,0,-1):
			temp = data[i]
			data[i] = data[0]
			data[0]=temp
			self.minHeapify(0,data,i-1)

if __name__ == '__main__':
	import profile
	largeSize = False
	if len(sys.argv) == 2:
		tsf = sys.argv[1]
	elif largeSize:
		tsf="../txtFile/sortData_50000.txt"
	else:
		tsf="../txtFile/sortData_5.txt"
	heapSort = HeapSort(tsf)
	profile.run("heapSort.maxHeap()")

#          764872 function calls (77092 primitive calls) in 3.386 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    3.385    3.385 :0(exec)
#       500    0.001    0.000    0.001    0.000 :0(extend)
#         2    0.000    0.000    0.000    0.000 :0(len)
#         1    0.000    0.000    0.000    0.000 :0(nl_langinfo)
#         1    0.000    0.000    0.000    0.000 :0(open)
#         1    0.008    0.008    0.008    0.008 :0(print)
#         1    0.001    0.001    0.001    0.001 :0(readlines)
#       500    0.001    0.000    0.001    0.000 :0(replace)
#         1    0.001    0.001    0.001    0.001 :0(setprofile)
#       500    0.003    0.000    0.003    0.000 :0(split)
#        37    0.000    0.000    0.000    0.000 :0(utf_8_decode)
#         1    0.002    0.002    3.385    3.385 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 _bootlocale.py:23(getpreferredencoding)
#         1    0.000    0.000    0.000    0.000 codecs.py:257(__init__)
#         1    0.000    0.000    0.000    0.000 codecs.py:306(__init__)
#        37    0.000    0.000    0.000    0.000 codecs.py:316(decode)
#       500    0.013    0.000    0.013    0.000 heapSort.py:15(<listcomp>)
# 762781/75001    3.185    0.000    3.185    0.000 heapSort.py:20(maxHeapify)
#         1    0.116    0.116    3.079    3.079 heapSort.py:34(sort)
#         1    0.052    0.052    0.273    0.273 heapSort.py:41(buildMaxHeap)
#         1    0.000    0.000    3.383    3.383 heapSort.py:47(maxHeap)
#         1    0.004    0.004    0.022    0.022 heapSort.py:8(loadData)
#         1    0.000    0.000    3.386    3.386 profile:0(heapSort.maxHeap())
#         0    0.000             0.000          profile:0(profiler)

#          789251 function calls (102093 primitive calls) in 3.331 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    3.330    3.330 :0(exec)
#       500    0.001    0.000    0.001    0.000 :0(extend)
#     25003    0.027    0.000    0.027    0.000 :0(len)
#         1    0.000    0.000    0.000    0.000 :0(nl_langinfo)
#         1    0.000    0.000    0.000    0.000 :0(open)
#         1    0.008    0.008    0.008    0.008 :0(print)
#         1    0.001    0.001    0.001    0.001 :0(readlines)
#       500    0.001    0.000    0.001    0.000 :0(replace)
#         1    0.001    0.001    0.001    0.001 :0(setprofile)
#       500    0.003    0.000    0.003    0.000 :0(split)
#        37    0.000    0.000    0.000    0.000 :0(utf_8_decode)
#         1    0.001    0.001    3.330    3.330 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 _bootlocale.py:23(getpreferredencoding)
#         1    0.000    0.000    0.000    0.000 codecs.py:257(__init__)
#         1    0.000    0.000    0.000    0.000 codecs.py:306(__init__)
#        37    0.000    0.000    0.000    0.000 codecs.py:316(decode)
#       500    0.013    0.000    0.013    0.000 heapSort.py:15(<listcomp>)
# 762159/75001    3.080    0.000    3.080    0.000 heapSort.py:55(minHeapify)
#         1    0.080    0.080    0.329    0.329 heapSort.py:70(buildMinHeap)
#         1    0.000    0.000    3.329    3.329 heapSort.py:74(minHeap)
#         1    0.004    0.004    0.023    0.023 heapSort.py:8(loadData)
#         1    0.112    0.112    2.969    2.969 heapSort.py:80(rSort)
#         1    0.000    0.000    3.331    3.331 profile:0(heapSort.minHeap())
#         0    0.000             0.000          profile:0(profiler)