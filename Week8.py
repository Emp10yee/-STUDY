#자료구조 8-15
#프로그램 8.4 코드를 활용함 

class ShellSort: #쉘 정렬
    def __init__(self, num): #정렬할 리스트, 리스트 크기 저장
        self.num = num
        self.size = len(num)
        print("Shell Sort:", self.num) #초기 리스트 출력

    def sort(self): #정렬 함수
        n= len(self.num) 
        num= self.num
        gap= n//2
        if gap % 2 == 0: gap+= 1 #gap을 홀수로 설정
        while gap > 0: #gap이 1이 될 때까지 반복
            print("\ngap:", gap)
            for i in range(gap, n):
                temp = num[i] #현재 위치 값 저장
                j= i
                flag= False
                while j >= gap and num[j-gap] > temp: #원소들 비교하며 위치 찾기
                    num[j] = num[j-gap]
                    j-=gap     #인덱스 gap만큼 뒤로 이동
                    flag= True #이동이 발생함
                num[j]=temp
                if flag: #이동이 발생하면 update된 배열 출력
                    print(num)
            gap //= 2
            if gap % 2==0 and gap>1: gap+= 1
        print("\n", self.num) #최종 정렬 리스트 출력

A= [77, 62, 80, 40, 30, 21, 14, 25, 9]

shell_sorter = ShellSort(A)
shell_sorter.sort()
