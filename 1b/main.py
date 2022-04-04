'''
Склады
Компания-застройщик занимается строительством недвижимости промышленного назначения, а именно – складских помещений.
Каждый квадратный метр площади стоит L рублей. Компания имеет достаточный запас оборотных средств,
чтобы продавать построенные помещения не сразу после завершения строительства, а в тот момент, когда ей это выгодно.
Рынок недвижимости очень динамичный, поэтому цена квадратного метра меняется каждый день.
Аналитики застройщика смогли точно спрогнозировать цену на ближайшие N дней (пронумеруем дни в хронологическом порядке от 0 до N-1).
Теперь требуется определить, в какие из этих дней нужно продавать, чтобы по истечению N дней заработать как можно больше денег.
Известно, что стройка новых площадей происходит с равномерной скоростью S кв. метров в сутки.
А к 0-му дню объем построенной площади составлял S кв. метров, при том что S = 1
Формат выходных данных
Вывести одно число - максимальное кол-во денег, которое может заработать компания-застройщик.
Примеры
Входные данные:
7
81 22 31 44 41 78 98
Выходные данные:
686
Входные данные:
5
81 14 88 2 22
Выходные данные:
308
'''

def main():
    n = int(input())
    l = input().split()
    results = [int(i) for i in l]
    maximum = 0
    ind = 0
    ms =0

    m = n
    if m %2 != 0:
        while (n > 0):
            ind = results.index(max(results)) + 1 - ind
            maximum += int(ind) * int(max(results))
            for i in range (int(ind)):
                results[i] = 0
            n = n - ind
        print(maximum)
    if m %2 == 0:
        while (n > 0):
            os = ms - ind
            ind = results.index(max(results)) + 1
            if (os == 0):
                maximum += int(ind) * int(max(results))
            maximum += os * int(max(results))
            for i in range (int(ind)):
                results[i] = 0
            n = n - ind
            ms = m
        print(maximum)

if __name__ == '__main__':
    main()

