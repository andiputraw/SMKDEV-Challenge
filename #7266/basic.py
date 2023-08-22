# Diselesaikan dengan pendekatan Imperative dan didesain agar bisa di maintain dengan mudah (kalaupun sebenernya gak perlu jgua sih)

# Pertanyaan

# Pada suatu hari udin dan nanang sedang mencoba membandingkan BMI (Indeks Massa Tubuh) mereka, yang dihitung menggunakan rumus: BMI = massa / tinggi ** 2 = massa / (tinggi * tinggi) (massa dalam kg dan tinggi dalam meter).

# Tugas Anda, bantulah udin dan nanang menghitung BMI mereka mengikuti langkah langkah berikut ini:

# 1. Simpan massa dan tinggi udin dan nanang dalam sebuah variabel.

# 2. Hitunglahﾠ kedua BMI mereka menggunakan rumus (kamu bahkan dapat mengimplementasikan kedua versi rumus diatas).

# 3. Buat variabel dengan output Boolean yang berisi informasi apakah udin memiliki BMI yang lebih tinggi daripada nanang.

# 4. Tampilkan keluaran yang bagus di konsol, yang menyatakan siapa yang memiliki BMI yang lebih tinggi.

# 5. Pesannya dapat berupa “BMI Udin lebih tinggi dari Nanang!” atau sebaliknya.

# 6. Gunakan konsep template literal untuk menyertakan nilai-nilai BMI dalam keluaran. Contoh: “BMI Udin (28,3) lebih tinggi dari Nanang (23,9)!”

import time

class Person:
    def __init__(self,mass : int, height : float, name: str):
        self.mass = mass
        self.height = height
        self.name = name
        self.BMI = round(self.mass / (self.height * self.height), 2) 

def print_bmi(person: Person) -> str:
    return f"{person.name} ({person.BMI})"

def highest_bmi(person1: Person, person2:Person):
    if person1.BMI > person2.BMI:
        print(f"BMI {print_bmi(person1)} Lebih tinggi dari {print_bmi(person2)}")
    else:
        print(f"BMI {print_bmi(person2)} Lebih tinggi dari {print_bmi(person1)}")

start = time.perf_counter()

print("Data 1: \n")
udin = Person(78,1.69,"Udin")
nanang = Person(92,1.95,"Nanang")

highest_bmi(udin,nanang)

print("Data 2: \n")
udin2 = Person(95,1.88, "Udin")
nanang2 = Person(85,1.76, "Nanang")

highest_bmi(udin2,nanang2)

print(f"\nTime Elapsed: {(time.perf_counter() - start) * 1000} miliseconds")



