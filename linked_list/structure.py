class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)

class LinkedList:
	def __init__(self, head=None):
		self.head = head

	def add_to_last(self, node):
		current_node = self.head
		if current_node is None:
			self.head = node
		else:
			while current_node.next is not None:
				current_node = current_node.next
			current_node.next = node

	def add_to_first(self, node):
		self.head, node.next = node, self.head

	def remove_from_first(self):
		self.head = self.head.next

	def remove_from_last(self):
		current_node = self.head
		prev=None
		while current_node.next is not None:
			prev = current_node
			current_node = current_node.next
		prev.next = None

	def show(self):
		current_node = self.head
		# print(current_node.data, end='-->')
		# while current_node.next is not None:
		# 	current_node = current_node.next
		# 	print(current_node.data, end='-->')
		while current_node:
			print(current_node.data, end='--->')
			current_node = current_node.next
		print()

ll = LinkedList()
ll.add_to_last(Node(10))
ll.add_to_last(Node(20))
ll.add_to_last(Node(30))
ll.show()
ll.add_to_first(Node(0))
ll.show()
ll.add_to_first(Node(-10))
ll.show()
ll.remove_from_first()
ll.show()
ll.remove_from_last()
ll.show()
ll.remove_from_last()
ll.show()