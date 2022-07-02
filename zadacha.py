#-----------------------------------------------------------------------------------------------------------------

#задача

# Создайте класс Factory и внутри создайте 2 метода:
# Метод engine который возвращает строку "Двигатель создан"
# Метод bridge который возвращает строку "Ходовая часть создана"
# Создайте класс Toyota который будет НАСЛЕДОВАТЬ класс Factory. В классе Toyota создайте методы wheels и windows.
# Метод wheels возвращает строку "Колёса готовы"
# Метод windows возвращает строку "Стёкла готовы"
# Из класса Toyota вызовите все методы, методы вернут вам строки(объекты)
# Результат каждого метода вставьте в лист

# class Factory:
#     def engine(self):
#         return 'Двигатель создан'
#     def bridge(self):
#         return 'Ходовая часть создана'
# class Toyota(Factory):
#     def wheels(self):
#         return 'Колеса готовы'
#     def windows(self):
#         return 'Стекла готовы'
# motor = Toyota()
# print(motor.engine())
# print(motor.bridge())
# print(motor.wheels())
# print(motor.windows())

#---------------------------------------------------------------------------------------------------------------------

#задача

# Создайте Класс Zoo.
# Инициализируйте класс в объект.
# К объекту Zoo добавьте атрибут animal_1 и присвойте ему значение "Тигр"
# К объекту Zoo добавьте атрибут animal_2 и присвойте ему значение "Бегемот"
# К объекту Zoo добавьте атрибут animal_3 и присвойте ему значение "Жираф"
# В объекте Zoo измените значение атрибута animal_1 и присвойте ему значение "Лев".
# К объекту Zoo добавьте атрибут animal_4 и присвойте ему list состоящий из animal_2 и animal_3
# В объекте Zoo измените значение атрибута animal_3 и присвойте ему значение "Змея".

# class Zoo:
#     def __init__(self, animal_1 = 'Тигр', animal_2 = 'Бегемот', animal_3 = 'Жираф') -> None:
#         self.animal_1 = animal_1
#         self.animal_2 = animal_2
#         self.animal_3 = animal_3
#         self.animal_4 = []
# z = Zoo(animal_1='Лев')
# print(z.animal_1)
# print(z.animal_2)
# print(z.animal_3)
# z.animal_4.append(z.animal_2)
# z.animal_4.append(z.animal_3)
# print(z.animal_4)
# z = Zoo(animal_3='змея')
# print(z.animal_3)

#-----------------------------------------------------------------------------------------------------------------------

#задача

# Тип дома, общая площадь и наименования мебели. В новом доме мебели нет вообще.
# Мебель имеет название и площадь, из которых Кровать: 4 кв.м Шкаф: 2 кв.м Стол: 1,5 кв.м
# Добавьте в дом вышеперечисленные три предмета мебели.
# При печати дома требуется вывод: тип дома, общая площадь, оставшаяся площадь, список наименований мебели.

# class House:
#     tip_of_house = 'квартира'
#     ob_ploshad = 0
#     krovat = 'квовать'
#     shkaf = 'шкаф'
#     stol = 'стол'

# class NewHouse(House):
#     def __init__(self, krovat_s = 4, shkaf_s = 2, stol_s = 1.5, ploshad = House.ob_ploshad):
#         self.krovat_s = krovat_s
#         self.shkaf_s = shkaf_s
#         self.stol_s = stol_s
#         self.ploshad = ploshad
        
#     def vyvod(self):
#         return f'''
#         тип дома: {House.tip_of_house} 
#         общая площадь: {self.ploshad}
#         оставшаяся плошадь: {self.ploshad - self.krovat_s - self.shkaf_s - self.stol_s}
#         список наименований мебели: {self.krovat, self.shkaf, self.stol}'''

# v = NewHouse(ploshad = 60)
# print(v.vyvod())

#-------------------------------------------------------------------------------------------------------------------------

#задача

# 3)Car 
# Создайте класс Car. Пропишите в конструкторе параметры make, model, year, odometer, fuel. 
# Пусть у показателя odometer будет первоначальное значение 0, 
# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В самом начале проверьте, 
# хватит ли вам бензина из расчета того, что машина 
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние, 
# то пусть этот метод добавляет эти километры к значению одометра, но не 
# напрямую, а с помощью приватного метода __add_distance. 
# Помимо этого пусть метод drive также отнимет потраченное количество бензина с помощью 
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s drive!”. 
# Если же бензина не хватит, то распечатайте “Need more fuel, please, fill more!”

# class Car:
#     def __init__(self, make, model, year, odometer = 0, fuel = 70):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = odometer
#         self.fuel = fuel

#     def drive(self, distance):
#         self.distance = distance

#     def _Car__add_distance(self):
#         if self.distance * 0.1 <= 70:
#             s = self.odometer + self.distance
#             print(s)
    
#     def _Car__subtract_fuel(self):
#         q = self.fuel - (self.distance * 0.1)
#         if q > 0:
#             print("Let’s drive!")
#         else:
#             print('Need more fuel, please, fill more!')


# b = Car('Germany', 'Mersedes', 2012)
# print(b.make)
# print(b.model)
# print(b.year)
# b.drive(850)
# b._Car__add_distance()
# b._Car__subtract_fuel()

#---------------------------------------------------------------------------------------------------------------------

# задача

# Student
# Создайте класс Student, конструктор которого имеет параметры name, lastname,
# department, year_of_entrance. Добавьте метод get_student_info, который
# возвращает имя, фамилию, год поступления и факультет в
# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:
# Программирование.”

# class Student:
#     def __init__(self, name, last_name, department, year_of_entrance):
#         self.name = name
#         self.last_name = last_name
#         self.department = department
#         self.year_of_entrance = year_of_entrance

#     def get_student_info(self):
#         return f'{self.name} {self.last_name} поступил в {self.year_of_entrance} году на факультет: {self.department}'
# s_i = Student('Вася', 'Иванов', 'Программирование', 2017)
# print(s_i.get_student_info())

#------------------------------------------------------------------------------------------------------------------------

#задача

# 2)Airplane
# Создайте новый класс Airplane. Создайте следующие характеристики (полей)
# объекAта:
# ● make (марка)
# ● model
# ● year
# ● max_speed
# ● odometer
# ● is_flying
# и методы имитирующих поведение самолета take off (взлет), fly (летать), land
# приземление). Метод take off должен изменить is_flying на True, а land на False. По
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
# все методы класса.

# class Airplane:
#     def __init__(self, make, model, year, max_speed, odometer, is_flying = False):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer = odometer
#         self.is_flying = is_flying

#     def take_off(self, is_flying):
#         return is_flying

#     def fly(self, distance):
#         self.distance = distance
#         return self.odometer + self.distance
        
        
#     def land(self, is_flying):
#         return is_flying

# d = Airplane('Боинг', '747-400', 2015, 933, 30000)
# print(d.take_off(True))
# print(d.land(False))
# print(d.fly(20000))

#------------------------------------------------------------------------------------------------------------------------

# 4)AK-47
# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)
# Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.
# Where soldier will fire from a gun and reload, and fire one more time.

# class Soldier:
#     name = 'Ryan'

# class Guns(Soldier):
#     def __init__(self, gun = 'AK47', bullets = 5) -> None:
#         self.gun = gun
#         self.bullets = bullets
    
# class Act_of_Shooting(Guns):
#     def fire(self):
#         while self.bullets>0:
#             print('tah-tah')
#             self.bullets-=1
#         if self.bullets==0:
#             print('у вас закончился пуля, перезаряжайте')
#             self.bullets+=5
#             print('перезаряжена')
#         for i in range(self.bullets):
#             print('tah-tah')

# f = Act_of_Shooting()
# f.fire()

#----------------------------------------------------------------------------------------------------------------------

#задача

# Создайте класс Soda (для определения типа газированной воды), 
# принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду). 
# В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, 
# а иначе отобразится следующая фраза: «Обычная газировка».

# class Soda:
#     def __init__(self, dobavka = 0) -> None:
#         self.dobavka = dobavka

#     def sow_my_drink(self):
#         if self.dobavka:
#             print(f'Газирока и {self.dobavka}')
#         else:
#             print('Обычная газировка')

# g = Soda('лимонная')
# g.sow_my_drink()

#--------------------------------------------------------------------------------------------------------------------------

# задача

# Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. 
# Для этого он решил создать класс TriangleChecker, принимающий только положительные числа. 
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.

# Построить треугольник из отрезков можно лишь в одном случае: сумма длин двух любых сторон всегда больше третьей.

# class TriangleChecker:
#     def __init__(self, sides) -> None:
#         self.sides = sides

#     def is_triangle(self):
#         if all(isinstance(side, (int, float)) for side in self.sides):
#             if all(side > 0 for side in self.sides):
#                 sorted_sides = sorted(self.sides)
#                 if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
#                     return 'Ура, можно построить треугольник!'
#                 return 'Жаль, но из этого треугольник не сделать'
#             return 'С отрицательными числами ничего не выйдет!'
#         return 'Нужно вводить только числа!'

# triangle1 = TriangleChecker([2, 3, 4])
# print(triangle1.is_triangle())
# triangle2 = TriangleChecker([77, 3, 4])
# print(triangle2.is_triangle())
# triangle3 = TriangleChecker([77, 3, 'Сторона3'])
# print(triangle3.is_triangle())
# triangle4 = TriangleChecker([77, -3, 4])
# print(triangle4.is_triangle())

#---------------------------------------------------------------------------------------------------------------------------








    
