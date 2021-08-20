# 이터레이터 생성방법

class Seasons:
    def __init__(self):
        self.season_list = ['spring', 'summer', 'autumn', 'winter']
        self.idx = 0
        self.max_num = 4

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.max_num:
            curr_idx = self.idx
            self.idx += 1
            return self.season_list[curr_idx]
        else:
            raise StopIteration

# for i in Seasons():
#     print(i)

iter_obj = Seasons().__iter__()

print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())