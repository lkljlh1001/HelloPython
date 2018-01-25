##          ***클래스를 이용한 성적프로그램처리***
#성적처리프로그램 V4
#이름name , 국어 kor, 영어eng , 수학 mat
# tot , avg , grd
#리스트 자료구조를 이용

class SungJuk:

    def __init__(self,name,kor,eng,mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def getTotal(self):
        tot = self.kor + self.eng + self.mat
        return tot

    def getAverage(self):
        avg = self.getTotal()/3
        return avg


    def getGrade(self):
        grdlist = '가가가가가가미양우수수'
        var = int(self.getAverage()/10)
        grd = grdlist[var]
        return grd



sj = SungJuk('혜교',99,98,99)
print(sj.getTotal())
print('%.2f' %(sj.getAverage()))
print(sj.getGrade())

class SungJukVO:

    def __init__(self,name,kor,eng,mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

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


sjsrv = SungJukService()
sj1 = SungJukVO('지현',99,98,99)
print(sj1.name)
print(sj1.kor)
print(sj1.eng)
print(sj1.mat)
print(sjsrv.getTotal(sj))
print(sjsrv.getAverage(sj))
print(sjsrv.getGrade(sj))