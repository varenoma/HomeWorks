from collections import namedtuple


Car = namedtuple("Car",["brand", "model", "year", "price"])

cars = (
    Car("BMW", "M8 Competition", 2023, 135000),
    Car("Toyota", "Supra MK4", 1998, 80000),
    Car("Nissan", "GT-R R35", 2022, 120000),
    Car("Dodge", "Challenger SRT Hellcat", 2021, 85000)
)

m_max = max(cars, key=lambda x: x.price)
print(f"brand: {m_max.model}, price: {m_max.price}")