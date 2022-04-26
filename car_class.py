class Transport:
    def __init__(self, power, cost, number, brand):
        self.power = power  # Мощность
        self.cost = cost  # Стоимость
        self.number = number  # Номер
        self.brand = brand  # Марка


class Automobile(Transport):
    def __init__(self, power, cost, number, brand, mileage, tech_inspection):
        super().__init__(power, cost, number, brand)
        self.mileage = mileage  # Пробег
        if tech_inspection:
            self.tech_inspection = "Пройден"
        else:
            self.tech_inspection = "Не пройден"


    def __repr__(self):
        return f'Номер: {self.number}; Мощность: {self.power}; Стоимость: {self.cost}; Марка: {self.brand}; ' \
               f'Пробег: {self.mileage}; Прохождение техосмотра: {self.tech_inspection} '


class Aircraft(Transport):
    def __init__(self, power, cost, number, brand, max_flight_altitude):
        super().__init__(power, cost, number, brand)
        self.max_flight_altitude = max_flight_altitude  # Максимальная высота полета

    def __repr__(self):
        return f'Номер: {self.number}; Мощность: {self.power}; Стоимость: {self.cost}; Марка: {self.brand}; ' \
               f'Макс. высота полета: {self.max_flight_altitude}'
