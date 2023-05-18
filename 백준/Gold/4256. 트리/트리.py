import sys
input = sys.stdin.readline
 
 
def postorder(preorder, inorder):
    if len(preorder) == 0:
        return
    if len(preorder) == 1:
        result.extend(preorder)
        return
        
    root = preorder[0]
    inorderidx = inorder.index(root)
    
    postorder(preorder[1:inorderidx+1], inorder[:inorderidx])
    postorder(preorder[inorderidx+1:], inorder[inorderidx+1:])
    result.append(root)
 
 
T = int(input())
for _ in range(T):
    result = []
    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder(preorder, inorder)
    print(*result)