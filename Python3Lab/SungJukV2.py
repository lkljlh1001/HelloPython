# 총점 getTotal
# 평균 getAverage
# 함수 getGrade
# 함수를 이용한 성적 처리 프로그램

def getTotal():
    tot = kor+eng+mat
    return tot # return 출력은 밖에서
    #pass                #pass  : dumy code

def getAverage():
    avg = getTotal()/3
    return avg
    #pass

def getGrade():
    avg = getAverage()
    grd = '가'
    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'
    return grd
    #pass

print('-- 성적 처리프로그램 v2 --')

name = input('이름을 입력하세요')
kor = int(input ('국어점수를 입력하세요'))
mat = int(input ('수학점수를 입력하세요'))
eng = int(input ('영어점수를 입력하세요'))


fmt = '이름:%s 국어:%d 영어:%d 수학:%d 총점:%d 평균:%.2f 학점:%s'  #출력할 형식을 미리 작성
print (fmt % (name, kor, eng , mat ,getTotal(),getAverage(),getGrade()))
