

__author__ = 'Administrator'

# 分解单独变量

data = ['caesar', 20, 2000.1, (1988, 8, 3)]
name, age, money, birthday = data
print(name, birthday)

# 如果元素数量不对会报错
# 丢弃某些不要的值

_, _, money, _ = data
print(money)

# 任意长度的可迭代对象中分解元素

def drop_first_last(grades):
    first, *middle, last = grades
    return middle

record = ('caesar', 11, 22, 33)
print(drop_first_last(record))

# *式语法在变长元组序列
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(x):
    print('bar', x)

for tag, *args in records:
    if tag=='foo':
        # *args是解参数，*号是把参数列表解析为数个值
        do_foo(*args)
    elif tag=='bar':
        do_bar(*args)
line = 'caesar;sh;28'
name, *other = line.split(';')
print(name)

# 嵌套分割
record = ('abc', 10, 20, (1, 2, 3))

# *_表示多个未命名的变量
name, *_, (*_, money) = record
print(name, money)



