import random
class BST(object):
	def __init__(self):
		self.root = None

	def insertDistinct(self,z):
		result = self.search(z.key)
		if isinstance(result,Node):
			print(str(z.key)+" already exist")
		else:
			self.insert(z)

	def searchSuccessor(self,key):
		if key == None:
			return None
		x=self.search(key)
		if isinstance(x,Node):
			return self.successor(x)
		else:
			return None

	def searchDelete(self,key):
		if key == None:
			return None
		x=self.search(key)
		if isinstance(x,Node):
			return self.delete(x)
		else:
			return None

	def insert(self,z):
		x = self.root
		y=None # x's parent
		while x!=None :
			y=x
			if x.key <= z.key:
				x=x.right
			else:
				x=x.left
		if y == None:
			self.root = z
			z.parent = None
		
		else:
			z.parent = y
			if y.key <= z.key:
				y.right = z
			else:
				y.left = z

	def transplant(self,d,r):
		""" d been delete r replecement"""
		if d.parent == None:
			self.root = r
		elif d == d.parent.left:
			d.parent.left = r
		else:
			d.parent.right = r
		if r!=None:
			r.parent = d.parent
		return d


	def delete(self,node):
		if node.left == None:
			# 如果node.right 是None 相当于把d直接置成None,否则 后继者一定是第一个right值
			return self.transplant(node,node.right)
		elif node.right == None:
			# node.left 一定存在
			return self.transplant(node,node.left)
		else:
			# 比node大的
			successor = self.minimum(node.right)
			if successor != node.right:
				# 最小的左边的值一定不存在
				self.transplant(successor,successor.right)
				# right有变化
				successor.right = node.right
				# 修改原来节点的父节点 node.right 一定存在
				successor.right.parent = successor 
			self.transplant(node,successor)
			successor.left=node.left
			# 修改原子节点的父节点 node.left一定存在
			successor.left.parent = successor
			return node

	def successor(self,node):
		if node == None:
			return None
		if node.right != None:
			# 后继一定在node的右节点
			return self.minimum(node.right)
		y = node.parent
		# 后继几点只能在右节点
		while  y!=None and node != y.right:
			node = y
			y=y.parent
		return y

	def search(self,key,node = None):
		x = self.root if node == None else node
		while  x!=None and x.key != key:
			if  key < x.key:
				x=x.left
			else:
				x=x.right
		return x

	def maximum(self,node=None):
		x = self.root if node == None else node
		while x!=None and x.right!=None:
			x = x.right
		return x

	def minimum(self,node=None):
		x = self.root if node == None else node
		while x!=None and x.left!=None:
			x = x.left
		return x

	# 中序遍历 输出递增数据
	def inorderTreeWalk(self,x):
		if x!=None:
			self.inorderTreeWalk(x.left)
			# python3 语法输出不换行
			print(x.key,end=',')
			self.inorderTreeWalk(x.right)
# 打印的方法
	# 1:先序遍历
	# 2:如果子节点不存在，那么所有子节点的打印空格数和父节点的长度保持一致
	# 3:左右节点只要有一个不存在，就不显示斜杠
	def __str__(self):
		if self.root == None:
			print("<empty tree>")
		def recurse(node):
			if node is None: 
				return [], 0 ,0
			key = str(node.key)
			left_lines ,left_num_pos, left_total_width=recurse(node.left)
			right_lines ,right_num_pos ,right_total_width=recurse(node.right)
			
			# 如果存在子元素 left_total_width - left_num_pos + right_num_pos + 1  加1保证两个子树之间最少存在一个空格，同事斜杠之间和数字的距离能反馈出这个加1
			# 对于倒数第一层和第二层，倒数第一层不存在子元素，倒数第一层左右子节点都只有元素的长度，为了显示好看，横线在两者之间的间隔应该有元素字符串的长度 len(key)
			length_between_slash =  max(left_total_width - left_num_pos + right_num_pos +1,len(key))

			# 数字在的位置 :左子树数字在的位置+斜杠之间
			num_pos= left_num_pos + length_between_slash // 2

			# 由于初始化的时候line_total_width都是0，不能用左边的距离加上右边的距离
			line_total_width= left_num_pos+length_between_slash+(right_total_width - right_num_pos)
			
			# 如果key的长度只有1，则不会替换
			key = key.center(length_between_slash,'.')
			# 由于斜线和点在同一列，会不美观
			if key[0] == '.':key=' ' + key[1:]
			if key[-1] == '.':key=key[:-1]+' '

			parent_line = [' '*left_num_pos +key+' '*(right_total_width- right_num_pos)]
			
			#扣除斜杠占据的位置
			slash_line_str = [' '*(left_num_pos)]
			if node.left is not  None and node.right is  not None:
				slash_line_str.append('/')
				slash_line_str.append(' '*(length_between_slash-2))
				slash_line_str.append('\\')
			elif node.left is None and node.right is not None:
				slash_line_str.append(' '*(length_between_slash-1))
				slash_line_str.append('\\')
			elif node.left is not None and node.right is None:
				slash_line_str.append('/')
				slash_line_str.append(' '*(length_between_slash-1))
			else:
				slash_line_str.append(' '*(length_between_slash))
			slash_line_str.append(' '*(right_total_width- right_num_pos))
			slash_line=[''.join(slash_line_str)]

			while len(left_lines)<len(right_lines):
				# 最上的一层肯定是最长的，下面的每一行保持和最长层的长度一致
				left_lines.append(' '*left_total_width)
			while len(right_lines) < len(left_lines):
				right_lines.append(' '*right_total_width)
			
			child_line = [l+' '*(line_total_width-left_total_width-right_total_width)+r for l , r in zip(left_lines,right_lines)]
			
			value = parent_line+slash_line+child_line
			return value, num_pos, line_total_width
		# list拼接直接换行就行
		return '\n'.join(recurse(self.root)[0])

class Node(object):
	"""docstring for Node"""
	def __init__(self, key,left=None,right=None,parent=None):
		super(Node, self).__init__()
		self.key = key
		self.left = left
		self.right = right
		self.parent = parent

def value(node,msg,notNodeMsg):
	if isinstance(node,Node):
		print(msg,node.key)
	else:
		print(notNodeMsg)

def test(bst):
	key = random.randint(1,100)
	node =bst.search(key)
	value(node,"search result ","Not Found "+str(key))
	node = bst.maximum()
	value(node,"max ","tree is empty")
	node = bst.minimum()
	value(node,"min ","tree is empty")
	key = random.randint(1,100)
	node = bst.searchSuccessor(key)
	value(node,str(key)+" successor is ","successor node not exist "+str(key))
	key = random.randint(1,100)
	dnode = bst.searchDelete(key)
	value(dnode,"delete ","node not exist "+str(key))


if __name__ == '__main__':
	bst = BST()
	for i in range(80):
		node = Node(random.randint(1,1000))
		bst.insertDistinct(node)
	# print("root",bst.root.key)
	# bst.inorderTreeWalk(bst.root)
	print(bst)
	label = "1"
	# print()




		