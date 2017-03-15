import sys
class MergeSort(object):
	"""docstring for MergeSort"""
	def __init__(self, toSortFile):
		super(MergeSort, self).__init__()
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

	def mergeLR(self,start,mid,end,data):
		i=0
		j=0
		k=start
		# python3 语法 range(start,mid+1) mid+1无法返回
		l=[ data[v] for v in range(start,mid+1) ]
		r=[ data[v] for v in range(mid+1,end+1) ]
		while i<len(l) and j<len(r):
			if l[i] >= r[j]:
				data[k]=r[j]
				k+=1
				j+=1
			else:
				data[k]=l[i]
				i+=1
				k+=1
		for li in range(i,len(l)):
			data[k]=l[li]
			k+=1
		for rj in range(j,len(r)):
			data[k]=r[rj]
			k+=1
    
    # end 取值 如果给的是数组的长度，那么在merge的时候需要区分左侧merge和右侧merge end是否可以取得到
    # 1分隔到最小的单元再合并
    # 2合并左侧取到中间值，右侧则不获取
	def subMerge(self,start,end,data):
		if start != end :
			mid = (end+start) // 2
			self.subMerge(start,mid,data)
			self.subMerge(mid+1,end,data)
			self.mergeLR(start,mid,end,data)




	def start(self):
		data = self.loadData(self.tsf)
		self.subMerge(0,len(data)-1,data)
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
	mergeSort = MergeSort(tsf)
	profile.run("mergeSort.start()")
	
#   1865840 function calls (1765840 primitive calls) in 6.435 seconds

 #   Ordered by: standard name

 #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #        1    0.000    0.000    6.434    6.434 :0(exec)
 #      500    0.001    0.000    0.001    0.000 :0(extend)
 #  1613752    2.510    0.000    2.510    0.000 :0(len)
 #        1    0.000    0.000    0.000    0.000 :0(nl_langinfo)
 #        1    0.000    0.000    0.000    0.000 :0(open)
 #        1    0.007    0.007    0.007    0.007 :0(print)
 #        1    0.000    0.000    0.001    0.001 :0(readlines)
 #      500    0.001    0.000    0.001    0.000 :0(replace)
 #        1    0.001    0.001    0.001    0.001 :0(setprofile)
 #      500    0.003    0.000    0.003    0.000 :0(split)
 #       37    0.000    0.000    0.000    0.000 :0(utf_8_decode)
 #        1    0.001    0.001    6.434    6.434 <string>:1(<module>)
 #        1    0.000    0.000    0.000    0.000 _bootlocale.py:23(getpreferredencoding)
 #        1    0.000    0.000    0.000    0.000 codecs.py:257(__init__)
 #        1    0.000    0.000    0.000    0.000 codecs.py:306(__init__)
 #       37    0.000    0.000    0.000    0.000 codecs.py:316(decode)
 #      500    0.013    0.000    0.013    0.000 mergeSort.py:15(<listcomp>)
 #    50000    3.268    0.000    5.972    0.000 mergeSort.py:20(mergeLR)
 #    50000    0.102    0.000    0.102    0.000 mergeSort.py:26(<listcomp>)
 #    50000    0.091    0.000    0.091    0.000 mergeSort.py:28(<listcomp>)
 # 100001/1    0.431    0.000    6.403    6.403 mergeSort.py:47(subMerge)
 #        1    0.000    0.000    6.433    6.433 mergeSort.py:60(start)
 #        1    0.003    0.003    0.022    0.022 mergeSort.py:8(loadData)
 #        1    0.000    0.000    6.435    6.435 profile:0(mergeSort.start())
 #        0    0.000             0.000          profile:0(profiler)
	# 