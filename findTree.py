"""
1.根据前序，中序遍历二叉树的顺序求后序遍历二叉树顺序
2.根据后序，中序遍历二叉树的顺序求前序遍历二叉树顺序
"""


def find_last_tree(prelist, midlist, lastlist):
    """
    首先写出递归的终止条件及边界条件
    :param prelist: 先序遍历树的list
    :param midlist: 中序遍历树的list
    :param lastlist: 后序遍历树的list
    :return: 通过先序和后序遍历返回树的后序遍历结果
    """
    if len(prelist) == 0:  # 判断边界
        return
    if len(prelist) == 1:   # 递归终止条件
        lastlist.append(prelist[0])
        return

    value = prelist[0]

    n = midlist.index(value)
    find_last_tree(prelist[1:n+1], midlist[0:n], lastlist)
    find_last_tree(prelist[n+1:], midlist[n+1:], lastlist)

    lastlist.append(value)  # 要构造一颗后序遍历二叉树，把先序遍历的中的先根节点最后加到树种

    return lastlist


def find_pre_tree(lastList, midList, preList):
    if len(lastList) == 0:  # 判断边界条件
        return
    if len(lastList) == 1:  # 递归终止条件
        preList.append(lastList[0])
        return

    value = lastList[-1]

    preList.append(value)

    n = midList.index(value)
    print(lastList[0:n], midList[0:n], preList)
    find_pre_tree(lastList[0:n], midList[0:n], preList)
    find_pre_tree(lastList[n:-1], midList[n+1:], preList)
    return preList


if __name__ == "__main__":
    # preList = list('12473568')
    # midList = list('47215386')
    # lastList = []
    # lastList = find_last_tree(preList, midList, lastList)
    # print(lastList)

    lastList = list('74258631')
    midList = list('47215386')
    preList = []
    preList = find_pre_tree(lastList, midList, preList)
    print(preList)
