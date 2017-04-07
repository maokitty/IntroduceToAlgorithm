class Radix(object):
	"""docstring for Radix
    核心思想:依次比较数字最高位
	"""
	def __init__(self,toSortFile,maxDigit):
		super(Radix, self).__init__()
		self.maxDigit=maxDigit
		try:
			f = open(toSortFile)
			lines = f.readlines()
			# self.__strData(lines)
			self.__intData(lines)
		except Exception as e:
			print(e)
			raise e
	def __strData(self,lines):
		self.data=[]
		for line in lines:
			nums = line.replace('\n','').split(',')
			self.data.extend([num for num in nums])
	def __intData(self,lines):
		self.data=[]
		for line in lines:
			nums = line.replace('\n','').split(',')
			self.data.extend([int(num) for num in nums])


	def significantDigit(self,n,value):
		"""
		获取value的第n位有效数字,从右往左依次是1,2,3,...,len(str(value))
		"""
		vLen = len(value)
		return 0 if n>vLen else value[vLen-n]

	def significantIntDigit(self,n,value):
		"""
		处理10进制
		int类型直接使用,与str相比不需要len
		"""
		return(value // 10 **(n-1))%10


	
	def __countSort(self,n,b=10):
		"""b代表进制，比如10进制，说明，最大数字是10"""
		L=[[] for i in range(b)]
		for x in range(len(self.data)):
			v=self.data[x]
			# vn = int(self.significantDigit(n,v))
			vn=self.significantIntDigit(n,v)
			L[vn].append(self.data[x])
		self.data=[]
		for i in range(b):
			self.data.extend(L[i])
			
	def sort(self):
		for i in range(1,self.maxDigit+1):
			self.__countSort(i)
		# 这里还是字串
		print(self.data)



if __name__ == '__main__':
    import profile
    largeSize = True
    if largeSize:
    	toSortFile="../txtFile/sortData_50000.txt"
    	maxDigit=5
    else:
    	toSortFile="../txtFile/sortData_5.txt"
    	maxDigit=3
    radix = Radix(toSortFile,maxDigit)
    profile.run("radix.sort()")
   #       500081 function calls in 1.388 seconds

   # Ordered by: standard name

   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   # 250005    0.315    0.000    0.315    0.000 :0(append)
   #      1    0.000    0.000    1.387    1.387 :0(exec)
   #     50    0.002    0.000    0.002    0.000 :0(extend)
   #      5    0.000    0.000    0.000    0.000 :0(len)
   #      1    0.006    0.006    0.006    0.006 :0(print)
   #      1    0.001    0.001    0.001    0.001 :0(setprofile)
   #      1    0.000    0.000    1.387    1.387 <string>:1(<module>)
   # 250005    0.356    0.000    0.356    0.000 RadixSort.py:35(significantIntDigit)
   #      5    0.707    0.141    1.380    0.276 RadixSort.py:43(__countSort)
   #      5    0.000    0.000    0.000    0.000 RadixSort.py:45(<listcomp>)
   #      1    0.001    0.001    1.387    1.387 RadixSort.py:55(sort)
   #      0    0.000             0.000          profile:0(profiler)
   #      1    0.000    0.000    1.388    1.388 profile:0(radix.sort())

   #    str  750086 function calls in 2.088 seconds

   # Ordered by: standard name

   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   # 250005    0.330    0.000    0.330    0.000 :0(append)
   #      1    0.000    0.000    2.087    2.087 :0(exec)
   #     50    0.003    0.000    0.003    0.000 :0(extend)
   # 250010    0.281    0.000    0.281    0.000 :0(len)
   #      1    0.007    0.007    0.007    0.007 :0(print)
   #      1    0.001    0.001    0.001    0.001 :0(setprofile)
   #      1    0.000    0.000    2.087    2.087 <string>:1(<module>)
   # 250005    0.598    0.000    0.879    0.000 RadixSort.py:19(significantDigit)
   #      5    0.867    0.173    2.080    0.416 RadixSort.py:26(__countSort)
   #      5    0.000    0.000    0.000    0.000 RadixSort.py:28(<listcomp>)
   #      1    0.001    0.001    2.087    2.087 RadixSort.py:37(sort)
   #      0    0.000             0.000          profile:0(profiler)
   #      1    0.000    0.000    2.088    2.088 profile:0(radix.sort())

		