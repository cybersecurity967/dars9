import matplotlib.pyplot as plt

tillar = ["Python", "C", "JavaScript", "Java"]
oquvchilar = [15, 8, 12, 5]

plt.pie(oquvchilar, labels=tillar, autopct="%1.1f%%", startangle=140)
plt.title("Sevimli dasturlash tillari")
plt.axis("equal") 
plt.show()