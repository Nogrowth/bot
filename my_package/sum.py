print("sum.py 파일 안 입니다.")

def sum_ab(x, y):
    return x + y

def print_name():
    print(f"sum.py 모듈의 __name__ : {__name__}")

class calculator:
    def __init__(self, cx, cy):
        self.x = cx
        self.y = cy

    def sum(self):
        return self.x + self.y

if __name__ == '__main__':
    print('sum.py 파일의 if__name__ == ''_main__'': 구문 안 입니다! ')
