#자료구조 8-16

def SelectionSort_max(num, n): #선택 정렬
    for i in range(0, n-1):
        max_idx = i            #최댓값의 위치 초기화
        for j in range(i+1, n):
            if num[j] > num[max_idx]: #최댓값보다 더 큰 값을 찾으면 update
                max_idx = j
        num[i], num[max_idx] = num[max_idx], num[i] #i의 값과 max_idx의 값을 교환

        print(f"{i+1}단계 : {num}")   #단계마다 swap 후의 배열 출력

arr=[2,93,45,4,30,42]
n= len(arr)
SelectionSort_max(arr, n)
