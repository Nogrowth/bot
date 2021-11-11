# version 1.3.2
print("collector 프로그램이 시작 되었습니다!")

from library.collector_api import *

class Collector:
    print("collector 클래스에 들어왔습니다.")
    # Collector class에는 아래와 같은 생성자와 method가 있다. 즉 c가 self이다.
    def __init__(self):
        print("__init__ 함수에 들어왔습니다.")
        self.collector_api = collector_api() # 생성자 내에 c.collector_api라는 인스턴스 변수를 정의하고, 이 변수는 collector_api라는 collector_api내에 정의된 다른 클래스가 된다.
        # 즉 collector_api라는 module 내의 collector_api라는 class 내의 method들을 사용할 수 있게 된다. -> 종목 리스트, 종목별 일, 분봉 데이터 등을 불러올 수 있게 된다.

    def collecting(self):
        self.collector_api.code_update_check()

if __name__ == "__main__":
    print("__main__에 들어왔습니다.")
    # 아래는 키움증권 openapi를 사용하기 위해 사용하는 한 줄! 이해 할 필요 X
    app = QApplication(sys.argv)
    c = Collector() # c라는 Collector class의 instace를 생성
    # 데이터 수집 시작 -> 주식 종목, 종목별 금융 데이터 모두 데이터베이스에 저장.
    c.collecting()
