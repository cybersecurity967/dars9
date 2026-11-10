import matplotlib.pyplot as plt

ismlar = ["Ali", "Vali", "Sardor", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]

max_ball = max(ballar)
min_ball = min(ballar)
max_talaba = ismlar[ballar.index(max_ball)]
min_talaba = ismlar[ballar.index(min_ball)]

orta_ball = sum(ballar) / len(ballar)

print(f"Eng yuqori ball: {max_talaba} ({max_ball})")
print(f"Eng past ball: {min_talaba} ({min_ball})")
print(f"O'rtacha ball: {orta_ball:.2f}")

plt.bar(ismlar, ballar, color="mediumseagreen", edgecolor="black")

plt.title("O'quvchilarning imtihon natijalari")
plt.xlabel("O'quvchilar")
plt.ylabel("Ballar")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig("oquvchilar_natijasi.png")
plt.show()