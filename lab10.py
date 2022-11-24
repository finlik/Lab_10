while True:
    try:
        N = int(input('Введите сумму: '))
    except ValueError:
        print('Вы ввели некорректное значение. Повторите попытку')
        continue
    k = 64
    while N > 0:
        if N >= k:
            print(k, 'x', N // k)
        N = N % k
        k = k // 2
    break
            
    
    
