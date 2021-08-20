# 실습문제 2.4.2
# ['오메가3', None, '비타민C500', None, '홍삼절편']
# ['오메가3', '', '비타민C500', '', '홍삼절편']

items = ['오메가3', None, '비타민C500', None, '홍삼절편']

# 리스트 내포 사용 전
# result = []
# for item in items:
#     if item != None:
#         result.append(item)
#     else:
#         result.append('')
# print(result)

# 리스트 내포 사용 후
result = [i if i != None else '' for i in items]
print(result)
