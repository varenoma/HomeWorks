harfdagi_gurgut_donachalari_soni = {"0":6, "1":2, "2":5, "3":5, "4":4, "5":5, "6":6, "7":3, "8":7, "9":6}

son = list(input())

res = 0
for y in son:
    print(y)
    res += harfdagi_gurgut_donachalari_soni[y]

print(res)