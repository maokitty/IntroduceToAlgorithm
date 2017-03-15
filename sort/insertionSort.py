import sys
class InsertionSort(object):
	"""docstring for InsertionSort"""
	def __init__(self, toSortFile):
		super(InsertionSort, self).__init__()
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

	def start(self):
		data = self.loadData(self.tsf)
		for i in range(len(data)):
			num = data[i]
			j = i -1
			while j>-1 and data[j]>num:
				data[j+1] = data[j]
				j-=1
			data[j+1]=num
		print(data)

		

if __name__ == '__main__':
	import profile
	largeSize = True
	if len(sys.argv) == 2:
		tsf = sys.argv[1]
	elif largeSize:
		tsf="../txtFile/sortData_50000.txt"
	else:
		tsf="../txtFile/sortData_5.txt"
		
	insertionSort = InsertionSort(tsf)
	profile.run("insertionSort.start()")

   #       2088 function calls in 180.892 seconds

   # Ordered by: standard name

   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000  180.892  180.892 :0(exec)
   #    500    0.001    0.000    0.001    0.000 :0(extend)
   #      1    0.000    0.000    0.000    0.000 :0(len)
   #      1    0.000    0.000    0.000    0.000 :0(nl_langinfo)
   #      1    0.000    0.000    0.000    0.000 :0(open)
   #      1    0.008    0.008    0.008    0.008 :0(print)
   #      1    0.000    0.000    0.001    0.001 :0(readlines)
   #    500    0.001    0.000    0.001    0.000 :0(replace)
   #      1    0.001    0.001    0.001    0.001 :0(setprofile)
   #    500    0.003    0.000    0.003    0.000 :0(split)
   #     37    0.000    0.000    0.000    0.000 :0(utf_8_decode)
   #      1    0.001    0.001  180.892  180.892 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 _bootlocale.py:23(getpreferredencoding)
   #      1    0.000    0.000    0.000    0.000 codecs.py:257(__init__)
   #      1    0.000    0.000    0.000    0.000 codecs.py:306(__init__)
   #     37    0.000    0.000    0.000    0.000 codecs.py:316(decode)
   #    500    0.013    0.000    0.013    0.000 insertionSort.py:15(<listcomp>)
   #      1  180.860  180.860  180.890  180.890 insertionSort.py:20(start)
   #      1    0.004    0.004    0.023    0.023 insertionSort.py:8(loadData)
   #      1    0.000    0.000  180.892  180.892 profile:0(insertionSort.start())
   #      0    0.000             0.000          profile:0(profiler)
