import matplotlib.pyplot as plt

mahsulotlar = ["Non", "Sut", "Tuxum", "Yog", "Shakar"]
sotuv = [45, 30, 60, 20, 25]

max_sotuv = max(sotuv)
min_sotuv = min(sotuv)
max_mahsulot = mahsulotlar[sotuv.index(max_sotuv)]
min_mahsulot = mahsulotlar[sotuv.index(min_sotuv)]

print(f"Eng ko'p sotilgan mahsulot: {max_mahsulot} ({max_sotuv} ta)")
print(f"Eng kam sotilgan mahsulot: {min_mahsulot} ({min_sotuv} ta)")

plt.bar(mahsulotlar, sotuv, color=["coral", "skyblue", "lightgreen", "gold", "orchid"])
plt.title("Bir haftadagi mahsulotlar savdosi")
plt.xlabel("Mahsulotlar")
plt.ylabel("Sotilgan soni")
plt.show()