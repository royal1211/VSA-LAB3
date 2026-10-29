from collections import deque
yasicoxolanlar = deque()
normaladamlar = deque()
def dayanacagagel(ad, yas):
    if yas > 65:
        yasicoxolanlar.append(ad)
        print(ad + " qabaq novbeye kecdi, cunki yasi " + str(yas) + " dir.")
    else:
        normaladamlar.append(ad)
        print(ad + " normal novbede dayanib.")
def avtobusamin():
    if len(yasicoxolanlar) > 0:
        adam = yasicoxolanlar.popleft()
        print(adam + " avtobusa birinci mindi (yasi coxdur deye).")
    elif len(normaladamlar) > 0:
        adam = normaladamlar.popleft()
        print(adam + " avtobusa mindi.")
    else:
        print("Dayanacaqda adam qalmayib.")
def haminigoster():
    print("Qocalarin novbesi: " + str(list(yasicoxolanlar)))
    print("Normal novbe: " + str(list(normaladamlar)))
print("AVTOBUS TESTI ")
dayanacagagel("Xanlar", 20)
dayanacagagel("Hesen dayi", 72)
dayanacagagel("Veli", 22)
haminigoster()
avtobusamin()
avtobusamin()
haminigoster()
