from random import *
inimesed = ["A", "B", "C", "D"]
palgad = [3000, 2000, 1000, 2000]
def sisesta_andmed(i, p):
    N = 4
    for n in range(N):
        inimene = input("Введите имя: ")
        i.append(inimene)
        palk = randint(100,10000)
        p.append(palk)
    return i,p
def andmed_ekranile(i, p):
    N=len(i)
    for n in range(N):
        print(f"{i[n]} - {p[n]}")
def kustutamine(i, p):
    nimi=input("Введите имя человека, которого нужно удалить: ")
    n=i.count(nimi)
    abi_list=[]
    if n > 0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e))
                print(f"{t}.{i[e]} - {p[e]}")
        j=int(input("Порядковый номер человека: "))
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekranile(i,p)
    return i,p
def maksimum(i, p):
    max_palk = palgad[0]
    kellel = inimesed[0]
    for p in palgad:
        if p > max_palk:
            max_palk = p
            i = palgad.index(max_palk)
            kellel = inimesed[i]
    print(f"Максимальную зарплату - {max_palk} получает - {kellel}")
def minimum(i, p):
    min_palk = palgad[0]
    kellel = inimesed[0]
    for p in palgad:
        if p < min_palk:
            min_palk = p
            i = palgad.index(min_palk)
            kellel = inimesed[i]
    print(f"Минимальную зарплату - {min_palk} получает - {kellel}.")
def keskmine(i, p):
    summa = 0
    t = False
    for palk in p:
        summa+=palk
    summa/=len(p)
    print(f"Средняя зарплата: {summa}")
    for palk in p:
        if palk==summa:
            n=p.index(palk)
            print(f"Такую зарплату получает: {i[n]}")
            t=True
    if t == False: 
        print("Люди, получающие такую зарплату, отсутсвуют.")
def sorteerimine(i, p, v):
    N = len(p)
    if v == 1:
        for n in range (0, N):
            for m in range (n, N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    else:
        for n in range (0, N):
            for m in range (n, N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi

    andmed_ekranile(i ,p)
def vordsed_palgad(i, p):
    N = len(p)
    dublikatid = [ x for x in palgad if palgad.count(x)>1 ]
    dublikatid = (list(set(dublikatid)))
    print(dublikatid)
    for palk in dublikatid:
        n = p.count(palk)
        k=-1
        for j in range(n):
            k = p.index(palk, k+1)
            nimi = i[k]
            print(f"{palk} - получает {nimi}.")
def nimi(i,p):
    otsi_nimi = []
    otsi_palk = []
    palk_keda = 0
    kes = input("Введите имя: ")
    n = len(inimesed)
    for j in range(n):
        if inimesed[j] == kes:
            palk_kes = palgad[j]
            otsi_nimi.append(inimesed[j])
            otsi_palk.append(palk_kes)
        else:pass
    for i in range(len(otsi_nimi)):
            print(f"{otsi_nimi[i]} получает - {otsi_palk[i]}.")
def topkolm(i,p,v):
    N = len(p)
    if v == 1:
        for n in range (0, N):
            for m in range (n, N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
        k = 3
        for i in range(0,k,1):
            print(palgad[i], inimesed[i])
            print()
    else:
        for n in range (0, N):
            for m in range (n, N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
        k = 3
        for i in range(0,k,1):
            print(palgad[i], inimesed[i])
            print()
def erinev(i, p):
    number = int(input("Введите сумму: "))
    usl = int(input("Больше суммы - 1\nМеньше суммы - 2\n"))
    for i in palgad:
        if usl == 1:
            if i > number:
                x = palgad.index(i)
                nimi = inimesed[x]
                print(f"{nimi} - {i}")
        else:
            if i < number:
                x = palgad.index(i)
                nimi = inimesed[x]
                print(f"{nimi} - {i}")
def tulumaks(i, p):
    summa = int(input("Введите зарплату: "))
    if summa < 1200:
        tul = (summa-500)*0.2
        x = summa - tul
    elif summa > 1200 <= 2100:
        tul = 500-(500/850)*(summa-1200)
        x = summa - tul
    else:
        x = summa*0.2
    print(f"Нетто зарплата - {round(x,2)}")
def sort_nimi_jargi(p, i, v):
    N = len(p)
    if v == 1:
        for n in range (0, N):
            for m in range (n, N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    else:
        for n in range (0, N):
            for m in range (n, N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi

    andmed_ekranile(i ,p)
def kust_kesk(i, p):
    summa = 0
    for palk in palgad:
        summa+=palk
    summa/=len(palgad)
    n = len(palgad)
    for i in range(n):
        for palk in palgad:
            if palk < summa:
                g = int(palgad.index(palk))
                palgad.remove(palk)
                inimesed.pop(g)
    N=len(inimesed)
    for n in range(N):
        print(f"{inimesed[n]} - {palgad[n]}")


while 1:
    valik=input("a - Ввод данных\ne -Показать данные \nk - Удаление\ns - Сортировка\nv - Проверка одинаковых зарплат\nmax - Максимальная зарплата\nmin - Минимальня зарплата\nkesk - Средняя зарплата\nn - Поиск по имени\ntop - Топ 3 богатых/бедных\nerinev - Вывод списка тех людей, кто получает больше/меньше чем указанная сумма\ntul - Зарплата с учетом налогов\nsort - Сортировка по имени\nkust - Удаление из списка людей, который получают меньше средней\n")
    if valik.lower() == "a":
        inimesed,palgad=sisesta_andmed(inimesed,palgad)
    elif valik.lower() == "e":
        andmed_ekranile(inimesed,palgad)
    elif valik.lower() == "k":
        inimesed,palgad=kustutamine(inimesed,palgad)
    elif valik.lower() == "s":
        sorteerimine(inimesed, palgad, int(input("1 - Сортировка по убыванию.\n2 - Сортировка по возростанию.\n")))
    elif valik.lower() == "v":
        vordsed_palgad(inimesed, palgad)
    elif valik.lower() == "max":
        maksimum(inimesed, palgad)
    elif valik.lower() == "min":
        minimum(inimesed, palgad)
    elif valik.lower() == "n":
        nimi(inimesed, palgad)
    elif valik.lower() == "kesk":
        keskmine(inimesed, palgad)
    elif valik.lower() == "top":
        topkolm(inimesed, palgad, int(input("1 - Топ богатых.\n2 - Топ бедных.\n")))
    elif valik.lower() == "erinev":
        erinev(inimesed, palgad)
    elif valik.lower() == "tul":
        tulumaks(inimesed,palgad)
    elif valik.lower() == "sort":
        sort_nimi_jargi(inimesed, palgad, int(input("1 - Сортировка от Я до А.\n2 - Сортировка от А до Я.\n")))
    elif valik.lower() == "kust":
        kust_kesk(inimesed, palgad)
    else:
        break