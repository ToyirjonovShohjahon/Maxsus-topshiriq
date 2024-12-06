# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_11pUf0G5sXIauHRmCLF47Ffa31LNsrE
"""

import numpy as np
import matplotlib.pyplot as plt

# X qiymatlari
x = np.linspace(0, 10, 100)
# Y qiymatlari
y = np.sin(x)

# Grafikni chizish
plt.plot(x, y, label="Sinus(x)", color="blue")

# Grafikning nomi va o'qlari
plt.title("Sinus Funktsiyasining Grafiki")
plt.xlabel("X qiymatlari")
plt.ylabel("Y qiymatlari")

# To'rlarni qo'shish
plt.grid(True)

# Legenda qo'shish
plt.legend()

# Grafikni ko'rsatish
plt.show()

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.random.uniform(0, 10, 50)
y = np.random.uniform(0, 10, 50)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Nuqtalar')

plt.title('Tasodifiy Nuqtalar Scatter Grafiki', fontsize=14)
plt.xlabel('X qiymatlari', fontsize=12)
plt.ylabel('Y qiymatlari', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

import pandas as pd

data = pd.read_csv("WHO COVID-19 cases.csv")

print("Ma'lumotlarning birinchi 5 qatori:")
print(data.head())

cases_by_country = data.groupby("Country").sum()["Cumulative_cases"]

print("\nHar bir davlat bo'yicha umumiy COVID-19 holatlari:")
print(cases_by_country)

country_filter = "Uzbekistan"
uzbekistan_data = data[data["Country"] == country_filter]

print(f"\n{country_filter} uchun ma'lumotlar:")
print(uzbekistan_data)

import matplotlib.pyplot as plt

top_10_countries = cases_by_country.sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
top_10_countries.plot(kind="bar", color="skyblue")
plt.title("Eng ko'p COVID-19 holatlari aniqlangan davlatlar", fontsize=16)
plt.xlabel("Davlat", fontsize=12)
plt.ylabel("Cumulative Cases", fontsize=12)
plt.xticks(rotation=45)
plt.show()

from PIL import Image
import matplotlib.pyplot as plt

# Rasmlarni yuklash (rasm nomlarini o'zgartiring yoki Colabga o'zingizning rasmlaringizni yuklang)
file_paths = ["vini.jpg", "jude.jpg", "fede.jpg"]  # O'zingiz yuklagan rasm fayl nomlari

# Rasmni oq-qora formatga o'tkazish va ko'rsatish
plt.figure(figsize=(15, 5))  # Grafik o'lchami
for i, file_path in enumerate(file_paths):
    # Rasmni ochish
    img = Image.open(file_path)

    # Oq-qora formatga o'tkazish
    img_gray = img.convert("L")

    # Asl va oq-qora rasmlarni ko'rsatish
    plt.subplot(2, 3, i + 1)
    plt.imshow(img)
    plt.title(f"Asl rasm {i + 1}")
    plt.axis("off")

    plt.subplot(2, 3, i + 4)
    plt.imshow(img_gray, cmap="gray")
    plt.title(f"Oq-qora rasm {i + 1}")
    plt.axis("off")

plt.tight_layout()
plt.show()