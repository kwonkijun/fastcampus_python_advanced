# 데코레이터
# 함수의 앞, 뒤로 부가적인 기능을 넣어주고 싶을 때 사용
# 로깅, 권한확인

# 데코레이터 생성하기
def logger(func):
    def wrapper(arg):
        print("함수 시작")
        func(arg) # 함수 실행
        print("함수 끝")
    return wrapper

@logger
def print_hello(name):
    print("hello", name)

@logger
def print_bye(name):
    print("bye", name)

print_hello('startcoding')
print_bye('fastcampus')
