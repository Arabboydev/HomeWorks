gnomlar = [1, 2, 3, 4, 5, 6, 7]

S = int(input("Sovg'a narxini kiriting: "))

gnomlar_sum = sum(gnomlar)

Natija = S - gnomlar_sum

print(f"Gnomlarning puli : {gnomlar_sum}")

if S + gnomlar_sum <= 1000:
    print(f"Qancha qo'shib yuborish kerakligi: {Natija}")
