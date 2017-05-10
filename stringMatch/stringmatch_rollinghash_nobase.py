class RollingHash(object):
	"""
	去掉 stringmatch_rollinghash中的base
	这样做的缺点是:比如字串 abcd 和 bdca,没有base回导致hash值一致，从而hash冲突
	另外，假设基数是 2^p ,mod = 2^p-1由于 
		x * (2^p)^n mod (2^p - 1) = x (2^p)^(n-1) * (2^p mod (2^p-1)) mod (2^p - 1) 
								  = x (2^p)^(n-1) mod (2^p - 1) 
								  = x
		相当于直接相加，没有产生作用
	"""
	def __init__(self,s):
		self.prime = 499999
		self.chash=0
		n = len(s)-1
		for c in s:
			self.chash += ord(c) 
			n -= 1
	def hash(self):
		return self.chash
		
	def slide(self,preChar,nextChar):
		self.chash=(self.chash - ord(preChar)+ ord(nextChar)) % self.prime
		if self.chash <  0:
			# 做求余运算使得 chash < prime < ord(preChar)[prime太小],在有的语言里面求余会得到不同的数值
			self.chash +=self.prime

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

	def rhMatch(self):
		winRh = RollingHash(self.findStr)
		winLength = len(self.findStr)
		lineLen = len(self.lines)
		matchRh = RollingHash(self.lines[0:winLength])
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
	def testRollingHash():
		rh1 = RollingHash('abcde')
		rh2 = RollingHash('bcdef')
		rh3 = RollingHash('cdefZ')
		rh1.slide('a','f')
		print("testRollingHash ",rh1.hash() == rh2.hash())
		rh1.slide('b','Z')
		print("testRollingHash ",rh1.hash() == rh3.hash())
	stringMatc = stringMatch("../txtFile/javawikipage.txt","java")
	profile.run("stringMatc.rhMatch()")
	print(stringMatc.count)
