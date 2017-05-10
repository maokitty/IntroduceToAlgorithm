class DoubleHash(object):
	"""docstring for DoubleHash
    核心思想：用数组实现hash,计算h(k,1),h(k,2),...,h(k,m-1),分配到不同的数组位置上
    采用 h(k,i)=(h1(k)+ih2(k)) mod m,h1(k) = k mod m;h2(k) = 1+(k mod m') ,取m是质数,m'=m-1
    search time 1/(1-alpha) alpha=n/m
    这里文件读入最多有 50001个数,取 alpha = 3/4 也就是最终需要66669【n/alpha +1】的空间，每次查找的最多次数是 4次[出现hash冲突，不同值]
    选择m是质数，那么依次倒推，选择的质数按照顺序存放在一张表里面,依次拿,不用计算质数
	"""
	def __init__(self,primeFile):
		super(DoubleHash, self).__init__()
		try:
			f=open(primeFile)
			lines = f.readlines()
			self.ms=[]
			for line in lines:
				self.ms.extend([int(line)])
		except Exception as e:
			print(e)
			raise e
		self.size = 0
		self.m = self.ms[0]
		self.mp=self.m-1
		self.alpha= 0.75
		self.dh = [ None for i in range(self.m)]
		self.maxTry = 1/(1-self.alpha)
		self.resizeCnt=0


	def __hash(self,k,i):
		return (k % self.m +i*(1+k % self.mp))%self.m

	def __getm(self):
		return self.ms[self.resizeCnt]
	
	def put(self,value):
		if self.size!=0 and  self.size / self.m -self.alpha > 0 :
			self.__resize()
		i=0
		# 如果求坐标的次数超过了原有数据的大小（size），那么，size+1一定会插入成功
		while i<=self.size+1:
			index=self.__hash(value,i)
			if self.dh[index] is None  or self.__isDelete(self.dh[index]) :
				self.dh[index] = value
				self.size += 1
				return index
			else:
				i=i+1
		
		return None

	def search(self,value):
		i=0
		while i<self.size:
			index=self.__hash(value,i)
			if self.dh[index] == value :
				return  True,index
			else:
				i=i+1
		return False,None

	def __isDelete(self,value):
		'''目前用的都是数字，使用空串作为删除标记'''
		return value is ''

	def __setDelete(self,index):
		self.dh[index] = ''

	def delete(self,value):
		i=0
		while i<self.size:
			index=self.__hash(value,i)
			if self.dh[index] == value :
				self.__setDelete(index)
				self.size-=1
				return  True,index
			else:
				i=i+1
		return False,None

	def printData(self):
		print("size ",self.size," self.m ",self.m)
		i=0
		for data in self.dh:
			if data is not None and not self.__isDelete(data):
				if (i==0 or i%30 !=0 ) and i!=self.size-1:
					print(data,end=",")
				else:
					print(data)
				i=i+1

	def printAll(self):
		print("size ",self.size," self.m ",self.m)
		i=0
		dLen=len(self.dh)
		for data in self.dh:
			if (i==0 or i%30 !=0 ) and i!=dLen-1:
				print(data,end=",")
			else:
				print(data)
			i=i+1


	def __resize(self):
		self.resizeCnt+=1
		self.m = self.__getm()
		self.mp = self.m-1
		tempDh = [None for i in range(self.m)]
		for d in self.dh:
			if d is None or  self.__isDelete(d):
				continue
			i=0
			while True:
				index=self.__hash(d,i)
				if tempDh[index] is None :
					tempDh[index] = d
					break
				else:
					i=i+1
		self.dh=tempDh
		tempDh=None
	
	def totalNum(self):
		return self.size

def getDoubleHashPrime():
	num = 66669 # 50001 / alpha +1
	allprime=[]
	try:
		f=open("./txtFile/primeIn70000.txt")
		datas = f.readlines()
		allprime.extend([int(num) for num in datas[0].split(',') ])
	except Exception as e:
		print(e)
		raise e
	prime=[]
	i = num
	# T(n) < T(3n/4)+O(n) 
	# 看看有没有更好的办法
	while i>13:
		j = i
		k=1
		while j not in allprime:
			if j&1 == 0:
				j+=1
			j+=2*k
			k+=1
		prime.extend([j])
		i = int(i*0.75)
	prime.reverse()
	for i in prime :
		print(i)


if __name__ == '__main__':
	largeFile = False
	if largeFile:
		file="./txtFile/sortData_50000.txt"
	else:
		file="./txtFile/sortData_5.txt"
	primeFile = "./txtFile/doubleHashPrime.txt"
	try:
		f=open(file)
		lines = f.readlines()
		data=[]
		for line in lines:
			nums = line.replace('\n','').split(',')
			data.extend([ int(num) for num in nums])
	except Exception as e:
		print(e)
		raise e
	dh = DoubleHash(primeFile)
	print(len(data))
	for d in data:
		dh.put(d)
	dh.printAll()
	def searchDeleteTest(value):
		find,index=dh.search(value)
		if find:
			print(index)
		else:
			print(value," not exist")
		while find:
			delete,dIndex=dh.delete(value)
			print("delete ",delete," dIndex",dIndex)
			find,index=dh.search(value)
		find,index=dh.search(value)
		if find:
			print(index)
		else:
			print(value, " not exist")
		print(dh.totalNum())
	searchDeleteTest(6)

	# getDoubleHashPrime()

