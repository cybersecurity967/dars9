import matplotlib.pyplot as plt

mashgulot = [1, 2, 3, 4, 5, 6]
masofa = [2.0, 2.5, 2.3, 3.0, 3.5, 4.0]

plt.plot(mashgulot, masofa, color="purple", marker="o", linewidth=2.5)
plt.title("Sportchining yugurgan masofalari")
plt.xlabel("Mashg'ulot raqami")
plt.ylabel("Masofa (km)")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()