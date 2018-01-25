#프로그램을 구성하는 독립적인 단위를
#각각 정의하고 관리하는 방법
#자주 사용하는 일반적인 기능은 모듈로 한번 만들어 두면
#필요할때 마다 도입해서 활용 할 수 있다.
#모듈 : 관련성 있는 데이터들, 함수,클래스
#모듈을 사용하려면 import 명령으로 인터프리터에게
#사용여부를 알려야 한다


#import random
# 인터프리에게 사용여부를 알림 (import)
#import random
#import random as r #별칭으로줄여쓰기
#from random import randint #모듈명 줄여쓰기
#from math import pi
#from math import sqrt
#from math import pi,sqrt #추천
#from math import * # 비추
#import Lab03 #우리가 작성한 함수가 있는 파일
#import math
#import lkljlh1001

#모듈을 호출할때는 모듈명(파일이름).함수명
#print (r.radint(1,10))
#print(randint(1,10))
#Lab03.isLeapYear()
#print(math.pi)
#print(pi)
#print(math.sqrt(9))
#print(sqrt(9))

#모듈 호출시 이름을 별칭을로 바꿔 정의
# import 모듈이름 as 별칭

#함수 호출시 모듈명까지 기술하는 것은 왠지 불편
#from 모듈명 import 함수명

#사용자가 만든 모듈을 다른 파일에서 참조하려면
# 두 파일이 모두 같은 위치에 있어야함
#즉, 프로젝드내에서 서로 참조하려면
#이 파일들은 같은 위치에 저장되어 있어야함

#한편, python IDE나 다른 프로젝트에서 모듈을
#참조하려면 pythonPath 가 정의한 위치에
#모듈을 저장해둔다
#파이썬설치위치 나 (파이썬 설치위치 /Lib)
#lkljlh1001.isLeapYear()

#파이썬 패키지
#다수의 개발자가 만든 모듈의 이름이 서로 같을 경우
# 파이썬에서는 패키지라는 개념을 이용해서 해결
# .연산자를 이용해서 모듈을 계층적(디렉토리)으로 관리
#파이썬에서 디렉토리가 패키지로 인식되려면
#__init__.py라는 파일이 반드시 있어야함
from lkljlh1002.hello import sayHello

sayHello()

