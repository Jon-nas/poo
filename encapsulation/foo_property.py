class foo:
    def __init__(self, x = None):
        self._x = x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0

Foo = foo(10)
print(Foo.x)
del Foo.x
print(Foo.x)
Foo.x = 10
print(Foo.x)
