class MinHeap(object):
	def __init__(self,data):
		self.data = data
		self.size = len(data)
		self.__build()

	def minHeapfy(self,i,heapSize):
		lC = 2*i+1
		rC = lC+1
		minimal = i
		if lC<=heapSize and self.data[lC] < self.data[i]:
			minimal = lC
		if rC <=heapSize and self.data[rC] < self.data[minimal]:
			minimal=rC
		if minimal!=i:
			temp=self.data[i]
			self.data[i]=self.data[minimal]
			self.data[minimal]=temp
			self.minHeapfy(minimal,heapSize)

	def __build(self):
		for i in range(self.size // 2,-1,-1):
			self.minHeapfy(i,self.size-1)

	def extractMinimal(self):
		temp=self.data[0]
		self.data[0] = self.data[self.size-1]
		self.size -= 1
		self.minHeapfy(0,self.size-1)
		return temp

	def get(self,i):
		return self.data[i]
	def getPair(self,i):
		return self.data[i]

	def getSize(self):
		return self.size
	
	def __str__(self):
		r=[]
		for i in range(self.size):
			r.append(str(self.data[i]))
		return ",".join(r)

class MaxHeap(object):
	def __init__(self):
		self.data=[]
		self.__size=0

	def maxHeapfy(self,i,heapSize):
		lC = 2*i+1
		rC = lC+1
		largest = i
		if lC<=heapSize and self.data[lC]>self.data[i]:
			largest=lC
		if rC<=heapSize and self.data[rC]>self.data[largest]:
			largest=rC
		if largest!=i:
			temp = self.data[i]
			self.data[i]=self.data[largest]
			self.data[largest]=temp
			self.maxHeapfy(largest,heapSize)

	
	def __parentIndex(self,i):
		return i//2 if i & 1 == 1 else i//2-1

	def __incresekey(self,i,val):
		if self.data[i]>val:
			print('forbitdon')
			return
		self.data[i]=val
		parentI = self.__parentIndex(i)
		# i<0表示当前i已经是根了
		while i>0 and self.data[parentI]<self.data[i]:
			temp=self.data[parentI]
			self.data[parentI]=self.data[i]
			self.data[i]=temp
			i=parentI
			parentI=self.__parentIndex(i)

	def insert(self,val):
		self.data.append(float('-inf'))
		self.__incresekey(self.__size,val)
		self.__size += 1

	def getSize(self):
		return self.__size
	def get(self,i):
		return self.data[i]
	
	def getMax(self):
		return self.data[0]

	def __str__(self):
		r=[]
		for i in range(self.__size):
			r.append(str(self.data[i]))
		return ','.join(r)

class PairVal(object):
	def __init__(self,val,index):
		self.__val = val
		self.__index = index
	def getVal(self):
		return self.__val
	def setValIndex(self,val,index):
		self.__val = val
		self.__index = index
	def getIndex(self):
		return self.__index

class MinHeapVal(object):
	def __init__(self):
		self.data=[]
		self.__size=0
    
    # 处理不像python
	def minHeapfy(self,i,heapSize):
		lC = 2*i+1
		rC = lC+1
		largest = i
		if lC<=heapSize and self.data[lC].getVal()<self.data[i].getVal():
			largest=lC
		if rC<=heapSize and self.data[rC].getVal()<self.data[largest].getVal():
			largest=rC
		if largest!=i:
			temp = self.data[i]
			self.data[i]=self.data[largest]
			self.data[largest]=temp
			self.minHeapfy(largest,heapSize)

	
	def __parentIndex(self,i):
		return i//2 if i & 1 == 1 else i//2-1

	def __decresekey(self,i,val,j):
		if self.data[i].getVal()<val:
			return
		self.data[i].setValIndex(val,j)
		parentI = self.__parentIndex(i)
		# i<0表示当前i已经是根了
		while i>0 and self.data[parentI].getVal()>self.data[i].getVal():
			temp=self.data[parentI]
			self.data[parentI]=self.data[i]
			self.data[i]=temp
			i=parentI
			parentI=self.__parentIndex(i)

	def insert(self,val,index):
		if self.__size==len(self.data):
			self.data.append(PairVal(float('inf'),-1))
		else:
			self.data[self.__size].setValIndex(val,index)
		self.__decresekey(self.__size,val,index)
		self.__size += 1

	def getSize(self):
		return self.__size
	
	def extractMin(self):
		pair = self.data[0]
		self.data[0]=self.data[self.__size-1]
		self.data[self.__size-1]=pair
		self.__size -=1 
		self.minHeapfy(0,self.__size-1)
		return pair.getVal(),pair.getIndex()

	def getMin(self):
		return self.data[0].getVal(),self.data[0].getIndex()
	def get(self,i):
		return self.data[i].getVal()
		
	def __str__(self):
		r=[]
		for i in range(self.__size):
			r.append(str(self.data[i].getVal()))
		return ','.join(r)

class KthElement(object):
	"""获取最小堆中第k小的元素
	nlgn:首先构建最小堆 nlgn/2,排序耗时 nlgn 
	nlgk:遍历整个最小堆的数组，拿到一个数，然后将数构建成最大堆
	klgn:每次取k次最小元素就可以
	klgk:从原来的堆里面拿到最小的元素，然后放入新的最小堆，存储其在原有最小堆中的位置，然后找到其子再次插入，一直执行k次

	"""
	def __init__(self, data,k):
		super(KthElement, self).__init__()
		self.minHeap = MinHeap(data)
		self.k = k

	def nlgn(self):
		size = self.minHeap.getSize()
		for i in range(size-1,0,-1): #n
			temp=self.minHeap.data[i]
			self.minHeap.data[i]=self.minHeap.data[0]
			self.minHeap.data[0]=temp
			self.minHeap.minHeapfy(0,i-1) #lg(i)
		return self.minHeap.get(size-self.k)
	
	def klgn(self):
		for i in range(0,self.k): #k
			val = self.minHeap.extractMinimal() #lg(n-k)
		return val

	def nlgk(self):
		maxH = MaxHeap()
		size = self.minHeap.getSize()
		for i in range(size): #n
			val=self.minHeap.extractMinimal() #lg(n-k)
			if i<self.k :
				maxH.insert(val) #lg(k)
		return maxH.getMax()
	
	def klgk(self):
		minH = MinHeapVal()
		miHeapSize=self.minHeap.getSize()
		minH.insert(self.minHeap.get(0),0)#常量
		for i in range(1,self.k): #(k-1)
			data,index=minH.extractMin() #lg(i-1)
			lC = 2*index +1
			rC = lC+1
			if lC<miHeapSize:
				minH.insert(self.minHeap.get(lC),lC)#lgi
			if rC<miHeapSize:
				minH.insert(self.minHeap.get(rC),rC)#lg(i+1)
		return minH.getMin()[0]
			

	def __str__(self):
		return self.minHeap.__str__()

if __name__ == '__main__':
	
	def testMinHeap(data):
		minHeap = MinHeap(data)
		print(minHeap)
	
	def testMaxHeap():
		maxH = MaxHeap([])
		maxH.insert(9)
		maxH.insert(2)
		maxH.insert(4)
		maxH.insert(6)
		maxH.insert(8)
		maxH.insert(0)
		d=maxH.data
		print(maxH)
		for i in range(maxH.getSize()-1,0,-1):
			temp=d[i]
			d[i]=d[0]
			d[0]=temp
			maxH.maxHeapfy(0,i-1)
		print(maxH)
	def testnlgk(k):
		print("   nlgk")
		data=[9,2,4,6,8,0]
		data=[1, 2, 10, 3, 11, 12, 13, 4]
		print("origin data:",data)
		kth=KthElement(data,k)
		print(k,"'th smallest element ",kth.nlgk())
	def nlgnTest(k):
		print("   nlgn")
		data=[9,2,4,6,8,0]
		data=[1, 2, 10, 3, 11, 12, 13, 4]
		print("origin data:",data)
		kth=KthElement(data,k)
		print(k,"'th smallest element ",kth.nlgn())
	def klgnTest(k):
		print("   klgn")
		data=[9,2,4,6,8,0]
		data=[1, 2, 10, 3, 11, 12, 13, 4]
		print("origin data:",data)
		kth=KthElement(data,k)
		print(k,"'th smallest element ",kth.klgn())
	def testklgk(k):
		print("    klgk")
		data=[9,2,4,6,8,0]
		data=[1, 2, 10, 3, 11, 12, 13, 4]
		print("origin data:",data)
		kth=KthElement(data,k)
		print(k,"'th smallest element ",kth.klgk())

	# testMaxHeap()
	# testMinHeap()
	k=2
	nlgnTest(k)
	klgnTest(k)
	testnlgk(k)
	testklgk(k)

	

