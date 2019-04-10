# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

student = namedtuple('student', 'marks classe name idt')

numAlunos = int(input())

order = input().split()

dic = {}
dic['idt'] = order.index('ID')
dic['marks'] = order.index('MARKS')
dic['classe'] = order.index('CLASS')
dic['name'] = order.index('NAME')

alunos = []

for i in range(numAlunos):
    std = input().split()
    a = student(idt = std[dic['idt']], marks = std[dic['marks']], classe = std[dic['classe']], name = std[dic['name']])
    alunos.append(a)

total = 0
for i in alunos:
    total += int(i.marks)

print("{0:.2f}".format(total/numAlunos))

