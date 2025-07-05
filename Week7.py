#자료구조 8-11
#다음 수에 대해 추가 배열 없이 quick sort 알고리즘을 수행하시오.
#(1)[9,58,3,25,50,34,20,48,11,2,16]   (2)[25,30,17,14,49,66,23,39]

class QuickSort:
    def __init__(self, num): #정렬 리스트 및 길이 저장
        self.num=num
        self.size=len(num)
        print("Quick Sort", self.num)
    
    def swap(self, a, b):    #swap 함수
        self.num[a], self.num[b]= self.num[b], self.num[a]

    def sort(self, left, right): 
        if left<right: #원소가 2개 이상일 때만 정렬(1개는 할 필요가 없다)
            i=left; j=right+1
            pivot=self.num[left]
            while True:
                while True: #i를 이동시키면서 pivot보다 같거나 큰 값 탐색
                    i+=1
                    if i>right or num[i] >=pivot: break
                while True: #j를 이동시키면서 pivor보다 같거나 작은 값 탐색
                    j-=1
                    if j<left or num[j] <=pivot: break
                if i<j: self.swap(i, j) #i<j이면 두 값 swap
                else: break             #i>=j이면 break
            
            self.swap(left, j)            #pivot을 위치로 이동
            if left != j: print(self.num) #중간과정 출력
            self.sort(left,j-1)   #pivot의 왼쪽 부분 정렬(재귀)
            self.sort(j+1, right) #pivot의 오른쪽 부분 정렬(")

num=[25,30,17,14,49,66,23,39]
n=QuickSort(num)
n.sort(0, len(num)-1)
