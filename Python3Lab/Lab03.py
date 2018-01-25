#               ((**lab01 ~ lab02의 예제를 함수로 작성**))
#<이름 짓기>
# 파스칼 표기법 : 첫단어를 대문자로 시작하며 이름을 지음
#       ex) Employees, Departments
#           RegisterEmployee,JoinMember
# 카멜 표기법 : 첫단어를 소문자로 시작하며 이름을 지음
#       ex) registerEmployee
# 스네이크 표기법 : 소문자와 _기호를 이용해서 이름을 지음
#       ex) register_employee
# 헝가리안 표기법 : 자료형을 의미하는 접두사를 이용해서 이름을 지음
#       ex) strName,isMarried,boolMarried




#8 생활속 문제를 파이썬으로 풀기
# 자취방을 구하는데 마음에드는 방 두개를 찾았다 .
# 방 A 는 가로2.5m 세로 3m 이고 월세 27만원이다.
# 방 B 는 가로 4m 세로 2m 이고 월세 30만원이다.

def compareRoom(width,height,price):
    return (width*height)/price

roomA = compareRoom(2.5, 3, 27)
roomB = compareRoom(4, 2, 30)

if(roomA > roomB):
    print('방A가 낫네요')
else:
    print('방B가 낫네요')


#10 주식회사 선박중공업은 한해 동안 철강 석유 등의
# 원자재(불변자본)를 구매하는데 30억원을,
#  노동자를 고용(가변자본)하는 데
# 15억원을 사용했다. 선방중공업은
# 이를 통해 선박을 제조/판매 하여
# 45억원의 순수익(잉여가치)을 냈다.
# 선박중공업의 한해 이윤율을 다음
# 송식을 이용해서 계산하세요
# 이윤율 = 잉여가치액/(불변자본 + 가변자본)

def computeProfit():
    c=int(input('불변자본을 입력하세요'))
    v=int(input('가변자본을 입력하세요'))
    s=int(input('잉여가치액을 입력하세요'))

    return (c+v)/s

print(computeProfit())





#11한국에 사는 당신은 외국 인터넷 쇼핑몰에서 노트북을 구매하려 한다.
# 이쇼핑몰에서는 달러(USD) 또는 유(EUR)료로 결제할 수 있고
# 노트북의 가격은 780달러 또는 650 유로다.
# 달러로 사는것과 유로로 사는것중 어느쪽이 더저렴한다?
# 이 문제를 파이썬 프로그램을 작성하여
# 해결하고 인터넷 검색을 현재의 '달러->원' 환율과
# '유로->원' 환율을 조사한 후 계산하세요
# --------------------------------------------------------
# 달러환율 = 1071
# 유로환율 = 1309

def getExchageRate(country):
    rate=0
    if country =='us':
        rate=1071
    elif country =='euro':
        rate=1309
    return rate

buyUS=780*getExchageRate('us')
buyEuro = 650*getExchageRate('euro')

print(buyEuro,buyUS)

if buyUS > buyEuro:
    print('유로화로 구입하는게 더 싸네요')
else:
    print('달러로 구입하는게 더 싸네요')


# 12당신이 다니는 학교의 운동장은 원형이고 지름이 100m다.
# 어느 체육 시간, 두 명씩 나란히 운동장을 한바퀴 달리는 시합을 하게 되었다.
# 그런데 안쪽선수는 바깥쪽선수보다 5m 안쪽에서 달린다.
# 당신은 바깥족에서 달리는 선수가 불리하다고 이의를 제기했다
# 바깥쪽 선수가 안족 선수보다 몇 미터 더달려야 하기 때문인가?
# 이 문제를 파이썬 프로그램을 작성하여 해결해 보자
# ----------------------------------------------------------------
# 원형 지름이 100m
# 안쪽선수는 바깥쪽 선수보다 5m 안쪽에서 달린다.
# 바깥쪽에서 달리는 서순사 불리하다고 이의를 제기함
# 바깥쪽 선수가 안쪽 선수보다 몇 미터 더달려야 하기때문인가
# pi * r

def howManyRun(radius):
    pi = 3.14
    return radius * pi

studentA = howManyRun(100)
studentB = howManyRun(90)

print('학생 A는 학생 B보다 %d만큼 더 뜀' % (studentA-studentB))


# 17 사용자로부터 두 개의 정수를 입력받아 사칙연산 계산 결과를 출력하는 프로그램을 작성해 보자.
#  예를 들어, 사용자가 입력한 수가 10과 20일떄, 프로그램의 실행 결과는 다음과 같다.
# 첫번째 정수를 입력하세요
#     10
# 두번째 정수를 입력하세요
#     20
# 10+20=30
# 10-20= -10
# 10*20=200
# 10/20 =0.5

def intCalu():
    num1=int(input('좌변값을 하나 입력하세요'))
    num2=int(input('우변값을 하나 입력하세요'))
    fmt ="%d + %d = %d \n %d - %d = %d\n"
    fmt +="%d * %d = %d \n %d / %d = %d\n"
    fmt +="%d ** %d = %d"
    print(fmt % (num1,num2,num1+num2,\
               num1,num2,num1-num2,\
               num1,num2,num1*num2,\
               num1,num2,num1/num2,\
               num1,num2,num1**num2,))
intCalu()

#18 사용자가 연봉과 결혼 여부를 입력하면 다음의
# 세금율에 의해 납부해야 할 세금을 계산하는 프로그램을 작성
def computeTax():
    salary = int(input('연봉을 입력하세요'))
    isMarried = input('결혼여부를 입력하세요 (Y/N)')
    tax=0
    if isMarried.upper() == 'N':
        if  salary <3000 :
            tax = salary * 0.1
        else :
            tax = salary * 0.25
        isMarried ="아니오"
    else:
        if salary :
            tax= salary*0.1
        else :
            tax = salary*0.25
        isMarried ="예"

    fmt = "연봉 : %d, 결혼여부 : %s,세금:%.1f"
    print(fmt % (salary,isMarried,tax))

computeTax()


# 19다음 조건을 이용해서 현재 연도를 입력하면
# 윤년 여부를 출력하는 프로그램을 작성하세요
def isLeapYear():
    year = int(input('윤년여부를 알고 싶은 년도를 입력하세요'))
    isleap = '윤년아닙니다'
    if year / 4 == 0 and year / 100 != 0 or year / 400 == 0:
        isleap = '윤년입니다'

    print("%d는 %s" % (year, isleap))


isLeapYear()


# 20다음 조건을 만족하는 복권 발행 프로그램을 작성하세요
# a 사용자로부터 복권 숫자 3자리를 입력받으세요
# b 프로그램상에서 난수 생성을 이용해서 복권 3자리 수를 생성
# c 사용자가 입력한 복권 숫자가 모두 일치 :상금 백만원
# c 사용자가 입력한 복권 숫자가 2개 일치 :상금 1만원
# c 사용자가 입력한 복권 숫자가 3개 일치 :상금 1천원
def rouletteLotto():
    import random
    lotto = str(random.randint(100, 999))
    lucky = input('복권번호를 입력하세요')
    match = 0  # 일치여부
    prize = '꽝 다음 기회에!'

    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            if (lucky[i] == lotto[j] or
                    lucky[i] == lotto[j] or
                    lucky[i] == lotto[j]):
                match += 1

    if match == 3:
        prize = '1등 당첨! 상금 백만원!'
    elif match == 2:
        prize = '2등 당첨! 상금 만원!'
    elif match == 1:
        prize = '3등 당첨! 상금 천원!'

    print(lucky, lotto, prize)


rouletteLotto()