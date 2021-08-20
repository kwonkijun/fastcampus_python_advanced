# 1. 위치 가변 매개변수
def print_fruits(*args):
    for arg in args:
        print(arg)

print_fruits('apple', 'orange', 'mango', 'grape')

# 2. 키워드 가변 매개변수
def comment_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

comment_info(name='파린이', content='정말 감사합니다!')

# 매개변수 작성 순서
# 위치 - 기본 - 위치 가변 - 키워드(기본) - 키워드 가변

def post_info(*tags, title, content, **kwargs):
    print(f'제목 : {title}')
    print(f'내용 : {content}')
    print(f'태그 : {tags}')

post_info('#파이썬', '#함수',title='파이썬 함수 정리!', content='다양한 매개변수 정리합니다.')