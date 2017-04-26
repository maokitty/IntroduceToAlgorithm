class RollingHashStepByStep(object):
	"""
	对RollingHash进行一步一步的拆分，可以分成两个步骤，每个步骤都会生成对应的hash值
	"""
	def __init__(self, base,p):
		"""
		得到一个rollinghash初始值
		"""
		super(RollingHashStepByStep, self).__init__()
		self.base = base
		# 质数
		self.p = p
		# 刚开始没有元素
		self.chash= 0 
		# 刚开始没有元素 magic = magic ** k %p k=0
		self.magic= 1
		self.ibase = base ** (-1) 
	# 保证数据小
	def append(self,newChar):
		"""
		在原有的hash基础上增加一个字符，计算其hash值
		"""
		# old 返回一个字串的 ASCII值
		new10=ord(newChar)
		self.chash = (self.chash * self.base + new10 ) % self.p
		#滑动窗口中增加一个元素,根据magic的定义 magic是base的长度的次方
		self.magic = (self.magic * self.base) 

	def skip(self,oldChar):
		"""
		在原有的hash基础上去掉一个字符,计算其hash值
		"""
		# hash-old*magic 可能是负值 old < base magic <p
		self.magic =int(self.magic * self.ibase) 
		# todo  进制计算，为什么传进来的数字不需要转换成对应的进制 在不用base的地方进行解答
		old10 =ord(oldChar); 
		self.chash = (self.chash-old10*self.magic + self.p * self.base )  % self.p
	
	def hash(self):
		return self.chash

class RollingHashCombination(object):
	"""
	将rolling hash的每一步组合起来
	"""
	def __init__(self,s):
		base = 7
		p=499999
		self.rhStepByStep = RollingHashStepByStep(base,p)
		for c in s:
			self.rhStepByStep.append(c)
		self.chash = self.rhStepByStep.hash()
	
	def hash(self):
		return self.chash

	def slide(self,preChar,nextChar):
		"""
		删掉之前的值 , 添加新的值
		"""
		self.rhStepByStep.skip(preChar)
		self.rhStepByStep.append(nextChar)
		self.chash = self.rhStepByStep.hash()

class stringMatch(object):
	def __init__(self,fs,findStr,caseSensive=False):
		self.findStr = findStr
		self.count = 0
		try:
			f=open(fs)
			readlines = f.readlines()
			lineList = []
			for realine in readlines:
				if caseSensive:
					lineList.append(realine)
				else:
					lineList.append(realine.lower())
			self.lines = ''.join(lineList)

		except Exception as e:
			print(e)
			raise e
	def rhCombinationMatch(self):
		winLength = len(self.findStr)
		winRh = RollingHashCombination(self.findStr)
		lineLen = len(self.lines)
		matchRh = RollingHashCombination(self.lines[0:winLength])
		for i in range(0,lineLen-winLength+1):
			if matchRh.hash() == winRh.hash():
				sequence=self.lines[i:i+winLength]
				# hash冲突
				if sequence == self.findStr:
					self.count+=1
			if i+winLength<lineLen:
				matchRh.slide(self.lines[i],self.lines[i+winLength])

if __name__ == '__main__':
	import profile
	def testRollingHashStepByStep():
		base = 10
		p=49999
		rh = RollingHashStepByStep(base,p) 
		print(rh.hash())
		rh.append('a')
		rh.append('b')
		rh.append('c')
		rh.append('d')
		rh.append('e')
		rh.skip('a')
		rh2 = RollingHashStepByStep(base,p)
		rh2.append('b')
		rh2.append('c')
		rh2.append('d')
		rh2.append('e')
		print("testRollingHashStepByStep ",rh.hash() == rh2.hash())
	# testRollingHashStepByStep()
	stringMatc = stringMatch("../txtFile/javawikipage.txt","java")
	profile.run("stringMatc.rhCombinationMatch()")
	print(stringMatc.count)
