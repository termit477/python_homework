# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота

from os import system
system("cls")

from task_5_func import *


game = input('с кем будете играть? \n "1" - с ботом, "2" - с другим игроком: ')

if game == '1': 
    candy = Input_candy()
    player = Input_name_first_player()
    Play_with_computer(candy, player)

elif game == '2':
    candy = Input_candy()
    first_player = Input_name_first_player()
    second_player = Input_name_second_players()
    Play_with_other_player(candy, first_player, second_player)