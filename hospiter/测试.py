__author__ = 'Administrator'
def a():
    for i in range(10):
        yield i
for i in a():
    print(i)