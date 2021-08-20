class Math:

    # 정적 메서드(static method)
    # 인스턴스를 만들 필요가 없는 메서드
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

print(Math.add(3, 4))
print(Math.sub(3, 4))