def get_post_order(n, inorder, preorder):
    if not inorder:
        return []
    if n == 1:
        return [preorder[0]]

    root = preorder[0]
    root_index = inorder.index(root)

    left_subtree = get_post_order(root_index, inorder[:root_index], preorder[1:root_index + 1])
    right_subtree = get_post_order(n - root_index - 1, inorder[root_index + 1:], preorder[root_index + 1:])

    return left_subtree + right_subtree + [root]

n = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))

postorder = get_post_order(n, inorder, preorder)
print(" ".join(map(str, postorder)))