import matplotlib.pyplot as plt

kunlar = ["Dush", "Sesh", "Chor", "Pay", "Juma", "Shan", "Yak"]
faollik = [3, 5, 4, 6, 7, 8, 5]

plt.plot(kunlar, faollik, marker="o", color="teal", linewidth=2)
plt.title("Haftalik foydalanuvchi faolligi")
plt.xlabel("Hafta kunlari")
plt.ylabel("Soatlar")
plt.grid(True)

plt.savefig("natija.png")
plt.show()