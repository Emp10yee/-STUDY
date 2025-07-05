tree1= [0, 1, 2, 3, 4, 5, 6, 7, 8]  #0은 dummy값, 완전 이진 트리로 가정(루트: 1)
adult= []
child= []

def tree1_ancestors(tree1_idx): #조상 노드 탐색 함수
    if tree1_idx == 1: #루트에 도달하면 종료
        return 1
    tree1_idx //= 2   #부모 노드 인덱스로 이동
    adult.append(tree1[tree1_idx])
    tree1_ancestors(tree1_idx) #부모 노드에 대해 재귀 호출

def tree1_descendants(tree1_idx): #자손 노드 탐색 함수
    left= tree1_idx * 2          #왼쪽 자식 노드 인덱스
    right= tree1_idx *2 +1       #오른쪽 자식 노드 인덱스

    if left< len(tree1):         #왼쪽 자식 노드 존재 시 추가+다시 자손 탐색
        child.append(tree1[left])
        tree1_descendants(left)
    if right< len(tree1):        #오른쪽 노드도 동일일
        child.append(tree1[right])
        tree1_descendants(right)

tree1_input=int(input('찾을 노드 입력: '))
if tree1_input not in tree1:
    print('노드를 찾을 수 없습니다.')
else: index_num= tree1.index(tree1_input) #인덱스 찾음

tree1_ancestors(index_num)   #탐색 후 결과 출력
tree1_descendants(index_num)

print('조상 노드:', adult)
print('자손 노드:', child)
