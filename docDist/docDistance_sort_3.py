import sys
import math
class DocDist(object):
	"""docstring for DocDist"""
	def __init__(self, f1,f2):
		super(DocDist, self).__init__()
		self.f1=f1
		self.f2=f2

	def read(self,fileName):
		try:
			f = open(fileName)
			return f.readlines()
		except Exception as e:
			print(e)

	def getwords(self,lines):
		words=[]
		for line in lines:
			words_inline = self.get_inline_words(line)
			words.extend(words_inline)
		return words

	def get_inline_words(self,line):
		words=[]
		character_list=[]
		for char in line:
			if char.isalnum():
				character_list.append(char)
			elif len(character_list)>0:
				word="".join(character_list)
				word=word.lower()
				words.append(word)
				character_list=[]
		if len(character_list)>0:
			word="".join(character_list)
			word=word.lower()
			words.append(word)
		return words



	def count_frequency(self,words):
		w_f=[]
		for word in words:
			for wf in w_f:
				if wf[0]==word:
					wf[1]=wf[1]+1
					break
			else:
				w_f.append([word,1])
		return w_f

	def mysort(self,wf):
		for i in range(len(wf)):
			key=wf[i]
			j = i-1
			while j>-1 and wf[j] > key:
				wf[j+1]=wf[j]
				j=j-1
			wf[j+1]=key

	def getWords_frequncy(self,fileName):
		lines=self.read(fileName)
		words=self.getwords(lines)
		wf=self.count_frequency(words)
		# 排序可以减少计算时候的循环量
		self.mysort(wf)
		return wf

	def inner_product(self,wf1,wf2):
		sum =0.0
		i=0
		j=0
		while i<len(wf1) and j<len(wf2):
			if wf1[i][0] == wf2[j][0]:
				sum += wf1[i][1]*wf2[j][1]
				i = i+1
				j=j+1
			elif wf1[i][0] < wf2[j][0]:
				i=i+1
			else:
				j=j+1
		return sum

	def getDist(self):
		w_f_1 = self.getWords_frequncy(self.f1)
		w_f_2 = self.getWords_frequncy(self.f2)
		numinator =  self.inner_product(w_f_1,w_f_2)
		denominator =  math.sqrt(self.inner_product(w_f_1,w_f_1)*self.inner_product(w_f_2,w_f_2))
		dist = math.acos(numinator/denominator)
		print("distance %0.6f"%dist)


if __name__ == '__main__':
	import profile
	if len(sys.argv) == 3:
		f1=sys.argv[1]
		f2=sys.argv[2]
	else:
		f1="../txtFile/javawikipage.txt";
		f2="../txtFile/pythonwikipage.txt"
	docDist = DocDist(f1,f2)
	profile.run("docDist.getDist()")

# distance 0.803896
#          290454 function calls in 1.755 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 :0(acos)
#    107145    0.113    0.000    0.113    0.000 :0(append)
#         1    0.000    0.000    1.754    1.754 :0(exec)
#       863    0.001    0.000    0.001    0.000 :0(extend)
#    108885    0.114    0.000    0.114    0.000 :0(isalnum)
#     17180    0.019    0.000    0.019    0.000 :0(join)
#     38269    0.039    0.000    0.039    0.000 :0(len)
#     17180    0.018    0.000    0.018    0.000 :0(lower)
#         2    0.000    0.000    0.000    0.000 :0(nl_langinfo)
#         2    0.000    0.000    0.000    0.000 :0(open)
#         1    0.000    0.000    0.000    0.000 :0(print)
#         2    0.000    0.000    0.001    0.000 :0(readlines)
#         1    0.001    0.001    0.001    0.001 :0(setprofile)
#         1    0.000    0.000    0.000    0.000 :0(sqrt)
#        18    0.000    0.000    0.000    0.000 :0(utf_8_decode)
#         1    0.001    0.001    1.754    1.754 <string>:1(<module>)
#         2    0.000    0.000    0.000    0.000 _bootlocale.py:23(getpreferredencoding)
#         2    0.000    0.000    0.000    0.000 codecs.py:257(__init__)
#         2    0.000    0.000    0.000    0.000 codecs.py:306(__init__)
#        18    0.000    0.000    0.000    0.000 codecs.py:316(decode)
#         2    0.000    0.000    0.001    0.000 docDistance_sort_3.py:10(read)
#         2    0.003    0.001    0.588    0.294 docDistance_sort_3.py:17(getwords)
#       863    0.299    0.000    0.584    0.001 docDistance_sort_3.py:24(get_inline_words)
#         2    0.608    0.304    0.612    0.306 docDistance_sort_3.py:43(count_frequency)
#         2    0.519    0.259    0.519    0.259 docDistance_sort_3.py:54(mysort)
#         2    0.000    0.000    1.720    0.860 docDistance_sort_3.py:63(getWords_frequncy)
#         3    0.019    0.006    0.033    0.011 docDistance_sort_3.py:71(inner_product)
#         1    0.000    0.000    1.753    1.753 docDistance_sort_3.py:86(getDist)
#         1    0.000    0.000    1.755    1.755 profile:0(docDist.getDist())
#         0    0.000             0.000          profile:0(profiler)

