class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)
        pass

    def search(self, find_val):
        return self.search_helper(self.root, find_val)
        
    def search_helper(self, current_node, find_val):
        if current_node is None:
            return False
        if find_val == current_node.value:
            return True
        if find_val < current_node.value:
            return self.search_helper(current_node.left, find_val)
        if find_val > current_node.value:
            return self.search_helper(current_node.right, find_val)
        
    def insert_helper(self, current_node, new_val):
        if new_val < current_node.value:
            if current_node.left == None:
                current_node.left = Node(new_val)
            else:
                self.insert_helper(current_node.left, new_val)
            
        if new_val > current_node.value:
            if current_node.right == None:
                current_node.right = Node(new_val)
            else:
                self.insert_helper(current_node.right, new_val)
