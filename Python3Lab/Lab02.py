#18 사용자가 연봉과 결혼 여부를 입력하면 다음의
# 세금율에 의해 납부해야 할 세금을 계산하는 프로그램을 작성
salary = int(input('연봉을 입력하세요'))
isMarried = input('결혼여부를 입력하세요 (Y/N)')
tax=0
if isMarried.upper() == 'N':
    if  salary <3000 :
        tax = salary * 0.1
    else : 
        tax = salary * 0.25
else:
    if salary :
        tax= salary*0.1
    else :
        tax = salary*0.25

print(isMarried,salary,tax)



#19다음 조건을 이용해서 현재 연도를 입력하면
# 윤년 여부를 출력하는 프로그램을 작성하세요

year = int(input('윤년여부를 알고 싶은 년도를 입력하세요'))
if year / 4 == 0 and year / 100 !=0 or year /400 == 0 :
    print('%d 는 윤년입니다' % year)
else :
    print('%d 는 윤년이 아닙니다' % year)


# 20다음 조건을 만족하는 복권 발행 프로그램을 작성하세요
#a 사용자로부터 복권 숫자 3자리를 입력받으세요
#b 프로그램상에서 난수 생성을 이용해서 복권 3자리 수를 생성
#c 사용자가 입력한 복권 숫자가 모두 일치 :상금 백만원
#c 사용자가 입력한 복권 숫자가 2개 일치 :상금 1만원
#c 사용자가 입력한 복권 숫자가 3개 일치 :상금 1천원
import random
lotto = str(random.randint(100,999))
lucky = input('복권번호를 입력하세요')
match = 0 #일치여부


if (lucky[0] == lotto[0] or
        lucky[0] == lotto[1] or
        lucky[0] == lotto[2]):
        match+=1
if (lucky[1] == lotto[0] or
        lucky[1] == lotto[1] or
        lucky[1] == lotto[2]):
        match+=1
if (lucky[2] == lotto[0] or
        lucky[2] == lotto[1] or
        lucky[2] == lotto[2]):
        match+=1

print(lotto , lucky , match)

if match == 3:
    print('1등 당첨 : 백만원!!')
elif match ==2:
    print('2등 당첨 :만원!')
elif match ==1:
    print('3등 당첨 : 천원!')
else :
    print('꽝입니다!!')





#21 사용자로부터 숫자 (1 - 9) 를 하나 입력 받아, 구구단을 출력하는 프로그램을 작성해보세요
# 단,  1-9이외의 숫자나 문자를 입력받으면 "잘못입력하셨습니다!!"라는 메시지를 출력하도록 합니다
# 아스키 코드를 이용  0 - 아스키 48  9 - 아스키 57  , ord : 아스키코드로 변환
dan = int(input('몇단을 출력받으시겠습니까'))
if ord(dan[0]) >= ord('0') and ord(dan[0]) <= ord('9'):
    print('구구단 출력')
else:
    print('입력 오류 - 숫자만 입력하세요!!')
#22 입력값을 소문자로 받아 대문자로 출력하는 프로그램을 작성하여라
# 단 숫자나 문자를 입력받으면 잘못입력하셨습니다notnot라는 메세지를 출력하도록 합니다
lower = input('소문자를 입력하세요')
if ord(lower[0]) >= ord('a') and ord(lower[0]) <= ord('z'):
    print(lower.upper())
else:
    print('소문자만 입력가능!!')

#23 다음 조건에 따라 숫자 맞추기 프로그램을 작성해 보세요
#a.사용자로부터 1- 100사이의 숫자를 입력 받으세요 (num1)
#b.컴퓨터는 임의의 숫자를 하나 생성 합니다 (num2)
#c.num1이 num2보다 크면 "추측한숫자가 큽니다" 라고 출력
#d.num1이 num2 보다 작으면 "추측한숫자가 작습니다" 라고 출력
#e. num1과 num2 가 같으면 "빙고not 숫자를 맞췄습니다"라고 출력
#num1>num2이거나num1<num2 이거일경우 다시 실행

loop = True
while loop :
    num1 = int(input('1~100사이의 숫자를 입력하세요'))
    import random
    num2 = random.randint(1,100)
    if num1>num2 :
        print('추측한숫자가 큽니다')
    elif num1<num2 :
        print('추측한숫자가 작습니다')
    elif num1==num2 :
        print('빙고 not 숫자를 맞췄습니다')
        loop = False
    else:
        print('다시시도해주세요!')
#25 임의의 숫자 6자리를 입력하면 신용카드의 종류와 은행정보를 출력하는 프로그램을 작성해보세요





