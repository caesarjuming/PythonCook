__author__ = 'Administrator'

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            # 生成的是匹配的那行，和前五个执行匹配动作的line
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open("../File/somefile.txt") as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline+'所匹配的行', end='\n')
            print(line+'成功匹配的行', end='\n')


# 多于3的部分会删掉
q = deque(maxlen=3)
for i in range(10):
    q.append(i)
print(q)