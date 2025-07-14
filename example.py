def yolo(x, y):
    x.dupa = y


class A:
    def magic(self, value):
        self.value = value


a = A()
setattr(A, 'magic', yolo)
a.magic(42)
print(a.dupa)
