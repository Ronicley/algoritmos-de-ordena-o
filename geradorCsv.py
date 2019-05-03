from random import randint, shuffle, choice
arq = open('10milNum.csv', 'w')

result = [randint(0, i) for i in range(10000)]
shuffle(result)
for i in range(len(result)):
    arq.write(str(choice(result))+';\n')

arq.close()