# 실습문제 6.1.2 
# 현지는 자사상품이벤트를 위해 고객들로부터 이메일을 입력받았다. 고객들이 이메일 형식을
# 올바르게 입력했는지 검사하는 정규표현식을 작성해보자.

# 1. 이메일은 ID 파트와 host 파트가 있다. (ID @ host)
# 2. ID 파트는 영문 대소문자, 숫자, 특수문자(-_)가 들어갈 수 있다.
# 3. host 파트는 영문 대소문자, 숫자, 특수문자(-)
# 4. host 파트는 2개 이상의 도메인으로 구성 될 수 있다.

# ^[\w-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$

import re

regex = re.compile('^[\w-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

datas = [
    'startcoding@maver.com',
    'start-coding@maver.com',
    'start_coding@maver.co.kr',
    'startcoding@k-mail.com',
    '@maver.com',
    'startcoding?@k-mail.com',
    'startcoding@k-mail',
    'startcoding@maver'
]

for data in datas:
    matchObj = regex.match(data)
    result = (lambda x : True if x != None else False)(matchObj)
    print(f'{data} {result}')