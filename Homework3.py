import matplotlib.pyplot as plt

kunlar = [1, 2, 3, 4, 5, 6, 7]
ali = [10, 15, 12, 20, 25, 22, 30]
vali = [8, 12, 18, 16, 22, 27, 28]

plt.plot(kunlar, ali, marker="o", color="blue", label="Ali")
plt.plot(kunlar, vali, marker="s", color="green", label="Vali")

plt.title("Ali va Valining haftalik natijalari")
plt.xlabel("Kunlar")
plt.ylabel("Natijalar")
plt.legend()
plt.grid(True)
plt.show()