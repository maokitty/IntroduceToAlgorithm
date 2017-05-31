import math
class BigInteger(object):
	"""计算500位的精度就有点慢了。。。，主要耗时在 extend/append 和乘法 使用karasuba大概可以快10s"""
	def __init__(self,val,sign=0):
		"""使用十进制"""
		self.value=[]
		self.sign=sign #0代表非负数
		for i in range(len(val)):
			if i==0 and val[i] == "-" :
				self.sign =-1 # -1代表是负数
				continue
			self.value.extend([int(val[i])])
		
	def length(self):
		return len(self.value)
	def getValue(self):
		return self.value

	def getSign(self):
		return self.sign

	def __keepBigFirst(self,a):
		sV=a.getValue()
		sLen=len(sV)
		lLen=len(self.value)
		if sLen >lLen:
			return sV ,sLen, self.value, lLen
		elif sLen < lLen:
			return self.value, lLen, sV, sLen
		else:
			for i in range(lLen):
				if self.value[i]>sV[i]:
					return self.value, lLen, sV, sLen
				elif self.value[i] < sV[i]:
					return sV ,sLen, self.value, lLen
			return sV ,sLen, self.value, lLen
	
	def compare(self,a):
		aSign=a.getSign()
		if self.sign>aSign:
			return 1
		elif aSign>self.sign:
			return -1
		else:
			result = 1
			aV=a.getValue()
			if len(self.value) > len(aV):
				if self.sign ==0:
					return 1
				else:
					return -1
			elif len(self.value) < len(aV):
				if self.sign ==0:
					return -1
				else:
					return 1
			else:
				for i in range(len(self.value)):
					if self.value[i]>aV[i]:
						if self.sign ==0:
							return 1
						else:
							return -1
					if self.value[i]<aV[i]:
						if self.sign ==0:
							return -1
						else:
							return 1
				return 0
						

	def absCompare(self,a):
		aV=a.getValue()
		vLen=len(self.value)
		aLen=len(aV)
		if vLen<aLen:
			return -1
		elif vLen>aLen:
			return 1
		else:
			for i in range(len(self.value)):
				if self.value[i] > aV[i]:
					return 1
				elif self.value[i] < aV[i]:
					return -1
		return 0

	def div(self,a,precision=0):
		if precision==0:
			quotient,remainder = self.mod(a)
			return quotient
		temp = self.mul_ten_power(ten.pow_ten(precision))
		quotient ,remainder=temp.mod(a)
		return quotient

	def mod(self,a):
		sV=self.value
		vLen=len(sV)
		aV=a.getValue()
		aLen=len(aV)
		if self.absCompare(a)<0:
			return BigInteger([0]), BigInteger(sV)
		quotient=[]
		dividend=BigInteger([sV[i] for i in range(aLen)])
		i=aLen-1
		divisor=BigInteger(aV)
		while i<vLen:
			q=0
			remainder=dividend.sub(divisor)
			#保证dividend>=dividor and len(rmV)-len(aV) <=1
			if remainder.getSign()<0:
				i+=1
				if i<vLen:
					dividend.getValue().extend([sV[i]])
				if len(quotient)!=0:
					quotient.extend([q])
				continue
			q +=1
			if remainder.absCompare(divisor)>=0:
				rmV=remainder.getValue()
				if len(rmV) == aLen:
					j=rmV[0] // aV[0]
					if j==1:
						remainder=remainder.sub(divisor)
						q+=j
				else:
					j=(rmV[0]*10+rmV[1]) // aV[0]
					if j==1:
						remainder=remainder.sub(divisor)
						q+=j
				if j!=1:
					temp=divisor.mul(BigInteger([j]))
					remainder=dividend.sub(temp)
					if remainder.getSign()<0:
						j-=1
						temp=temp.sub(divisor)
						remainder=dividend.sub(temp)
					if remainder.absCompare(a)>=0:
						j+=1
						temp=temp.add(divisor)
						remainder=dividend.sub(temp)
					q+=(j-1)
			i+=1
			rV=remainder.getValue()
			if i<vLen:
				rV.extend([sV[i]])
			quotient.extend([q])
			if len(rV)>1 and rV[0]==0:
				j=1
				while j<len(rV) and rV[j] ==0 :
					j+=1
				if j==vLen:
					remainder=BigInteger([0])
				else:
					rTemp=[]
					for k in range(j,len(rV)):
						rTemp.extend([rV[k]])
					remainder=BigInteger(rTemp)
			dividend=remainder



		if self.sign+a.getSign() == -1:
			remainder.sign=-1
			return BigInteger(quotient,-1),remainder
		return BigInteger(quotient),remainder
			
	def mul(self,a):
		if len(a.getValue())>40 and len(self.value)>40:
			return self.karasuba_mul(a)
		result=[]
		aV=a.getValue()
		lV=self.getValue()
		lVLen=len(lV)
		aVLen=len(aV)
		for i in range(lVLen-1,-1,-1):
			carry =0
			b=[0]*aVLen
			for j in range(aVLen-1,-1,-1):
				mul=aV[j]*lV[i]+carry
				carry=mul // 10
				b[j]=mul % 10
			if carry!=0:
				b.insert(0,carry % 10)
				carry=carry // 10
			while lVLen-i>1:
				b.extend([0])
				i+=1
			if len(result)<len(b):
				temp=result
				result=b
				b=temp
			bLen = len(b)
			rLen=len(result)
			while bLen>0:
				bLen -=1
				rLen -=1
				sum=result[rLen]+b[bLen]+carry
				result[rLen]=sum %10
				carry = sum // 10
			while carry!=0 and rLen>0:
				rLen -=1
				sum =result[rLen]+carry
				result[rLen]=sum%10
				carry=sum // 10
			if carry!=0:
				result.insert(0,carry)

		if self.sign+a.getSign()==-1:
			return BigInteger(result,-1)
		return BigInteger(result)
			
	def sub(self,a):
		if self.sign +  a.getSign() == -1:
			if self.sign ==0:
				return self.add(BigInteger(a.getValue()))
			return self.add(BigInteger(a.getValue(),-1))
		lV,lLen,sV,sLen = self.__keepBigFirst(a) 
		carry=0
		result=[0]*lLen
		while sLen>0:
			sLen -=1
			lLen -=1
			diff=lV[lLen]-sV[sLen]-carry
			if diff >=0:
				result[lLen]=diff
				carry=0
			else:
				result[lLen] = diff+10
				carry=1
		while carry!=0 and lLen>0:
			lLen -=1
			diff=lV[lLen]-carry
			if diff >=0:
				result[lLen]=diff
				carry=0
			else:
				result[lLen] = diff+10
				carry=1
		while lLen >0:
			lLen -=1
			result[lLen]=lV[lLen]
		j=0
		while j<len(result) and result[j] == 0:
			j+=1
		if j==len(result):
			return BigInteger([0])
		if j!=0:
			r=[0]*(len(result)-j)
			for i in range(j,len(result)):
				r[i-j]=result[i]
			result=r
		if  self.sign+a.getSign()==0 and lV!=self.value:
			return BigInteger(result,-1)
		if self.sign+a.getSign() == -2 and lV == self.value:
			return BigInteger(result,-1)
		return BigInteger(result)
			


	def add(self,a):
		if a.getSign() + self.sign == -1:
			if self.sign <0:
				return a.sub(BigInteger(self.value))
			else:
				return self.sub(BigInteger(a.getValue()))
		lV,lLen,sV,sLen = self.__keepBigFirst(a) 
		carry=0
		result=[0]*lLen
		while sLen >0:
			sLen -=1
			lLen -=1
			sum=sV[sLen]+lV[lLen]+carry
			result[lLen]=sum % 10
			carry=sum // 10
		while carry!=0 and lLen>0:
			lLen -=1
			sum=lV[lLen]+carry
			result[lLen]=sum %10
			carry = sum //10
			
		while lLen >0:
			lLen -=1
			result[lLen]=lV[lLen]
		if carry !=0:
			r=[1]
			for i in range(1,len(result)+1):
				r.extend([result[i-1]])
			result=r
		if self.sign+a.getSign() == -2:
			return BigInteger(result,-1)
		return BigInteger(result)
	
	def pow_ten(self,n):
		"""10的n次方"""
		r=[1]
		r+=[0]*n
		return BigInteger(r,self.sign)
	def ten_power_pow(self,n,m):
		"""10的n次方的m次方"""
		r=[1]
		r+=[0]*n*m
		return BigInteger(r,self.sign)
	
	def mul_ten_power(self,n):
		"""当前数字乘以10的n次方"""
		r=[i for i in self.value]
		if isinstance(n,BigInteger):
			nV=n.getValue()
			r+=[nV[i] for i in range(1,len(nV))]
			return BigInteger(r,self.sign)
		if n<1:
			return self
		r+=[0]*n
		return BigInteger(r,self.sign)
	def __trustedStripLeadingZeroInts(self,a):
		j=0
		for i in a:
			if i!=0:
				break
			j+=1
		if j<len(a):
			return a[j:]
		return [0]
	def karasuba_mul(self,a):
		aV=a.getValue()
		sV=self.getValue()
		maxLength=max(len(aV),len(sV))
		sP=maxLength//2
		h1,l1=BigInteger(self.__trustedStripLeadingZeroInts(sV[:-sP])),BigInteger(self.__trustedStripLeadingZeroInts(sV[-sP:]))
		h2,l2=BigInteger(self.__trustedStripLeadingZeroInts(aV[:-sP])),BigInteger(self.__trustedStripLeadingZeroInts(aV[-sP:]))
		z0=l1.mul(l2)
		z1=l1.add(h1).mul(l2.add(h2))
		z2=h1.mul(h2)
		result=z2.mul_ten_power(self.pow_ten(2*sP)).add(z1.sub(z2).sub(z0).mul_ten_power(self.pow_ten(sP))).add(z0)
		if a.getSign()!=self.sign:
			result.sign=-1
		else:
			result.sign=0
		return result
	
	def __str__(self):
		r=[]
		if self.sign==-1:
			r.append("-")
		for i in range(len(self.value)):
			r.append(str(self.value[i]))
		return "".join(r)


class Catalan(object):
	"""
    假设圆的直径是1000,000,000,000,圆心在C，在圆上做半径AC,BC，作BD垂直于AC，使得 |bd|=1,且角bca小于90度 求AD
    AD=(AC-CD)=(AC-根号下(BC^2-BD^2))
    http://people.csail.mit.edu/devadas/numerics_demo/chord.html
	"""
	ten = BigInteger("10")
	two=BigInteger("2")
	def __init__(self,guessValue,initvalue,precision):
		super(Catalan, self).__init__()
		self.rn=initvalue
		self.x=BigInteger(guessValue)
		self.precision=precision
		self.multiplier=Catalan.ten.pow_ten(precision)
		self.multiplier_square=Catalan.ten.pow_ten(2*precision)
		self.scaledn=self.rn.mul(self.multiplier)
	def fx(self,precision):
		fxa=self.x.sub(self.scaledn)
		fxb=self.x.mul(fxa)
		fxc=fxb.add(self.multiplier)
		return self.x.mul(self.x.sub(self.scaledn)).add(self.multiplier_square)

	def dfx(self,precision):
		dfxa=self.x.mul(Catalan.two)
		dfxb=dfxa.sub(self.scaledn)
		return self.x.mul(Catalan.two).sub(self.scaledn)
		
	def newtonMethod(self):
		while True:
			fatx=self.fx(self.precision)
			dfatx=self.dfx(self.precision)
			xn=self.x.sub(fatx.div(dfatx))
			if xn.compare(self.x)==0:
				break
			self.x=xn
	def __str__(self):
		r=["0."]
		while  self.precision - (len(self.x.getValue())+len(r))+2>0:
			r.append("0")
		xV=self.x.getValue()
		for i in range(len(xV)):
			r.append(str(xV[i]))
		return "".join(r)

def addWithCarry():
	x=BigInteger("12345")
	y=BigInteger("55")
	z=y.add(x)
	print("12345+ 55=",z)
	w=x.add(y)
	print("55 +12345=",w)
def addOverFlow():
	x=BigInteger("9")
	y=BigInteger("1")
	print("9+1=",x.add(y))
def subWithCarry():
	x=BigInteger("123")
	y=BigInteger("34")
	print("123-34=",x.sub(y))
	print("34-123=",y.sub(x))
def addMinus():
	x=BigInteger("11")
	y=BigInteger("-9")
	print("11+(-9)=",x.add(y))
	print("(-9)+11=",y.add(x))
	z=BigInteger("-1")
	print("(-1)+(-9)=",z.add(y))
def subMinus():
	x=BigInteger("11")
	y=BigInteger("-9")
	print("11-(-9)=",x.sub(y))
	print("(-9)-11=",y.sub(x))
	z=BigInteger("-1")
	print("(-1)-(-9)=",z.sub(y))
	w=BigInteger("-11")
	print("(-11)-(-9)=",w.sub(y))
def mul():
	x=BigInteger("0")
	y=BigInteger("-9")
	print("99*(-9)=",x.mul(y))
	print("(-9)*99=",y.mul(x))
	z=BigInteger("12345678901234")
	w=BigInteger("99999999999999")
	print("12345678901234*99999999999999=",z.mul(w))
	print("12345678901234*99999999999999=",w.mul(z))
	a=BigInteger("-12382152733846")
	print("-12382152733846*(-9)",a.mul(y))
def mod():
	x=BigInteger("99")
	y=BigInteger("9")
	quotient,remainder=x.mod(y)
	print("99/9 q:",quotient," re:",remainder)
	quotient,remainder=y.mod(x)
	print("9/99 q:",quotient," re:",remainder)
	x=BigInteger("93721278331123721983")
	y=BigInteger("-198738934758947358439891273938274392847")
	quotient,remainder=x.mod(y)
	print("q",quotient,"r",remainder)
	quotient,remainder=y.mod(x)
	print("(-198738934758947358439891273938274392847)/93721278331123721983=q",quotient,"r",remainder)
	x=BigInteger("2250")
	y=BigInteger("113")
	q,r=x.mod(y)
	print("2250 / 113",q,r)
	x=BigInteger("1234532423")
	y=BigInteger("3")
	q,r=x.mod(y)
	print("1234532423 / 3",q,r)
	x=BigInteger("10")
	y=BigInteger("3")
	q,r=x.mod(y)
	print("10/3=",q,r)
	x=BigInteger("9")
	q,r=x.mod(y)
	print("9/3=",q,r)
	x=BigInteger("2")
	q,r=x.mod(y)
	print("2/3=",q,r)
	x=BigInteger("-3")
	y=BigInteger("-3")
	q,r=x.mod(y)
	print("-3/-3=",q,r)
def generate():
	ten=BigInteger("10")
	ct = Catalan("1",ten.pow_ten(12),500)
	ct.newtonMethod()
	print(ct)
def karasuba():
	x=BigInteger("123912837981273982749827598327498732984723894782374983274982374982374987329847328974893274892374987238947239847892374982374827389472389473289472398474298472389478237498327498237498229847238947823749832749823749822984723894782374983274982374982298472389478237498327498237498229847238947823749832749823749822984723894782374983274982374982298472389478237498327498237498229847238947823749832749823749821928739843578923749703928409382094809384209840923840928304982309482039840912398792387894375843658437658743657843658743658736487519287398435789237497039284093820948093842098409238409283049823094820398409123987923878943758436584376587436578436587436587364875192873984357892374970392840938209480938420984092384092830498230948203984091239879238789437584365843765874365784365874365873648755679873298372498327498237489723492837493822759438759873498739879837258973498257892735897238947982374892374987238947239847398")
	y=BigInteger("192873984357892374970392840938209480938420984092384092830498230948203984091239879238789437584365843765874365784365874365871928739843578923749703928409382094809384209840923840928304982309482039840912398792387894375843658437658743657843658743658736487519287398435789237497039284093820948093842098409238409283049823094820398409123987923878943758436584376587436578436587436587364875192873984357892374970392840938209480938420984092384092830498230948203984091239879238789437584365843765874365784365874365873648751928739843578923749703928409382094809384209840923840928304982309482039840912398792387894375843658437658743657843658743658736487519287398435789237497039284093820948093842098409238409283049823094820398409123987923878943758436584376587436578436587436587364875364875")
	print(x.mul(y))
	print("$$$$")
	print(x.karasuba_mul(y))
def mulTenP():
	x=BigInteger("-99999999999999999999999900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
	y=BigInteger("100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
	print(x.mul(y))
if  '__main__':
	#addWithCarry()
	#addOverFlow()
	#subWithCarry()
	#addMinus()
	#subMinus()
	#mul()
	#mod()
	import profile
	profile.run("generate()")
	#karasuba()
	#mulTenP()

