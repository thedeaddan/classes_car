from car_class import Automobile, Aircraft
import sys

cars_list = list()
airplanes_list = list()

while True:
    com = input('Введите команду (help для получения списка команд): ').lower()

    if com == '1':
        power = input('Введите мощность: ')
        cost = input('Введите стоимость: ')
        number = input('Введите номер: ')
        brand = input('Введите марку: ')
        mileage = input('Введите пробег: ')
        tech_inspection = input('Пройден ли техосмотр (y/n):')
        while True:
            if tech_inspection == 'y':
                tech_inspection = True
                break
            elif tech_inspection == 'n':
                tech_inspection = False
                break
            else:
                print('Используйте англ раскладку и введите "y" для подтверждения или "n" в ином случае!')
                tech_inspection = input('    Пройден ли техосмотр (y/n): ')
        auto = Automobile(power, cost, number, brand, mileage, tech_inspection)
        cars_list.append(auto)

    elif com == '2':
        power = input('Введите мощность: ')
        cost = input('Введите стоимость: ')
        number = input('Введите номер: ')
        brand = input('Введите марку: ')
        max_flight_altitude = input('Введите максимальную высоту полета: ')
        air = Aircraft(power, cost, number, brand, max_flight_altitude)
        airplanes_list.append(air)

    elif com == '3':
        i = 1
        if len(cars_list) > 0:
            print('Выберите автомобиль:')
            for car in cars_list:
                print(f'{i}) Номер - {car.number}, марка - {car.brand}')
                i += 1
            num = int(input('Выберите порядковый номер автомобиля: ')) - 1
            print(f'''
Пробег данного автомобиля составляет - {cars_list[num].mileage}
Стоимость данного автомобиля составляет - {cars_list[num].cost}
''')

    elif com == '4':
        all_cost = 0
        for car in cars_list:
            all_cost += int(car.cost)
        tax = all_cost / 100 * 5
        print(f'Налог на регистрации всех машин составляет: {tax}')

    elif com == '5':
        cost = 0
        for car in cars_list:
            if int(car.cost) > cost:
                cost = int(car.cost)
        for car in cars_list:
            if int(car.cost) == cost:
                if car.tech_inspection:
                    print('Владелец самой дорогой машины прошел техосмотр!')
                else:
                    print('Владелец самой дорогой машины не проходил техосмотр!')

    elif com == '6':
        i = 1
        print('Выберите самолет:')
        for air in airplanes_list:
            print(f'{i}) Номер - {air.number}, марка - {air.brand}')
            i += 1
        num = int(input('Выберите порядковый номер самолета: ')) - 1
        print(f'''
Мощность данного самолета - {airplanes_list[num].power}
Макс. высота полета данного самолета - {airplanes_list[num].max_flight_altitude}
''')

    elif com == '7':
        all_cost = 0
        if len(airplanes_list) > 0:
            for air in airplanes_list:
                all_cost += int(air.cost)
            tax = all_cost / 100 * 3
            print(f'Налог на регистрации всех самолетов составляет: {tax}')

    elif com == '8':
        cost = 0
        for air in airplanes_list:
            if int(air.cost) > cost:
                cost = int(air.cost)
        for air in airplanes_list:
            if int(air.cost) == cost:
                print(f'''
Мощность самого дорогого самолета - {air.cost}
тоимость самого дорогого самолета - {air.cost}
Марка самого дорогого самолета - {air.brand}
''')

    elif com == '9':
        count = 1
        if len(cars_list) > 0:
            print('Машины:')
            for car in cars_list:
                print(f'    {count}) {car}')
                count += 1
        count = 1
        if len(airplanes_list) > 0:
            print('Самолеты:')
            for airplane in airplanes_list:
                print(f'    {count}) {airplane}')
                count += 1
        if len(airplanes_list) == 0 and len(cars_list) == 0:
            print('Вы не ввели никаких данных о машинах и самолетах')

    elif com == 'help':
        print('''
Список команд:
1 - Добавление автомобиля
2 - Добавление самолета
3 - Получение стоимости и пробега определенного автомобиля
4 - Подсчитать налог с регистрации всех машин
5 - Выяснить прошел ли владелец самой дорогой машины техосмотр
6 - Выяснить для заданного самолета мощность и максимальную высоту полета
7 - Подсчитать налог с регистрации всех самолетов
8 - Определить мощность, стоимость и марку самого дорогого самолета
9 - Получить полную информацию обо всех автомобилях и самолетах
''')
    elif com == 'exit':
        sys.exit(0)
