# 2. 제너레이터 표현식
double_generator = (i * 2 for i in range(1,10))

for i in double_generator:
    print(i)

# 3. 메모리 사용을 효율적으로 하기 위해서 사용
# ex) 숫자 1 - 10000 3배로 만든 결과 리스트 vs 제너레이터

# 리스트 : 데이터 저장에 필요한 메모리를 모두 사용
# 제너레이터 : 나중에 필요할 때 값을 만들어 사용 (메모리 매우 적게필요)
import sys

list_data = [i * 3 for i in range(1, 10000 + 1)]
generator_data = (i * 3 for i in range(1, 10000 + 1))

print(sys.getsizeof(list_data))
print(sys.getsizeof(generator_data))