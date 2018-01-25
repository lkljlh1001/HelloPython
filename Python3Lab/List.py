#파이썬 자료구조
#리스트 : sequence 자료구조를 사용
#sequence : 순서가 있는 데이터 구조를 의미
#리스트, 튜플, 레인지, 문자열 등이 sequence 구조 사용
#리스트는 []을 이용해서 각 요소에 접근할 수 있다

#문자열
msg = 'Hello, World!!'


#파이썬에서는 자료구조를 의미하는 접미사를
#변수명에 사용하기도 한다

list1_list=[]            #빈 리스트
list2_list=[1,2,3,4,5]   #숫자
list3_list=['a','b','c'] #문자
list4_list=['a','b','c',1,2,3,True] #혼합

print(list1_list)

#간단한 연산
#요소 존재 여부 파악 : in/not in 연산자
print(1 in list1_list)
print('a' in list1_list)
print(3 in list2_list)

#길이 연산 : len()
print(len(list1_list))
print(len(list2_list))

#연결 연산 : +
print(list2_list + list3_list)

#반복 연산 : *
print(list2_list * 2)

#요소의 특정값 참조 : index 사용
print(msg[5],msg[7])
print(list2_list[2])
print(list3_list[2])
print(list4_list[5])

#요소값 변경 : index, = 사용
list2_list[2] = -3
print(list2_list)

#주민 코드에서 성별 여부 판별
jumin=[1,2,3,4,5,6,1,2,3,4,5,6,7]

if jumin[6] == 1 :
    print('남자입니다')
else :
    print('여자입니다')

#주민코드에서 생년월일 추출
for i in range(0,6):
    print(jumin[i], end=' ')    # end =' ' 줄바꿈없이 출력시 종결문자를 지정


#특정범위내 요소들을 추출할때는 슬라이스를 사용 [i:j]
print(jumin[0:6])       # 생년월일
print(jumin[:6])        # 시작 위치부터
print(jumin[6:])        # 6번째 인덱스에서 부터 나머지
print(jumin[:])         # 모두출력

print(jumin[0:6:2])     # 홀수자리만 추출
print(jumin[::-1])      # 역순 출력


#print(jumin[100])       # 인덱스 초과 - 오류
#print(jumin[0:100:2])   # 인덱스 초과 - 오류

#리스트 관련 통계 함수
print(sum(list2_list))   # 합
print(min(list2_list))   # 최소
print(max(list2_list))   # 최대


#리스트가 주어지면
# 이것의 가운데에 있는 요소 값을 출력

#list = [1,2,3,4,5]
list = [1,2,6,8,4,10]
size = len(list)
mid=int(size / 2)
print('가운데 값:',list[mid])         #요소 수가 홀수
print('가운데 값:',list[mid-1:mid+1]) #요소 수가 짝수

def listcenter(list):
    size = len(list)
    mid = int(size/2)
    if size %2 == 0 : #짝수인경우
        print(list[mid-1:mid+1])
    else:
        print(list[mid])

listcenter([1,2,3])
listcenter([1,2,3,4])

# 리스트 조작 함수
# 요소 추가 : append

list = [1,2,3,4,5]
list.append(9)
list.append(8)
print(list)

# 요소 추가 : insert(위치, 값)
list.insert(6, 7)
print(list)

# 요소 제거 : remove(값), 왼쪽부터 검색 후 삭제
list.remove(9)
print(list)

# 요소 제거 : pop(), pop(위치)
list.pop(5)
print(list)

list.pop() # 마지막 요소 제거
print(list)

# 모두 제거 : clear()
list.clear()
print(list)