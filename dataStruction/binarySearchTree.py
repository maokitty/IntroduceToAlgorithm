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
	def __str__(self):
		if self.root is None: return '<empty tree>'
		def recurse(node):
			if node is None: return [], 0, 0
			# 前序遍历
			label = str(node.key)
			left_lines, left_pos, left_width = recurse(node.left)
			right_lines, right_pos, right_width = recurse(node.right)
			middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
			pos = left_pos + middle // 2
			width = left_pos + middle + right_width - right_pos
			while len(left_lines) < len(right_lines):
				left_lines.append(' ' * left_width)
			while len(right_lines) < len(left_lines):
				right_lines.append(' ' * right_width)
			if (middle - len(label)) % 2 == 1 and node.parent is not None and \
				node is node.parent.left and len(label) < middle:
				label += '.'
			# center 返回指定宽度 width 居中的字符串,用 . 填充 如 label=1,label.center(10,'.')表示 ....1.....
			label = label.center(middle, '.')
			if label[0] == '.': label = ' ' + label[1:]
			if label[-1] == '.': label = label[:-1] + ' '
			# zip 合并两个list成为元组
			lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
			return lines, pos, width
		return '\n'.join(recurse(self.root) [0])

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
	# bst = BST()
	# for i in range(100):
	# 	node = Node(random.randint(1,100))
	# 	bst.insertDistinct(node)
	# print("root",bst.root.key)
	# bst.inorderTreeWalk(bst.root)
	# print(bst)
	label = "1"
	print()




		