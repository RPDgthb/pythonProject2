from random import randint

comp_ch = randint(1, 10)
player_ch = input('Виберіть число від 1 до 10: ')

if player_ch == comp_ch:
    print('ПЕРЕМОГА')
else:
    print('ПОРАЗКА')