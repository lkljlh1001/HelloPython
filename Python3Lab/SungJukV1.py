#성적프로그램 작성
name = input('이름을 입력하세요')
kor = int(input ('국어점수를 입력하세요'))
mat = int(input ('수학점수를 입력하세요'))
eng = int(input ('영어점수를 입력하세요'))

tot = kor + mat + eng
avg = tot / 3
grd = '가'

if avg >= 90:
    grd ='수'
elif avg >= 80:
    grd ='우'
elif avg >= 70:
    grd ='미'
elif avg >= 60:
    grd ='양'
print (name,kor,mat,eng,tot,avg,grd)
print ('{0}{1}{2}{3}{4}{5:.2f}{6}'
           .format(name,kor,mat,eng,tot,avg,grd))
print ('%s %d %d %d %d %.2f %s' \
            %(name,kor,mat,eng,tot,avg,grd))

