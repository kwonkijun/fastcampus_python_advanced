# 기존 함수
def minus_one(a):
    return a-1

# 람다 함수 - 이름이 필요없는 간단한 함수
lambda a : a-1

# 람다 함수 호출방법 1. 함수 자체를 호출
print((lambda a : a-1)(10))

# 람다 함수 호출방법 2. 변수에 담아서 호출
minus_one_2 = lambda a : a-1
print(minus_one_2(100))

# 람다 함수에서 if 문 사용

# 기존 함수
def is_positive_number(a):
    if a > 0:
        return True
    else:
        return False

# 람다 함수
lambda a : True if a > 0 else False

# 람다 함수 호출 (1)
print((lambda a : True if a > 0 else False)(-2))

# 람다 함수 호출 (2)
is_positive_number = lambda a : True if a > 0 else False
print(is_positive_number(2))