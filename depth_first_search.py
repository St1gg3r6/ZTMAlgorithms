class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{{'value': {self.value}, 'left': {self.left}, 'right': {self.right}}}"

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def __repr__(self):
        return str(self.root)

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            current_node = self.root
            while current_node != None:
                if current_node.value == value:
                    break
                if value < current_node.value:
                    if current_node.left == None:
                        current_node.left = new_node
                    current_node = current_node.left
                else:
                    if current_node.right == None:
                        current_node.right = new_node
                    current_node = current_node.right

    def lookup(self, value):
        if not self.root:
            return None
        current_node = self.root
        while current_node != None:
            if current_node.value > value:
                current_node = current_node.left
            elif current_node.value < value:
                current_node = current_node.right
            elif current_node.value == value:
                return current_node
        return None
                
    def remove(self, value):
        if not self.root:
            return None
        current_node = self.root
        parent_node = None
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif current_node.value == value:
                if not current_node.right:
                    if not parent_node:
                        self.root = current_node.left
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.left
                elif not current_node.right.left:
                    current_node.right.left = current_node.left
                    if not parent_node:
                        self.root = current_node.right
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right
                else:
                    leftmost = current_node.right.left
                    leftmost_parent = current_node.right
                    while leftmost.left:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left
                    leftmost_parent.left = leftmost.right
                    leftmost.left = current_node.left
                    leftmost.right = current_node.right
                    if not parent_node:
                        self.root = leftmost
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = leftmost
                        elif current_node.value > parent_node.value:
                            parent_node.right = leftmost
                return True
            
    def depth_first_search_in_order(self):
        return self.traverse_in_order(self.root, [])

    def depth_first_search_pre_order(self):
        return self.traverse_pre_order(self.root, [])

    def depth_first_search_post_order(self):
        return self.traverse_post_order(self.root, [])

    def traverse_in_order(self, node, list):
        if node.left:
            self.traverse_in_order(node.left, list)
        list.append(node.value)
        if node.right:
            self.traverse_in_order(node.right, list)
        return list
    
    def traverse_pre_order(self, node, list):
        list.append(node.value)
        if node.left:
            self.traverse_pre_order(node.left, list)
        if node.right:
            self.traverse_pre_order(node.right, list)
        return list
    
    def traverse_post_order(self, node, list):
        if node.left:
            self.traverse_post_order(node.left, list)
        if node.right:
            self.traverse_post_order(node.right, list)
        list.append(node.value)
        return list
    

bst = BinarySearchTree()
vals = [9, 4, 6, 20, 170, 15, 1]
for val in vals:
    bst.insert(val)

print(bst.depth_first_search_in_order())
print(bst.depth_first_search_pre_order())
print(bst.depth_first_search_post_order())
