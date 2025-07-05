class Node:
    def __init__(self, item):
        self.data=item
        self.link= None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def view(self): #리스트 출력 함수
        temp=self.head
        print('[', end='')
        while temp:
            print(temp.data, end ='')
            temp = temp.link
        print(']')
    
    def attach(self, item): #노드 연결 함수
        node = Node(item)
        if not self.head:   #리스트가 비어있는 경우
            self.head=node
            self.tail=node
        elif self.tail:     #리스트가 안비어있는 경우
            self.tail.link = node
            self.tail = node

    def delete(self): #노드 삭제 함수
        node=self.head
        if not self.head: #리스트가 비어있는 경우 끝
            print('리스트 삭제 완료')
            return
        
        if self.head ==self.tail: #노드 하나 남은 경우
            self.head = self.tail = None
        
        else: self.head = self.head.link 
        del node


linked = SinglyLinkedList()

print('연결리스트 생성')
for i in range(5):
    linked.attach(i+1)
linked.view()

print('연결리스트 삭제')
for i in range(5):
    linked.delete()
linked.view()