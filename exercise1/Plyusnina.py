#я слишком поздно увидела что нужны функции
#но с помощью них я бы и не смогла сделать :(
while True:

    for i in reversed(range(13,17)):
        print(('   ')*i,end='')
        print('/ / / / /')
    for i in reversed(range(13,20)):
        print(('  ')*i,end='')
        print('/ / / /')
    for i in reversed(range(10,13)):
        print(('  ')*i,end='')
        print('/ / /')
    for i in reversed(range(16,20)):
        print((' ')*i,end='')
        print('/ / /')
    for i in reversed(range(9,16)):
        print((' ')*i,end='')
        print(' / /')
    for i in reversed(range(2,9)):
        print((' ')*i,end='')
        print('  /')
    for i in reversed(range(1,7)):
        #print((' ')*i,end='')
        print('  |')
    
    a = (input('Продолжить? да/нет '))
    if a == 'нет':
         break
