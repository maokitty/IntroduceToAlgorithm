import math
class DocDistance(object):
	def __init__(self):
		self.file_1 = "txtFile/javawikipage.txt"
		self.file_2="txtFile/pythonwikipage.txt"

	def read_file(self,filename):
		try:
			file=open(filename)
			return file.readlines()
		except Exception as e:
			print(e)

	def word_split_file(self,records):
		words=[]
		for line in records:
			character_list=[]
			for character in line:
				if character.isalnum():
					character_list.append(character)
				elif len(character_list)>0:
					word="".join(character_list)
					word=word.lower()
					# words.append(word) #append可以是任何类型
					words.extend(word) #extend接受一个参数，这个参数总是list 比append要快
					character_list=[]
			if len(character_list)>0:
				word="".join(character_list)
				word=word.lower()
				words.extend(word)
				# words.append(word)
		return words

	def count_frequency(self,words):
		w_f=[]
		for word in words:
			for wf in w_f:
				if wf[0] == word:
					wf[1]=wf[1]+1
					break
			else:
				# python 语法：循环因为break被终止不会执行以下语句。当循环因为耗尽整个列表而终止时或条件变为假是会执行
				w_f.append([word,1])
		return w_f


	def word_frequence(self,filename):
		records = self.read_file(filename)
		words = self.word_split_file(records)
		w_f = self.count_frequency(words)
		return w_f

	def inner_product(self,w_f_1,w_f_2):
		sum = 0.0
		for w1,cnt1 in w_f_1:
			for w2,cnt2 in w_f_2:
				# 循环都是一样的 
				if w1 == w2:
					sum+=cnt1*cnt2
		return sum

	def distance(self):
		w_f_1 = self.word_frequence(self.file_1)
		w_f_2 = self.word_frequence(self.file_2)
		numerator = self.inner_product(w_f_1,w_f_2)
		denominator = math.sqrt(self.inner_product(w_f_1, w_f_1)*self.inner_product(w_f_2,w_f_2))
		dist = math.acos(numerator/denominator)
		print("%0.6f"%dist)

if __name__ == '__main__':
	import profile
	docDist = DocDistance()
	profile.run("docDist.distance()")

# 0.803896
#          274277 function calls in 2.099 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 :0(acos)
#    107145    0.129    0.000    0.129    0.000 :0(append)
#         1    0.000    0.000    2.098    2.098 :0(exec)
#    108885    0.131    0.000    0.131    0.000 :0(isalnum)
#     17180    0.022    0.000    0.022    0.000 :0(join)
#     23820    0.028    0.000    0.028    0.000 :0(len)
#     17180    0.021    0.000    0.021    0.000 :0(lower)
#         2    0.000    0.000    0.000    0.000 :0(nl_langinfo)
#         2    0.000    0.000    0.000    0.000 :0(open)
#         1    0.000    0.000    0.000    0.000 :0(print)
#         2    0.001    0.000    0.001    0.000 :0(readlines)
#         1    0.001    0.001    0.001    0.001 :0(setprofile)
#         1    0.000    0.000    0.000    0.000 :0(sqrt)
#        18    0.000    0.000    0.000    0.000 :0(utf_8_decode)
#         1    0.000    0.000    2.098    2.098 <string>:1(<module>)
#         2    0.000    0.000    0.000    0.000 _bootlocale.py:23(getpreferredencoding)
#         2    0.000    0.000    0.000    0.000 codecs.py:257(__init__)
#         2    0.000    0.000    0.000    0.000 codecs.py:306(__init__)
#        18    0.000    0.000    0.000    0.000 codecs.py:316(decode)
#         2    0.341    0.170    0.667    0.333 docDistance_listStruct.py:14(word_split_file)
#         2    0.702    0.351    0.707    0.353 docDistance_listStruct.py:32(count_frequency)
#         2    0.000    0.000    1.375    0.687 docDistance_listStruct.py:48(word_frequence)
#         3    0.722    0.241    0.722    0.241 docDistance_listStruct.py:54(inner_product)
#         1    0.000    0.000    2.097    2.097 docDistance_listStruct.py:63(distance)
#         2    0.000    0.000    0.001    0.001 docDistance_listStruct.py:7(read_file)
#         1    0.000    0.000    2.099    2.099 profile:0(docDist.distance())
#         0    0.000             0.000          profile:0(profiler)