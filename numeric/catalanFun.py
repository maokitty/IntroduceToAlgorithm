import math
class BigInteger(object):
	def __init__(self,val,sign=0):
		"""使用十进制"""
		self.value=[]
		self.sign=sign #0代表非负数
		for i in range(len(val)):
			if i==0 and val[i] == "-" :
				self.sign =-1 # -1代表是负数
				continue
			self.value.append(int(val[i]))
		
#	def pow10(self,power):
#		i=power
#		while(i>0):
#			self.value.append("0")
#			i-=1
	def multiTo(self,a):
		valueStr="".join(self.value)
		aStr=str(a)
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

	def mod(self,a,precision=0):
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
					dividend.getValue().append(sV[i])
				if len(quotient)!=0:
					quotient.append(q)
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
						#temp=divisor.mul(BigInteger([j]))
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
				rV.append(sV[i])
			quotient.append(q)
			if len(rV)>1 and rV[0]==0:
				j=1
				while rV[j] ==0 and j<vLen:
					j+=1
				if j==vLen:
					remainder=BigInteger([0])
				else:
					rTemp=[]
					for k in range(j,len(rV)):
						rTemp.append(rV[k])
					remainder=BigInteger(rTemp)
			dividend=remainder



		if self.sign+a.getSign() == -1:
			remainder.sign=-1
			return BigInteger(quotient,-1),remainder
		return BigInteger(quotient),remainder



	def mul10(self,n):
		val=self.value
		while n>0:
			val.append(0)
			n-=1
		return BigInteger(val,self.sign)
			
	def mul(self,a):
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
				b.append(0)
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
				r.append(result[i-1])
			result=r
		if self.sign+a.getSign() == -2:
			return BigInteger(result,-1)
		return BigInteger(result)

		
			

#	def __karasuba(self,x,y):
		
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
	def __init__(self,radius,side,digit):
		super(Catalan, self).__init__()
		self.radius = radius
		self.side = side
		self.digit = digit

	def catalanMagic(self):
		a=self.radius**2-self.side**2
		a=2
		x=self.initGuess(a)
		ntVal=self.newtonMethod(x,a,self.digit)
		val = self.radius-ntVal
		print("val",val)
	
	def initGuess(self,a):
		value=2
		while (value**2)<a:
			value=value**2
		return value
	def newtonMethod(self,x,a,digit):
		d=0
		while d<digit:
			xNext=self.nextValue(x,a,digit)
			x=xNext
			d=d+2
			print("xNext",xNext)
		return x

	def nextValue(self,b,a,digit):
		yd=0
		R=10**digit
		y=1
		while yd<digit:
			yNext = 2*y-(b/R)*(y**2)
			y=yNext
			yd=yd+2
		return 0.5*(b+a*yd)


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
	x=BigInteger("99")
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


	
	

if  __name__ == '__main__':
	#addWithCarry()
	#addOverFlow()
	#subWithCarry()
	#addMinus()
	#subMinus()
	#mul()
	mod()
