import random
class Node(object):
	def __init__(self,key,right=None,left=None,parent=None):
		self.right = right
		self.left = left 
		self.parent = parent
		self.key = key

  # 树是单独的结构，BST用来操作BST树，确保BST的性质不会有改变
class AvlBST(object):
	"""左子树的值小于父子树的值小于等于右子树的值"""
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
		if node.key<xParent.key:
			xParent.left = node
		else:
			xParent.right = node

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
	"""左子树的值小于父子树的值小于右子树的值,同时每个左子树的高度与右子树的高度差值不大于1"""
	def __init__(self, arg):
		super(Avl, self).__init__()
		self.arg = arg

if __name__ == '__main__':
	def test():
		bst=AvlBST()
		for x in range(1,40):
			bst.insert(random.randint(1,1000))
		print(bst)
	test()




		





