
from random import randint as rnd

def Input_candy():
    return int(input('Введите количество конфет: '))

def Input_name_first_player():
    return input('Введите имя игрока: ')

def Input_name_second_players():
    return input('Введите имя игрока: ')


# Для игры с конфетами
def Play_with_other_player(can, name1, name2):
  while can > 0:
    while True:
        player_1_step = int(input(f'{name1} берет конфеты в количестве: '))
        if 0 < player_1_step < 29 and player_1_step <= can:
            can = can - player_1_step
            print(f'Осталось конфет: {can}')
            break
        else:
            print('Повторите ввод.')
    if can == 0: 
        print(f' Победил {name1} и забирает все конфеты')
        break

    while True:
        player_2_step = int(input(f'{name2} берет конфеты в количестве: '))
        if 0 < player_1_step < 29:
            can = can - player_2_step
            print(f'Осталось конфет: {can}')
            break
    if can == 0: 
        print(f' Победил {name2} и забирает все конфеты')
        break


def Play_with_computer(can, name):
    while can > 0:
        while True:
            player_step = int(input(f'{name} берет конфеты в количестве: '))
            if 0 < player_step < 29 and player_step <= can:
                can = can - player_step
                print(f'Осталось конфет: {can}')
                break
            else:
                print('Повторите ввод.')
        if can == 0: 
            print(f'Победил {name} и забирает все конфеты')
            break

        if can < 29:
            print(f'Тебя, {name}, обыграл жалкий компьютеришка и забрал все виртуальные конфеты')
            break
        else:
            computer_step = rnd(1, 29)
            print(f'Компьютер взял {computer_step}')
            can = can - computer_step
            print(f'Осталось конфет: {can}')


# Для игры в крестики-нолики
def A_lot_of_player(p1, p2):
    # Опеределение, игрока, кто ходит первый и начало самой игры
    lot = rnd(0,1)
    if lot == 0: 
        print(f'Начинает игрок {p1}')
        player_1_hod = 'X'
        player_2_hod = 'O'
        Game_XO(p1, p2, player_1_hod, player_2_hod)
    elif lot == 1: 
        print(f'Начинает игрок {p2}')
        player_1_hod = 'O'
        player_2_hod = 'X'
        Game_XO(p2, p1, player_2_hod, player_1_hod)


def Game_XO(p1, p2, p1_hod, p2_hod):
    mass = [['.','.','.'], ['.','.','.'], ['.','.','.']]
    count = 1
    while count < 10:
        if count % 2 == 1: 
            while True:
                hod = input(f'Ход игрока {p1}: ')
                if (len(hod) != 2 or 
                    int(hod[0]) > len(mass)-1 or 
                    int(hod[1]) > len(mass[0])-1):
                    print('Повторите ввод.')
                    Output_array(mass)
                else:
                    if mass[int(hod[0])][int(hod[1])] != '.':
                        print('Повторите ввод.')
                        Output_array(mass)
                    else:
                        mass[int(hod[0])][int(hod[1])] = p1_hod
                        Output_array(mass)
                        break

            if Result_game(mass) == 1:
                print(f'Победил игрок {p1}')
                break

        elif count % 2 == 0:
            while True:
                hod = input(f'Ход игрока {p1}: ')
                if (len(hod) != 2 or 
                    int(hod[0]) > len(mass)-1 or 
                    int(hod[1]) > len(mass[0])-1):
                    print('Повторите ввод.')
                    Output_array(mass)
                else:
                    if mass[int(hod[0])][int(hod[1])] != '.':
                        print('Повторите ввод.')
                        Output_array(mass)
                    else:
                        mass[int(hod[0])][int(hod[1])] = p2_hod
                        Output_array(mass)
                        break

            if Result_game(mass) == 1:
                print(f'Победил игрок {p2}')
                break
                
        count += 1
    
    if Result_game(mass) == 0: 
        print('Ничья')


def Output_array(array):
    for i in range(len(array)):
        for j in range(len(array)): 
            print(array[i][j], end = ' ')
        print()


def Result_game(arr):
    # Не удалось красиво прописать :)
    if (arr[0][0] == arr[0][1] == arr[0][2] == 'X' or
        arr[1][0] == arr[1][1] == arr[1][2] == 'X' or 
        arr[2][0] == arr[2][1] == arr[2][2] == 'X' or 
        arr[0][0] == arr[1][0] == arr[2][0] == 'X' or 
        arr[0][1] == arr[1][1] == arr[2][1] == 'X' or 
        arr[0][2] == arr[1][2] == arr[2][2] == 'X' or 
        arr[0][0] == arr[1][1] == arr[2][2] == 'X' or 
        arr[0][2] == arr[1][1] == arr[2][0] == 'X'):
        return 1
    elif (arr[0][0] == arr[0][1] == arr[0][2] == 'O' or
          arr[1][0] == arr[1][1] == arr[1][2] == 'O' or 
          arr[2][0] == arr[2][1] == arr[2][2] == 'O' or 
          arr[0][0] == arr[1][0] == arr[2][0] == 'O' or 
          arr[0][1] == arr[1][1] == arr[2][1] == 'O' or 
          arr[0][2] == arr[1][2] == arr[2][2] == 'O' or 
          arr[0][0] == arr[1][1] == arr[2][2] == 'O' or 
          arr[0][2] == arr[1][1] == arr[2][0] == 'O'):
        return 1
    else:
        return 0