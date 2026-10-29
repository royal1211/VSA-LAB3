from collections import deque
apteknovbesi = deque()
def dermana_yaz(ad, dermanadi):
    apteknovbesi.append({"ad": ad, "derman": dermanadi})
    print(ad + " novbeye girdi Derman " + dermanadi)
def derman_ver():
    if len(apteknovbesi) > 0:
        adam = apteknovbesi.popleft()
        print(adam["ad"] + " " + adam["derman"] + " aldi ve novbeden cixdi.")
    else:
        print("Novbede heckim yoxdur.")
def siyahiya_bax():
    print("Aptekdeki novbe:")
    for a in apteknovbesi:
        print(a["ad"] + " - " + a["derman"])
print("APTEK TESTI ")
dermana_yaz("Xanlar", "parasetamol")
dermana_yaz("Eli", "nimesil")
siyahiya_bax()
derman_ver()
siyahiya_bax()
print("\n")