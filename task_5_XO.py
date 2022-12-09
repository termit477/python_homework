# Создайте программу для игры в ""Крестики-нолики"".(в консоли происходит выбор позиции)

from os import system
system("cls")

from task_5_func import Input_name_first_player
from task_5_func import Input_name_second_players
from task_5_func import A_lot_of_player

first_player = Input_name_first_player()
second_player = Input_name_second_players()

# Ввод данных - местопложение в двумерном массиве. Пример: "01", или "20"
A_lot_of_player(first_player, second_player)
