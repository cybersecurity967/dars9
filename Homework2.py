import matplotlib.pyplot as plt

fanlar = ["Matematika", "Python", "Ingliz tili", "Fizika", "Tarix"]
ballar = [85, 95, 72, 80, 88]

plt.bar(fanlar, ballar, color="skyblue", edgecolor="black")
plt.title("O'quvchining fanlardan olgan ballari")
plt.xlabel("Fanlar")
plt.ylabel("Ballar")
plt.show()