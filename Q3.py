class a():
    global z

    def __init__(self, y):
        self.y = y

    def __call__(self, z):
        if z > self.y:
            return z - self.y
        else:
            return self.y - z


class b(a):
    def __call__(self, z=4):  # (self,z):
        if z > self.y:
            return z - self.y
        else:
            return self.y - z


print(a(5)(b(6)()))

print(a(6)(b(5)(6)))
