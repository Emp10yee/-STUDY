#2-17(1) 볼링
frame = []
total = 0
R = []   #결과 기호 따로 저장

for i in range(10):
  first, second = map(int, input('(입력) %d프레임 : ' % (i + 1)).split())
  f_total = first + second

  if first == 10:  #결과 기호 지정
      result = 'X'
      second = 0
  elif f_total == 10:
      result = '/'
  else:
      result = '-'

  frame.append((first, second, result, f_total)) #튜플
  R.append(result) #편의성을 위해 결과 기호만 따로 모아둠

  # i=0일 때 R[-1]이 되지 않도록 i>0 조건을 걸어줌
  if i > 0 and R[i-1] =='X': #스트라이크 보너스 처리
    temp=frame[i-1]
    updated=temp[3]+f_total
    frame[i-1] = (temp[0], temp[1], temp[2], updated)
    #튜플은 수정이 되지 않으므로 temp를 통해 통째로 변경해준다
    if i > 1 and R[i-2] =='X': #더블 스트라이크 처리
      temp2=frame[i-2]
      updated2 =temp2[3]+first
      frame[i-2] = (temp[0], temp[1], temp[2], updated2)
  
  if i>0 and R[i-1]=='/': #스페어 보너스 처리
    temp=frame[i-1]
    updated=temp[3]+first
    frame[i-1] = (temp[0], temp[1], temp[2], updated)

  total = sum(f[3] for f in frame)
  print(frame)
  print('Total =', total)
  print()


bonus = R[-1]
if bonus in ['X', '/']: #보너스 프레임
  first, second = 0, 0
  if bonus == 'X':
    first, second = map(int, input('(입력) 보너스 프레임 : ').split())
    frame.append((first, second, 'X', first+second))
    
    temp=frame[-2]
    updated=temp[3]+first+second
    frame[-2]=(temp[0], temp[1], temp[2], updated)

  elif bonus == '/':
    first = int(input("(입력) 보너스 프레임 : "))
    frame.append((first, second, '/', first+second))
    
    temp=frame[-2]
    updated=temp[3]+first
    frame[-2]=(temp[0], temp[1], temp[2], updated)

  b_total = sum(f[3] for f in frame)
  print(frame)
  print('Total =', b_total)


bonus = R[-1] 
if bonus in ['X', '/']: #보너스 프레임
  first, second = 0, 0
  if bonus == 'X':
    first, second = map(int, input('(입력) 보너스 프레임 : ').split())
    temp=frame[-1]
    updated=temp[3]+first+second
    frame[-1] = (first, second, '-', updated)
    total += first+second
  
  elif bonus == '/':
    first = int(input("(입력) 보너스 프레임 : "))
    temp=frame[-1]
    updated=temp[3]+first
    frame[-1] = (first, second, '-', updated)
    total+= first
  
  frame.append((first, second, '-', first+second))
  b_total = sum(f[3] for f in frame)
  print(frame)
  print('Total =', b_total)