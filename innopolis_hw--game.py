from random import randint

KNIGHT_HEALTH = 10

KNIGHT_STRENGTH = 10

MONSTER_POWER = 0

MONSTER_HEALTH = 0

SWORD_POWER = 0

POSSIBLE_VALUES = ['monster', 'apple', 'sword']

SLAIN_MONSTERS = 0

CONTINUE = True

print('Start game')

while CONTINUE:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    action = ''
    random_value = randint(0,2)
    print('кол-во побежденный монстров:', SLAIN_MONSTERS, '*' * SLAIN_MONSTERS)
    print('кол-во жизней:', KNIGHT_HEALTH , '@' * KNIGHT_HEALTH)
    print('сила удара:', KNIGHT_STRENGTH , '^' * KNIGHT_STRENGTH)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('')
    if SLAIN_MONSTERS == 10:
        print(SLAIN_MONSTERS)
        print('Победа')
        CONTINUE = False
        break
    else:    
        if POSSIBLE_VALUES[random_value] == 'monster':
            MONSTER_HEALTH = randint(5,20)
            MONSTER_POWER = randint(5,20)
            print('Вы встретили чудовище с', MONSTER_HEALTH, 'жизнями и с силой удара', MONSTER_POWER)
            action = input()
            while action != '1' and action != '2':
                print('введите корректное значение')
                action = input()
            if action == '1':
                print('вы повстречали монстра')
                if KNIGHT_HEALTH <= MONSTER_POWER:
                    print('Игра окончена')
                    break
                elif MONSTER_HEALTH > KNIGHT_STRENGTH:
                    print('не убить с одного удара')
                    while MONSTER_HEALTH != 0 or MONSTER_HEALTH < 0:
                        if KNIGHT_HEALTH <= 0:
                            print('Игра окончена')
                            CONTINUE = False
                            break
                        else:
                            print('Удар')
                            MONSTER_HEALTH -= KNIGHT_STRENGTH
                            KNIGHT_HEALTH -= MONSTER_POWER
                    SLAIN_MONSTERS += 1        
                else:
                    KNIGHT_HEALTH -= MONSTER_POWER
                    SLAIN_MONSTERS += 1
            elif action == '2':
                print('вы убежали')
        elif POSSIBLE_VALUES[random_value] == 'apple':
            KNIGHT_HEALTH += randint(5,10)
            print('+1 жизнь')
            print('Здоровье ', KNIGHT_HEALTH)
        else:
            print('вы нашли меч')
            SWORD_POWER = randint(1,20)
            print('сила меча ', SWORD_POWER)
            action = input()
            while action != '1' and action != '2':
                print('введите корректное значение')
                action = input()
            if action == '1':
                KNIGHT_STRENGTH = SWORD_POWER
            elif action == '2':
                print('идем дальше')
                    
