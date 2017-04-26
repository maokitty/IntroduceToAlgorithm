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

	def equalsMatch(self):
		lineLen = len(self.lines)
		winLength = len(self.findStr)
		for i in range(0,lineLen-winLength):
			# 为什么这样会特别快
			if self.findStr == self.lines[i:i+winLength]:
				self.count+=1

if __name__ == '__main__':
	import profile
	stringMatc = stringMatch("../txtFile/javawikipage.txt","java")
	profile.run("stringMatc.equalsMatch()")
	print(stringMatc.count)