# 1. 이터러블 객체 (iterable object)
# 문자열, 리스트, 튜플, 딕녀서리, range 객체

# for i in "123":
#     print(i)

# for i in [10, 20, 30]:
#     print(i)

iter_obj = [10, 20, 30].__iter__()

print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())