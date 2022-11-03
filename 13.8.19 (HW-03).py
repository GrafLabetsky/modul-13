bilets = int(input("Количество билетов, которые вы хотите приобрести на мероприятие \n"))
stoimost_summa = 0

for i in range(bilets):
    vozrast = int(input(f"Укажите возраст посетителя {i+1} "))
    if vozrast < 18:
        stoimost = 0
    elif 25 > vozrast >= 18:
        stoimost = 990
    else:
        stoimost = 1390
    print("Стоимость билета составит", stoimost)
    stoimost_summa += stoimost
    print('*'*32)

if bilets > 3:
    stoimost_summa -= (stoimost_summa * .1)

print("")
print("Стоимость всех билетов", stoimost_summa)