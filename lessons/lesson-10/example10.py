# Полиморфизм


class SplitPath(str):
    def __init__(self, obj):
        self.obj = str(obj)

    def __truediv__(self, other):
        first = self.obj.endswith('/')
        start = self.obj

        if isinstance(other, str):
            second = other.startswith('/')
            finish = other
        elif isinstance(other, SplitPath):
            second = other.obj.startswith('/')
            finish = other.obj
        else:
            second = str(other).startswith('/')
            finish = str(other)

        if first and second:
            return SplitPath(start[:-1] + finish)
        if (first and not second) or (not first and second):
            return SplitPath(start + finish)
        if not first and not second:
            return SplitPath(start + '/' + finish)

p1 = SplitPath('/home/user')
p2 = SplitPath('project')
res = p1 / p2

print(res, 'type: ', type(res))
print(res / 'text' / '/user' / 42)

# /home/user/project type:  <class '__main__.SplitPath'>
# /home/user/project/text/user/42
