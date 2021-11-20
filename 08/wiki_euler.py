# n - количество итераций, h - шаг, (x, y) - начальная точка
def Euler(n = 10, h = 0.01, x = 1, y = 1):
    for i in range(n):
        y += h * function(x, y)
        x += h
    return x, y # решение


def function(x, y):
    return 6 * x**2 + 5 * x * y # функция первой производной


print(Euler())

class Poem(object):
    def __init__(self, content):
        self.content = "init"

    def indent(self, spaces=4):
        self.content = "indent"
        return self

    def suffix(self, content):
        self.content = "suffix"
        return self

    def __str__(self):
        return self.content

object = Poem('Road Not Taken')
print(object.indent(4).suffix('Rober Frost').content)
