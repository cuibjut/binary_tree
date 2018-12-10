#!coding=UTF_8
"""
参考：http://www.cnblogs.com/freeman818/p/7252041.html
"""


class Node:
    """
    如何表达一棵树：
    使用一个类的__init__()方法，方法中含有3个参数，分别是value, left, right, 并为其赋初识值
    """
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def pre_traverse(root):
    """
    前序遍历二叉树
    :param root: root为一颗二叉树
    :return:
    """
    if not root:   # 首先要判断边界条件
        return

    print(root.value, end=" ")
    pre_traverse(root.left)
    pre_traverse(root.right)


def mid_traverse(root):
    """
    中序遍历二叉树
    :param root: root为一颗二叉树
    :return:
    """
    if not root:
        return

    mid_traverse(root.left)
    print(root.value, end=" ")
    mid_traverse(root.right)


def after_traverse(root):
    """
    后序遍历二叉树
    :param root: root为一颗二叉树
    :return:
    """
    if not root:
        return

    after_traverse(root.left)
    after_traverse(root.right)
    print(root.value, end=" ")


def traverse(root):
    """
    二叉树的层次遍历
    :param root:
    :return: 返回一颗按层次遍历的二叉树
    """

    # 基本上都是用两个list来实现的，一个是用来存储值，一个是用来存储指针的
    if not root:
        return

    q = [root]
    result = [root.value]
    while len(q) != 0:
        pop_node = q.pop(0)
        if pop_node.left is not None:
            q.append(pop_node.left)
            result.append(pop_node.left.value)
        if pop_node.right is not None:
            q.append(pop_node.right)
            result.append(pop_node.right.value)
    return result






if __name__ == "__main__":
    root = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
    print("前序遍历:")
    pre_traverse(root)

    print("\n---------------------\n")

    print("中序遍历:")
    mid_traverse(root)

    print("\n---------------------\n")

    print("后序遍历:")
    after_traverse(root)

    traverse(root)
    print("层次遍历：", traverse(root))
