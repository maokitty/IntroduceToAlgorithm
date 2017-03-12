import sys
import math
# 数据结构选错出现问题
class Docdis(object):
	def __init__(self):
		self.file_1 = "txtFile/javawikipage.txt"
		self.file_2="txtFile/pythonwikipage.txt"

	def readFile(self,filename):
		try:
			f=open(filename)
			return f.readlines()
		except Exception as e:
			print(e)

	def get_world_frequency(self,filename):
		lines=self.readFile(filename)
		word_list =[]
		for line in lines:
			character_list=[]
			# 读取每一个字符
			for character in line:
				if character.isalnum():
					character_list.append(character)
				elif len(character_list)>0:
					# 拼接list 形如 ['a','b'] 结果是 ab
					word = "".join(character_list)
					word = word.lower()
					word_list.append(word)
					character_list=[]
			if len(character_list)>0:
				word = "".join(character_list)
				word = word.lower()
				word_list.append(word)
		word_frequency = []
		for word in word_list:
			for w_f in word_frequency:
				if word in w_f:
					w_f[word] = w_f[word]+1
					break
			else:
				word_frequency.append({word:1})
		return word_frequency

	def inner_product(self,wf1,wf2):
		sum = 0.0
		for w1 in wf1:
			for w2 in wf2:
				# 由于选用的是 字典 ，这段代码很丑陋
				# 用字典的缘由 key-value应该是一对的 
				if list(w1.keys())[0] == list(w2.keys())[0]:
					sum +=list(w1.values())[0]*list(w2.values())[0]
		return sum

	def getdistance(self):
		word_frequency_1=self.get_world_frequency(self.file_1)
		word_frequency_2=self.get_world_frequency(self.file_2)
		numerator=self.inner_product(word_frequency_1,word_frequency_2)
		denominator=math.sqrt(self.inner_product(word_frequency_1,word_frequency_1)*self.inner_product(word_frequency_2,word_frequency_2))
		dist = math.acos(numerator/denominator)
		print(dist)


if __name__ == '__main__':
	import profile
	doc =Docdis()
	profile.run("doc.getdistance()")

# 0.8038961724616909
#          24842905 function calls in 70.756 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 :0(acos)
#    107145    0.169    0.000    0.169    0.000 :0(append)
#         1    0.000    0.000   70.755   70.755 :0(exec)
#    108885    0.170    0.000    0.170    0.000 :0(isalnum)
#     17180    0.029    0.000    0.029    0.000 :0(join)
#  由于选错了数据结构，导致这里的keys调用时间大量增加，而且在代码上非常的丑陋
#  24558866   27.742    0.000   27.742    0.000 :0(keys)
#     23820    0.037    0.000    0.037    0.000 :0(len)
#     17180    0.028    0.000    0.028    0.000 :0(lower)
#         2    0.000    0.000    0.000    0.000 :0(nl_langinfo)
#         2    0.000    0.000    0.000    0.000 :0(open)
#         1    0.000    0.000    0.000    0.000 :0(print)
#         2    0.001    0.000    0.001    0.001 :0(readlines)
#         1    0.001    0.001    0.001    0.001 :0(setprofile)
#         1    0.000    0.000    0.000    0.000 :0(sqrt)
#        18    0.000    0.000    0.000    0.000 :0(utf_8_decode)
#      9766    0.012    0.000    0.012    0.000 :0(values)
#         1    0.001    0.001   70.755   70.755 <string>:1(<module>)
#         2    0.953    0.476    1.387    0.694 DocDistance.py:16(get_world_frequency)
#   重复数据接口的问题
#         3   41.612   13.871   69.366   23.122 DocDistance.py:45(inner_product)
#         1    0.001    0.001   70.754   70.754 DocDistance.py:55(getdistance)
#         2    0.000    0.000    0.001    0.001 DocDistance.py:9(readFile)
#         2    0.000    0.000    0.000    0.000 _bootlocale.py:23(getpreferredencoding)
#         2    0.000    0.000    0.000    0.000 codecs.py:257(__init__)
#         2    0.000    0.000    0.000    0.000 codecs.py:306(__init__)
#        18    0.000    0.000    0.000    0.000 codecs.py:316(decode)
#         1    0.000    0.000   70.756   70.756 profile:0(doc.getdistance())
#         0    0.000             0.000          profile:0(profiler)
