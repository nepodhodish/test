import random

print(
    'Добро пожаловать в игру "Кости". Цель игры: игрок и компьютер по очереди \nкидают две игральные кости. У кого сумма цифр за 3 броска будит больше тот и выйграл.')
brosok = 0
summa_player = 0
summa_computer = 0
input('Нажмите Enter для продолжения')
while (brosok < 3):
    brosok = brosok + 1
    
    k1 = random.randint(1, 6)
    k2 = random.randint(1, 6)
    print('У вас выпали числа:', k1, 'и', k2)
    summa_player = summa_player + k1 + k2
    print('В сумме у вас:', summa_player)
    input('Нажмите Enter для продолжения')
    print('Ходит компьютер')
    k1 = random.randint(1, 6)
    k2 = random.randint(1, 6)
    print('У компьютера выпали числа:', k1, 'и', k2)
    summa_computer = summa_computer + k1 + k2
    print('В сумме у компьютера:', summa_computer)
    input('Нажмите Enter для продолжения')

if (summa_player > summa_computer):
    print('Ура ты выйграл!')
elif (summa_player < summa_computer):
    print('Ха ХА! Ты проиграл!')
elif (summa_player == summa_computer):
    print('ммм Ничья!')
