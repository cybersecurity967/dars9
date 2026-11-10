import matplotlib.pyplot as plt

testlar = [1, 2, 3, 4, 5]
guruh_a = [65, 70, 75, 80, 85]
guruh_b = [60, 72, 70, 88, 90]

plt.plot(testlar, guruh_a, marker="o", color="red", label="Guruh A")
plt.plot(testlar, guruh_b, marker="^", color="blue", label="Guruh_b")

plt.title("Ikki guruhning test natijalari taqqoslashi")
plt.xlabel("Testlar")
plt.ylabel("Ballar")
plt.legend()
plt.grid(True)
plt.show()