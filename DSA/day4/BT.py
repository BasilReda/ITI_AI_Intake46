class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
    
    def inorder_traversal(self):
        values = []
        if self.left:
            values.extend(self.left.inorder_traversal())
        values.append(self.value)
        if self.right:
            values.extend(self.right.inorder_traversal())
        return values
    
    def preorder_traversal(self):
        values = []
        values.append(self.value)
        if self.left:
            values.extend(self.left.preorder_traversal())
        if self.right:
            values.extend(self.right.preorder_traversal())
        return values
        
    def postorder_traversal(self):
        values = []
        if self.left:
            values.extend(self.left.postorder_traversal())
        if self.right:
            values.extend(self.right.postorder_traversal())
        values.append(self.value)
        return values

    def inorder_preorder(self, inorder, preorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.inorder_preorder(inorder[:mid], preorder[1: mid+1])
        root.right = self.inorder_preorder(inorder[mid+1:], preorder[mid+1:])
        return root
    
    def inoreder_postorder(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.inoreder_postorder(inorder[:mid], postorder[:mid])
        root.right = self.inoreder_postorder(inorder[mid+1:], postorder[mid:-1])
        return root


tree = TreeNode(10)
tree.insert(5)
tree.insert(15)
tree.insert(8)
tree.insert(2)
tree.insert(18)
tree.insert(12)
preorder = tree.preorder_traversal()
inorder = tree.inorder_traversal()
postorder = tree.postorder_traversal()
inorder_preorder = tree.inorder_preorder(inorder, preorder)
inorder_postorder = tree.inoreder_postorder(inorder, postorder)
print(f"preorder trav:{preorder}\n")
print(f"inorder trav:{inorder}\n")
print(f"postorder trav:{postorder}\n")
print(f"inorder_preorder:{inorder_preorder.inorder_traversal()}\n")
print(f"inorder_postorder:{inorder_postorder.inorder_traversal()}\n")