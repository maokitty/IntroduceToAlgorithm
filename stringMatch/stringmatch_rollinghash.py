class RollingHash(object):
	"""
	n(0) 旧数字
	n(1) 新数字
	old 要删除的元素
	new 要增加的元素
	base 进制
	k 要比较的字串的长度 比如 algorithm 找 gorit   k是5
    n(1) = (n(0)-old*base^(K-1))*base+new
    假设旧数字的hash值是 h1,新数字的hash是
    h2=[(n(0)-old*base^(K-1))*base+new] mod p
      =[(n(0) mode p)*base -old *(base^(k) mod p) +new ] mod p  //对同行一个数求两次余数不会改变结果
    使magic = base(k) mod p 而 h1 = n(0) mod p
    h2= [h1*base -old*magic +new ]mod p
	"""
	def __init__(self,s):
		self.base = 7
		self.prime = 499999
		self.chash=0
		lenS = len(s)
		n = lenS-1
		self.magic = (self.base ** lenS ) % self.prime
		for c in s:
			self.chash += ord(c) * (self.base ** n)
			n -= 1
	def hash(self):
		return self.chash
		
	def slide(self,preChar,nextChar):
		self.chash=(self.chash*self.base - ord(preChar)*self.magic + ord(nextChar)) % self.prime

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
