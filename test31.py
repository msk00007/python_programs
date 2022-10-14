class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def insert(root,data):
    new_node = node(data)
    if root == None:
       root = new_node
    else:
        prev = None
        temp = root
        while temp != None:
            if temp.data>data:
                prev = temp
                temp = temp.left
            elif temp.data<data:
                prev = temp
                temp = temp.right
        if prev.data>data:
            prev.left = new_node
        else:
            prev.right = new_node
    return root
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
def preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if root is None:
        return
    preorder(root.left)
    preorder(root.right)
    print(root.data,end=" ")
r = None
r=insert(r,5)
r=insert(r,3)
r=insert(r,4)
r=insert(r,31)
r=insert(r,1)
r=insert(r,6)
print("\nthe in order of this bst is ")
inorder(r)
print("\nthe post order of this bst is :")
postorder(r)
print("\nthe pre order of this bst is :")
preorder(r)
print("\n The root data is ",r.data)

    

