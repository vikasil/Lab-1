#test comment
import time
import os
clear = lambda: os.system('cls')

RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

#task 1
print("task 1")
i = 15
print(f'{RED}{"  " * i}{END}')
print(f'{WHITE}{"  " * i}{END}')
for r in range(3):
    print(f'{BLUE}{"  " * i}{END}')
print(f'{WHITE}{"  " * i}{END}')
print(f'{RED}{"  " * i}{END}')

#task2
print("task 2")
matrica = [[" " for i in range(70)] for i in range(3)]
for i in range(3, 70,7):
    matrica[0][i] ="*"
    matrica[1][i+1] ="*"
    matrica[1][i-1] ="*"
    matrica[2][i+2] ="*"
    matrica[2][i-2] ="*"
    matrica[2][i+3] ="*"
    matrica[2][i-3] ="*"
for i in range(3):
    for j in range(70):
        print(matrica[i][j], end="")
    print()



#task 3
print("task 3")
plot_list = [[0 for i in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        if j == 0 and i<=4:
            plot_list[i][j] = "!"
        if (j == 1 and i == 5) or (j == 2 and i == 6) or (j == 3 and i == 7) or (j == 4 and i == 8):
            plot_list[i][j] = "!"
        if j >=5 and i==9:
            plot_list[i][j] = "!"    

for i in range(10):
    for j in range(10):
        print(plot_list[i][j], end="")
    print()

#task 4

print("task 4")
with open('sequence.txt', 'r') as g:
    file = g.readlines()
colmen5 = []
col =0
colbol5 = []
for number in file:
    if float(number) > 5:
        colbol5.append(i)
    if 0<= float(number) < 5:
        colmen5.append(i)
bol = (len(colbol5)/len(file)*100)
men = (len(colmen5)/len(file)*100)
print(">5")
print(f'{RED}{"  " * int(bol)}{WHITE}{"  " * int(100 -bol)}{END}')
print(" >0 and <5")
print(f'{RED}{"  " * int(men)}{WHITE}{"  " * int(100 -bol)}{END}')

print(" для запуска анимации введите любой симвл в консоль")
f=input()
while True:
    print("это")
    time.sleep(1)
    clear()
    print("анимация")
    time.sleep(1)
    clear()
    print("честно")
    time.sleep(1)
    clear()

    
