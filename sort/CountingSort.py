import sys
class Counting(object):
	"""docstring for Counting"""
	def __init__(self,toSortFile,maxValue):
		super(Counting, self).__init__()
		try:
			f=open(toSortFile)
			lines = f.readlines()
			self.data=[]
			self.maxValue=maxValue
			for line in lines:
				nums = line.replace('\n','').split(',')
				self.data.extend([int(num) for num in nums])
		except Exception as e:
			print(e)
			raise e
	def sort(self):
		k=self.maxValue+1
		L=[[] for i in range(k)]
		n=len(self.data)
		for j in range(n):
			# 保证原有的相同元素顺序不会更改
			L[self.data[j]].append(self.data[j])
		output=[]
		for i in range(k):
			output.extend(L[i])
		print(output)

if __name__ == '__main__':
	import profile
	largeSize = True
	if len(sys.argv) ==2:
		toSortFile = sys.argv[1]
	elif largeSize:
		toSortFile = "../txtFile/sortData_50000.txt"
		maxValue=50000
	else:
		toSortFile = "../txtFile/sortData_5.txt"
		maxValue=100
	cnt = Counting(toSortFile,maxValue)
	profile.run("cnt.sort()")

	  #        100010 function calls in 0.308 seconds

   # Ordered by: standard name

   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #  50001    0.069    0.000    0.069    0.000 :0(append)
   #      1    0.000    0.000    0.307    0.307 :0(exec)
   #  50001    0.060    0.000    0.060    0.000 :0(extend)
   #      1    0.000    0.000    0.000    0.000 :0(len)
   #      1    0.011    0.011    0.011    0.011 :0(print)
   #      1    0.001    0.001    0.001    0.001 :0(setprofile)
   #      1    0.009    0.009    0.306    0.306 <string>:1(<module>)
   #      1    0.150    0.150    0.297    0.297 CountingSort.py:17(sort)
   #      1    0.007    0.007    0.007    0.007 CountingSort.py:19(<listcomp>)
   #      1    0.000    0.000    0.308    0.308 profile:0(cnt.sort())
   #      0    0.000             0.000          profile:0(profiler)

		