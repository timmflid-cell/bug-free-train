#задание 1
list1 = [1,-2, 3, 4, 5, -6, 7, -9, -10, 11, 12]

NLO = 0
Garantiya = 0
luky = 0

for i in list1:
    if i < 0:
        NLO += i

for b in list1:
    if b % 2 == 0 and b > 0:
            Garantiya += 1

for c in list1:
    if c % 2 != 0 and c > 0:
        luky += 1

def summ(list1) -> int:
    count = 1
    for index, item in enumerate(list1):
        if index % 3 == 0:
            count *= item
    return count


def numbers(list1) -> int:
    count = 1
    for index, item in enumerate(list1):
        list1.sort()
        if index == 0 or index == len(list1) -1:
            continue
        else:
            count *= item
    return count


def pushka(list1) -> int:
    count = 0
    for index, item in enumerate(list1):
        if index == 0 or index == len(list1) - 1:
            continue
        else:
            count += item
    return count

#задание 2
import random

dzlist = []

for e in range(-10, 10):
    dzlist.append(random.randint(1, 10))

newdzlist = []
list2 = []
list3 = []
list4 = []

for z in range(len(dzlist)):
    if dzlist[z] % 2 == 0:
        newdzlist.append(dzlist[z])

for p in range(len(dzlist)):
    if dzlist[p] % 2 != 0:
        list2.append(dzlist[p])

for u in range(len(dzlist)):
    if dzlist[u] < 0:
        list3.append(dzlist[u])

for u in range(len(dzlist)):
    if dzlist[u] > 0:
        list4.append(dzlist[u])

# задание 1
print(NLO)
print(Garantiya)
print(luky)
print(summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(numbers([1, 2, 3, 4]))
print(pushka([1, 2, 3, 4]))

# задание 2
print(dzlist)
print(newdzlist)
print(list2)
print(list3)
print(list4)