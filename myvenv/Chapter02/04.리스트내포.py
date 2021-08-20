# 리스트 내포
# for 사용
nums = [i for i in range(5)]
print(nums)

nums2 = [100, 200, 300]
double_nums = [i * 2 for i in nums2]
print(double_nums)

# if 사용
nums3 = [i for i in range(10) if i % 2 == 0]
print(nums3)

nums4 = [100, 200, 300, 400, 500]
double_nums2 = [i * 2 for i in nums4 if i >= 300]
print(double_nums2)