from Node import *

def insert(start, data):

	if start is None:
		return Node(data)

	if data < start.data:
		start.left = insert(start.left, data)

	elif data > start.data:
		start.right = insert(start.right, data)
		
	return start

def bst_max(start):

	if not isinstance(start, Node):
		raise ValueError('Not a node!')

	if start.data == None:
		raise ValueError('Empty!')

	if start.right == None:
		return start.data

	while(start.right):
		start = start.right

	return start.data

def bst_min(start):

	if not isinstance(start, Node):
		raise ValueError('Not a node!')

	if start.data == None:
		raise ValueError('Empty!')

	if start.left == None:
		return start.data

	while(start.left):
		start = start.left

	return start.data

root = Node(7)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 11)
root = insert(root, 2)
print bst_min(root)
print bst_max(root)