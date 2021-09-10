# Закодируйте любую строку из трех слов по алгоритму Хаффмана.


from collections import deque

class Node:
    def __init__(self, value, letter=None, left=None, right=None):
        self.value = value
        self.letter = letter
        self.left = left
        self.right = right


def search(node, path='',):
    if node.letter is not None:
        node.value = 0
        return node.letter, path
    if node.right is not None and node.right.value != 0:
        spam = search(node.right, path=f'{path}1')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return spam
    if node.left is not None and node.left.value != 0:
        spam = search(node.left, path=f'{path}0')
        if node.right.value == 0 and node.left.value == 0:
            node.value = 0
        return spam


s = input('Vvedite stroku :\n')

s_dict = {}
for i in s:
    if i not in s_dict:
        s_dict[i] = 1
    else:
        s_dict[i] += 1

node_list = deque([Node(s_dict[i], i) for i in s_dict])

for i in range(len(s_dict)-1):

    node_list = deque(sorted(node_list, key=lambda node: node.value))
    first_el = node_list.popleft()
    second_el = node_list.popleft()
    new_node = Node(first_el.value + second_el.value, left=first_el, right=second_el)
    node_list.appendleft(new_node)

tree = node_list[0]


table = {}
for _ in range(len(s_dict)):
    k = search(tree)
    table[k[0]] = k[1]
del tree

print('Kodirovannaya stroka :')
for char in s:
    print(table[char], end=' ')