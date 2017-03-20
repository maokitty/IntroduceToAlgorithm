import sys
class PriorityQueue(object):
	"""docstring for PriorityQueue"""
	def __init__(self, f):
		super(PriorityQueue, self).__init__()
		self.f = f
		self.data=self.loadData()
		self.buildMaxHeap(self.data)

	def loadData(self):
	 	try:
	 		f=open(self.f)
	 		lines=f.readlines()
	 		data=[]
	 		for line in lines:
	 			lineArr = line.replace('\n','').split(',')
	 			data.extend([int(num) for num in lineArr])
	 		return data
	 	except Exception as e:
	 		raise e

	def  maxHeapify(self,data,i):
		lChild = 2*i+1
		rChild = lChild+1
		largestIndex = i
		if lChild<=self.heapSize and data[lChild] > data[largestIndex]:
			largestIndex = lChild
		if rChild <= self.heapSize and data[rChild] > data[largestIndex]:
			largestIndex = rChild
		if largestIndex!=i:
			temp=data[i]
			data[i]=data[largestIndex]
			data[largestIndex]=temp
			self.maxHeapify(data,largestIndex)
			
	def buildMaxHeap(self,data):
		self.heapSize = len(data)-1
		for i in range(len(data)//2 ,-1,-1):
			self.maxHeapify(data,i)

	def heapExtractMax(self,data):
		if self.heapSize<1:
			print("error")
			return None
		maxD=data[0]
		data[0]=data[self.heapSize]
		self.heapSize -= 1
		self.maxHeapify(data,0)
		return maxD

	def parentIndex(self,i):
		# python3 语法，左子树一定是奇数，右子树一定是偶数
		return i//2 if i%2!=0 else i//2-1

	def heapIncreaseKey(self,data,i,key):
		if key<data[i]:
			print("new key can not smaller than original key")
			return None
		data[i]=key
		pI=self.parentIndex(i)
		while  i>0 and data[pI] < data[i]:
			temp=data[pI]
			data[pI]=data[i]
			data[i]=temp
			i=pI
			pI=self.parentIndex(i)

	def maxHeapInsert(self,data,key):
		self.heapSize += 1
		data.append(float('-inf'))
		self.heapIncreaseKey(data,self.heapSize,key)	

		
	def heapMaximum(self,data):
		return data[0]


if __name__ == '__main__':
	if len(sys.argv) == 2:
		f=sys.argv[1]
	else:
		f="txtFile/sortData_5.txt"
	pq=PriorityQueue(f)
	print(pq.heapMaximum(pq.data))
	pq.heapIncreaseKey(pq.data,4,200)
	print(pq.data)
	pq.maxHeapInsert(pq.data,150)
	print(pq.data)



