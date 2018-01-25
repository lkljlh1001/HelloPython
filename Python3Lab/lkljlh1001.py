# 모듈을 이용한 예제문제

#17
def isLeapYear():
    year = int(input('윤년여부를 알고 싶은 년도를 입력하세요'))
    isleap = '윤년아닙니다'
    if year / 4 == 0 and year / 100 != 0 or year / 400 == 0:
        isleap = '윤년입니다'

    print("%d는 %s" % (year, isleap))

#윤년여부
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


#복권 발행
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





#성적데이터클래스
class SungJukVO:

    def __init__(self,name,kor,eng,mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat


#성적처리용클래스
class SungJukService:

    def getTotal(self,sj):
        tot = sj.kor + sj.eng + sj.mat
        return tot

    def getAverage(self,sj):
        avg = sj.getTotal()/3
        return avg


    def getGrade(self,sj):
        grdlist = '가가가가가가미양우수수'
        var = int(sj.getAverage()/10)
        grd = grdlist[var]
        return grd