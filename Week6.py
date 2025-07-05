#6-11 
#이진 트리에 존재하는 노드의 총 개수를 출력하는 프로그램을 작성하시오

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def count_nodes(root): #노드 개수 count 함수
    if not root:       #노드가 존재하지 않으면 0 반환
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right) #재귀

#노드 개수가 4개인 트리를 만들고 노드 개수를 출력해보자...
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
print("노드의 총 개수:", count_nodes(root))

#이번에는 노드 개수가 6개인 트리로 확인해보자...
root= Node(1)
root.left= Node(2)
root.right= Node(3)
root.left.left=Node(4)
root.left.right= Node(5)
root.right.right= Node(6)
print("노드의 총 개수:", count_nodes(root))
