word = input()
n = len(word)            #문자열 길이
result_array = [''] * n  #결과를 저장할 배열
visited = [False] * n    #방문 여부 확인하는 배열

def permutation(depth):
    if depth == n:       #모든 글자를 다 골랐다면 출력하고 종료
        print("".join(result_array), end=" ")
        return 0
    
    for i in range(n):         #방문하지 않은 글자라면 선택
        if not visited[i]:
            visited[i] = True  #방문 체크
            result_array[depth] = word[i] #현재 깊이에 문자 저장
            permutation(depth + 1)        #다음 깊이 탐색
            visited[i] = False #다음에 방문할 때 문자 다시 선택할 수 있도록 초기화


permutation(0) #순열 생성
