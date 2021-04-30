a = 35
b = 25
c = 75
if a < b and a < c:
    print("Самое маленькое число а!")
    if b > c:
        print("Самое большое число b!")
    else:
        print("Самое большое число c!")
elif b < a and b < c:
    print("Самое маленькое число b!")
    if a > c:
        print("Самое большое число a!")
    else:
        print("Самое большое число c!")
elif c < a and c < b:
    print("Самое маленькое число c!")
    if b > a:
        print("Самое большое число b!")
    else:
        print("Самое большое число a!")