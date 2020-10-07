# -*- coding:utf-8 -*-
import random
words_list=['испания','береза','существо','планшет','фосфор','дренаж','западня','человек','пномпень','кочерга','юность',
            'инфузория','топчан','цианид','вагонетка','бройлер','самосвал','дракон','станок','гвалт','йорк','мыльница',
            'желание','эвкалипт','ненастье']
errors=90

def print_hang(elements):
    """ печатает виселецу по количеству элементов
        равное количеству ошибок угадывания
    """
    for i in range(5):
        print()
    if (elements==0):
        print('\n\n\n\n\n\n')
    elif (elements==1):
        print('#\n#\n#\n#\n#\n#\n')
    elif (elements==2):
        print('#     #\n#     #\n#     #\n#     #\n#     #\n#     #\n')
    elif (elements==3):
        print('#######\n#     #\n#     #\n#     #\n#     #\n#     #\n')
    elif (elements==4):
        print('#######\n#  |  #\n#     #\n#     #\n#     #\n#     #\n')
    elif (elements==5):
        print('#######\n#  |  #\n#  o  #\n#     #\n#     #\n#     #\n')
    elif (elements==6):
        print('#######\n#  |  #\n#  o  #\n#  |  #\n#     #\n#     #\n')
    elif (elements==7):
        print('#######\n#  |  #\n#  o  #\n# /|  #\n#     #\n#     #\n')
    elif (elements==8):
        print('#######\n#  |  #\n#  o  #\n# /|\\ #\n#     #\n#     #\n')
    elif (elements==9):
        print('#######\n#  |  #\n#  o  #\n# /|\\ #\n# /   #\n#     #\n')
    elif (elements==10):
        print('#######\n#  |  #\n#  o  #\n# /|\\ #\n# / \\ #\n#     #\n')
    else:
        print('error')

def print_masked(source,mask):
    """
    печатает подряд все элементы массива источника.
    если значение соответствующего элемента массива маски равно 1, то само значение,
    в противном случае вмесот элемента печатет []
    :param source: список источник
    :param mask: список маска - равный по длинне источнику
    """
    for w in range(len(source)):
        if (mask[w]==1):
            print(source[w],end='')
        else:
            print('[]',end='')
    print()

def make_mask(source,mask):
    """
    заполняет список маску нулями
    :param source: список эталон длинны
    :param mask: список, который заполняем нулями
    """
    for l in range(len(source)):
        mask[l]=0

def chek_attempt(liter,source,mask,arch):
    """
    проверяет букву на наличие в списке источнике
    добавляет в список учета попыток
    если есть - отмечает 1 по индексу в маске
    :param liter:  угадываемая буква
    :param source: список с загаданным словом
    :param mask: список с маской
    :param arch: список с символами , которые пробовали
    :return: если символ совпал возвращаем 1, если нет - 0
    """
    fnd=0
    for l in range(len(source)):
        if liter==source[l]:
            mask[l]=1
            fnd+=1
    if (fnd>0):
        arch.append(liter)
        return 0
    else:
        arch.append(liter)
        return 1
def do_you_have_a_mask(mask):
    """
    проверяем, не закончилась ли маска
    :param mask: список маска
    :return: если в маске еще есть 0 возвращаем 1, если нет - 0
    """
    fnd=0
    for l in range(len(mask)):
        if (mask[l]==0):
            fnd+=1
    if (fnd>0):
        return 1
    else:
        return 0


errors=0
game_over=0
arch_try=[]
target_word=list(random.choice(words_list))
cur_mask=list(target_word)
not_finded=len(target_word)
make_mask(target_word,cur_mask)
while game_over==0:
    print_hang(errors)
    print_masked(target_word,cur_mask)
    if (len(arch_try)>0):
        print('уже были буквы:',arch_try)
    print('Попробуйте угадать букву:')
    att=input('>')
    arch_try.sort()
    if (arch_try.count(att)>0):
        print('Такая буква уже загадывалась')
    elif att=='':
        print('вы ничего не ввели')
    else:
        errors=errors+chek_attempt(att,target_word,cur_mask,arch_try)
        if (errors>=10):
            game_over=1
        if (do_you_have_a_mask(cur_mask)==0):
             game_over=2
if (game_over==1):
    print_hang(10)
    print('Вы проиграли, вас повесили')
elif (game_over==2):
    print('ПОЗДРАВЛЯЕМ, ВЫ ВЫИГРАЛИ')
    print('Загаданное слово:   ',target_word)


