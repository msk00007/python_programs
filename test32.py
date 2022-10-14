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
def rsearch(root,key):
    if root is None:
        return
    if root.data == key:
        return root
    elif root.data>key:
        return rsearch(root.left,key)
    else:
        return rsearch(root.right,key)
def Nr_search(root,key):
    if root is None:
        return root
    while(root!=None):
        if root.data == key:
            return root
        elif root.data>key:
            root = root.left
        else:
            root = root.right
    return root

r = None
r=insert(r,5)
r=insert(r,3)
r=insert(r,4)
r=insert(r,31)
r=insert(r,1)
r=insert(r,6)
key = int(input("Enter the key value : "))
result_1 = rsearch(r,key)
if result_1 == None:
    print("Rsearch key is not found")
else:
    print("Rsearch key is found ...")
res_2 = Nr_search(r,key)
if res_2 == None:
    print("Nr_search key is not found")
else:
    print("Nr_search key is found ...")

    