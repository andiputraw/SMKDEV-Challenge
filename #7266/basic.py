import time

class Person:
    def __init__(self,mass : int, height : float, name: str):
        self.mass = mass
        self.height = height
        self.name = name

    def calc_bmi(self) -> float:
        return self.mass / (self.height * self.height)

def highest_bmi(person1: Person, person2:Person):
    if person1.calc_bmi() > person2.calc_bmi():
        print(f"BMI {person1.name} Lebih tinggi dari {person2.name}")
    else:
        print(f"BMI {person2.name} Lebih tinggi dari {person1.name}")

start = time.perf_counter()

udin = Person(78,1.69,"Udin")
nanang = Person(92,1.95,"Nanang")

highest_bmi(udin,nanang)

udin2 = Person(95,1.88, "Udin")
nanang2 = Person(85,1.76, "Nanang")

highest_bmi(udin2,nanang2)

print(f"\nTime Elapsed: {time.perf_counter() - start} seconds")



