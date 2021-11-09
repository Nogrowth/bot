# 패키지 만들기 실습(package_test.py 파일 및 my_package 패키지 생성 후 실습)
# from 패키지 import 모듈 (ex. from my_package import sum)



# from 패키지.모듈 import 함수, 클래스!!!! (ex. from my_package.sum import sum_ab)

from my_package.sum import sum_ab, calculator, print_name
from my_package.sub import sub_ab

# print(sum_ab(1, 2))
# print(sub_ab(3, 0))
#
# c = calculator(1, 2)
# print(f"c.sum() = {c.sum()}")

# __name__ ? => 현재 모듈의 이름을 담고 있는 내장 변수
# 현재 모듈의 이름은? package_test인데.. 왜?
# 우리가 package_test를 실행 중이기 때문에 --> __main__이 담겨져 있다.
# 즉, 이 파일을 실행했을 경우 실행할 구문!!!
# file 내의 경우 import하는 순간 다 실행하기 때문에..


if __name__ == '__main__':
    print(sum_ab(1, 2))
    print(sub_ab(3, 0))

    c = calculator(1, 2)
    print(f"c.sum() = {c.sum()}")

    print(f"package_test.py의 __name__: {__name__}")
    print_name()
