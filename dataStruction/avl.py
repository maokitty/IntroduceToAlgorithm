import random
class Node(object):
	def __init__(self,key,right=None,left=None,parent=None):
		self.right = right
		self.left = left 
		self.parent = parent
		self.key = key

  # 树是单独的结构，BST用来操作BST树，确保BST的性质不会有改变
class AvlBST(object):
	"""左子树的值小于父子树的值小于等于右子树的值
	最坏情况是：成为一条链
	"""
	def __init__(self):
		self.root = None

	def insert(self,key):
		node = Node(key)
		x = self.root
		xParent = None
		while  x!=None:
			xParent = x
			if node.key< x.key:
				x=x.left
			else:
				x = x.right
		if xParent == None:
			self.root = node
			return node
		node.parent = xParent
		if node.key<xParent.key:
			xParent.left = node
		else:
			xParent.right = node
		return node

	def maximum(self,node = None):
		startPosition = self.root if node is None else node
		while startPosition is not None and startPosition.right is not None:
			startPosition = startPosition.right
		return startPosition
	
	def minimun(self,node = None):
		startPosition = self.root if node is None else node
		while startPosition is not None and startPosition.left is not None:
			startPosition = startPosition.left 
		return startPosition

	def search(self,key):
		node = self.root
		while node is not None and node.key != key:
			if key <node.key:
				node = node.left
			else:
				node = node.right
		return node


	# 在没有重复的BST中,比key要大的最小的节点
	def successor(self,key,node = None):
		node = self.search(key) if node is None else node
		if node is not None:
			if node.right is not None:
				return self.minimun(node.right)
			nodeP = node.parent
			while nodeP is not None and node != nodeP.left:
				node = nodeP
				nodeP=node.parent
			return nodeP
		return None

	# ’_‘开头表示是内部实现 
	def _translate(self,delete,replace):
		deleteP = delete.parent
		if deleteP == None:
			self.root = replace 
		elif delete == deleteP.left:
			deleteP.left = replace
		else:
			deleteP.right = replace
		if replace!=None:
			replace.parent = deleteP
		return delete
	
	#左子树和右子树都存在是时需要找后继节点，如果后继节点不是要删除节点的右节点，需要再删除一次
	def delete(self,key,node=None):
		node = self.search(key) if  node is None else node
		if node is None:
			return node
		if node.right is None:
			return self._translate(node,node.left)
		elif node.left is None:
			return self._translate(node,node.right)
		else:
			successor = self.minimun(node.right)
			if successor != node.right:
				self._translate(successor,successor.right)
				successor.right = node.right
				node.right.parent = successor
			self._translate(node,successor)
			node.left.parent = successor
			successor.left = node.left
			return successor


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

class Avl(AvlBST):
	"""
	高度平衡的二叉查找树
	左子树的值小于父子树的值小于右子树的值,同时每个左子树的高度与右子树的高度差值不大于1
		情况1:
			1  
			\  
			 2 
			  \ 
			   3
			左旋
			2  
			/\ 
			1 3
		情况2:
			 3 
			/  
		   1  
			\  
			 2
		   对1进行左旋
		       3 
			  / 
		     2  
			/  
		   1
		   再右旋
		    2  
			/\ 
			1 3
		情况3:
			   3 
			  / 
			 2  
			/  
		   1 
			右旋
			2  
			/\ 
			1 3
		情况4:
			1  
			 \ 
			  3 
			 / 
			2
			右旋：
			1  
			 \  
			  2 
			  \ 
			   3
			左旋:
			2  
			/\ 
			1 3
	"""
	def __init__(self):
		super(Avl, self).__init__()
	def _height(self,node):
		if node is None:
			return -1
		else:
			return node.height

	def _update_height(self,node):
		node.height = max(self._height(node.left),self._height(node.right))+1

	def insert(self,key):
		node=super().insert(key)
		self._reblance(node)
	
	def _reblance(self,node):
		while node is not None:
			self._update_height(node)
			if self._height(node.left) - self._height(node.right) >=2:
				nodeL = node.left 
				if self._height(nodeL.left) < self._height(nodeL.right):
					self._left_roate(nodeL)
				self._right_roate(node)
			elif self._height(node.right) - self._height(node.left) >=2:
				nodeR = node.right 
				if self._height(nodeR.left) > self._height(nodeR.right):
					self._right_roate(nodeR)
				self._left_roate(node)
			node = node.parent
 
	def _right_roate(self,node):
		'''当前节点的左节点高度-右节点高度>=2
		右旋表示左边节点高
		'''
		pivot=node.left		
		pivot.parent = node.parent
		if node == self.root:
			self.root=pivot
		else:
			if node.parent.left is node:
				pivot.parent.left = pivot
			else:
				pivot.parent.right = pivot
		node.parent = pivot
		tempNode = pivot.right 
		pivot.right = node
		node.left = tempNode
		if tempNode is not None:
			tempNode.parent = node
		
		self._update_height(pivot)
		self._update_height(node)


	def _left_roate(self,node):
		'''当前节点的右节点高度-左节点高度>=2
		从上到下，按照父子一对一对处理
		'''
		pivot = node.right
		pivot.parent = node.parent 
		if node == self.root:
			self.root = pivot
		else:
			if node.parent.left is node:
				pivot.parent.left = pivot
			else:
				pivot.parent.right = pivot
		tempNode = pivot.left
		pivot.left = node
		node.parent = pivot
		node.right = tempNode
		if tempNode is not None:
			tempNode.parent = node
		self._update_height(pivot)
		self._update_height(node)





class AvlNode(Node):
	def __init__(self,key,right=None,left=None,parent=None):
		super(AvlNode,self).__init__()
		self.height=0

if __name__ == '__main__':
	def testBST():
		bst=AvlBST()
		for x in range(1,60):
			bst.insert(random.randint(1,1000))
		val(bst.maximum(),"bst maximum:","empty bst")
		val(bst.minimun(),"bst minimun:","empty bst")
		bst.insert(23)
		val(bst.search(23),"search result","key:"+str(23)+"not exist")
		bst.insert(200)
		bst.insert(210)
		bst.insert(209)
		bst.insert(202)
		bst.insert(214)
		bst.insert(216)
		val(bst.successor(200),"successor is:","key:"+str(200)+"successor not exist")
		val(bst.successor(216),"successor is:","key:"+str(216)+"successor not exist")
		val(bst.delete(210),"delete is:","key:"+str(210)+" not exist")
		print(bst)
	def val(node,msg,reason):
		print(msg,node.key) if node is not None else print(reason)
	
	def testAVL():
		avl = Avl()
		for x in range(1,40):
			avl.insert(random.randint(1,1000))
		print(avl)
	testAVL()




		





