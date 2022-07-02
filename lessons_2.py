

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
#         return 'Ходовая готова'

# class Toyota(Factory):
#     def wheel(self):
#         return 'Колеса готовы'
    
#     def window(self):
#         return 'Окна готовы'

# t = Toyota()
# print(t.engine())
# print(t.bridge())
# print(t.window())
# print(t.wheel())




# Создайте Класс Zoo.
# Инициализируйте класс в объект.
# К объекту Zoo добавьте атрибут animal_1 и присвойте ему значение "Тигр"
# К объекту Zoo добавьте атрибут animal_2 и присвойте ему значение "Бегемот"
# К объекту Zoo добавьте атрибут animal_3 и присвойте ему значение "Жираф"
# В объекте Zoo измените значение атрибута animal_1 и присвойте ему значение "Лев".
# К объекту Zoo добавьте атрибут animal_4 и присвойте ему list состоящий из animal_2 и animal_3
# В объекте Zoo измените значение атрибута animal_3 и присвойте ему значение "Змея".

# class Zoo:
#     def __init__(self):
#         self.animal_1 = 'Тигр'
#         self.animal_2 = "Бегемот"
#         self.animal_3 = "Жираф"
#         self.animal_4 = []

# z = Zoo()
# z.animal_1 = 'Лев'
# print(z.animal_1)
# print(z.animal_2)
# print(z.animal_3)
# z.animal_4 = []
# z.animal_4.append(z.animal_2)
# z.animal_4.append(z.animal_3)
# print(z.animal_4)
# z.animal_3 = 'Змея'
# print(z.animal_3)





# Тип дома, общая площадь и наименования мебели. В новом доме мебели нет вообще.
# Мебель имеет название и площадь, из которыхКровать: 4 кв.м Шкаф: 2 кв.м Стол: 1,5 кв.м
# Добавьте в дом вышеперечисленные три предмета мебели.
# При печати дома требуется вывод: тип дома, общая площадь, оставшаяся площадь, список наименований мебели.

# class House:
#     type_home = 'Квартира'
#     ploshad = 0
#     kravat_name = 'Кровать'
#     shkaf_name = 'Шкаф'
#     stol_name = 'Стол'
#     kravat = 4
#     shkaf = 2
#     stol = 1.5

# class MyHome(House):
#     def __init__(self, ploshad):
#         self.ploshad = ploshad
#         self.kravat = House.kravat
#         self.shkaf = House.shkaf
#         self.stol = House.stol
#     def vyvod(self):
#         return f'''
#         Тип дома: {self.type_home}
#         Общая площадь: {self.ploshad}
#         Оставщаяся площадь {self.ploshad-self.shkaf-self.kravat-self.stol} m2 
#         список наименований мебели:{self.kravat_name, self.shkaf_name, self.stol_name} '''

# s = MyHome(60)
# print(s.vyvod())







# Нужно создать класс который принимет модель ноутбука(Acer, Asus, ...) и возвращает полную комплектацию ноутбука со \n
# всеми характеристиками.
# В характеристики должны входить:
# Процессор
# Оперативная Память
# Видео карта
# Жёсткий Диск
# Материнская плата
# Размер экрана
# Для каждой характеристики создайте внутри класса функцию которая добавляет по одной характеристики к Dictionary.
# В итоге Ваш класс должен вернуть Dictionary в котором перечислены: 
# Модель Ноутбука и его Характеристики.  

# class Aser:
#     def __init__(self, cpu, ram, video_card, ssd, mother_board, screen_size) -> None:
#         self.cpu = cpu
#         self.ram = ram
#         self.video_card = video_card
#         self.ssd = ssd
#         self.mother_board = mother_board
#         self.screen_size = screen_size
    
#     def display(self):
#         return {
#             'cpu': self.cpu,
#             'ram': self.ram,
#             'video_card': self.video_card,
#             'ssd': self.ssd,
#             'mother_board': self.mother_board,
#             'screen_size': self.screen_size
#             }
        
# class Hp:
#     def __init__(self, cpu, ram, video_card, ssd, mother_board, screen_size) -> None:
#         self.cpu = cpu
#         self.ram = ram
#         self.video_card = video_card
#         self.ssd = ssd
#         self.mother_board = mother_board
#         self.screen_size = screen_size
        
#     def display(self):
#         return {
#             'cpu': self.cpu,
#             'ram': self.ram,
#             'video_card': self.video_card,
#             'ssd': self.ssd,
#             'mother_board': self.mother_board,
#             'screen_size': self.screen_size
#             }
        

# class Leptop(Aser, Hp):
#     def __init__(self, cpu, ram, video_card, ssd, mother_board, screen_size) -> None:
#         super().__init__(cpu, ram, video_card, ssd, mother_board, screen_size)

#     def leptops(self):
#         return {
#             'Aser' : self.display(),
#             'Hp' : self.display() 
#         }


# s = Leptop('intel core i7', '14 GB', 'GEFORCE', 'SSD Teamgroup NVMe MP33 128GB M.2 2280', 'Asus Prime H310M-K',
#            '13–15 дюймов 1400 × 1050')

# print(s.leptops())




# 3)Car 
# Создайте класс Car. Пропишите в конструкторе параметры make, model, year, odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0, 
# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В самом начале проверьте, хватит ли вам бензина из расчета того, что машина 
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние, то пусть этот метод добавляет эти километры к значению одометра, но не 
# напрямую, а с помощью приватного метода __add_distance. Помимо этого пусть метод drive также отнимет потраченное количество бензина с помощью 
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill more!”

# class Car:
#     def __init__(self, make, model, year, odometer = 0, fuel = 70) -> None:
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = odometer
#         self.fuel = fuel

#     def drive(self, distance):
#         self.distance = distance

#     def _Car__add_distance(self):
#         if self.distance*0.1<=70:
#             s = self.odometer + self.distance
#             print(s)

#     def _Car__subtract_fuel(self):
#         q = self.fuel - (self.distance*0.1)
#         if q > 0:
#             print("Let's drive!")
#         else:
#             print("Need more fuel, please, fill more!")

# d = Car('Toyota', 'Hilander', 2011)
# print(d.make)
# print(d.model)
# print(d.year)
# d.drive(700)
# d._Car__add_distance()
# d._Car__subtract_fuel()




# 1)Student
# Создайте класс Student, конструктор которого имеет параметры name, lastname,
# department, year_of_entrance. Добавьте метод get_student_info, который
# возвращает имя, фамилию, год поступления и факультет в
# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:
# Программирование.”

# class Student:
#     def __init__(self, name, lastname, department, year_of_entrance) -> None:
#         self.name = name
#         self.lastname = lastname
#         self.department = department
#         self.year_of_entrance = year_of_entrance


#     def get_student_info(self):
#         return f'{self.name} {self.lastname} поступил в {self.year_of_entrance} г. на факультет:{self.department}'

# i = Student('Вася', 'Иванов', 'Программирование', 2017)
# print(i.get_student_info())




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
#     def __init__(self, make, model, year, max_speed, odometer, is_flying = False) -> None:
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

# a = Airplane('Боинг', '747-400', 2015, 933, 30000)
# print(a.make)
# print(a.model)
# print(a.year)
# print(a.max_speed)
# print(a.odometer)
# print(a.take_off(True))
# print(a.fly(10000))
# print(a.land(False))
    






# Нужно создать класс который принимет данные в формате dict. Эти данные, вы сможете взять из Classroom Data #1.
# Вам нужно создать 6 методов класса:
# Получить все ключи в TUPLE.
# Получить все значения в TUPLE.
# Получить все ключи в LIST.
# Получить все значения в LIST.
# Получить все ключи в SET.
# Получить все значения в SET.
# Ниже когда вы будете передавать Словарь классу и вызывать из него любой метод Вы должны получать соответсвенно нужные типы данных.
# Example: my_class = Parser("DICT") | my_class.get_keys_tuple()

# Data #1:
# colors = {
#     "black": {"category": "hue", "type": "primary", "code": {"rgba": [255, 255, 255, 1], "hex": "#000"}},
#     "white": {"category": "value", "code": {"rgba": [0, 0, 0, 1], "hex": "#FFF"}},
#     "red": {"category": "hue", "type": "primary", "code": {"rgba": [255, 0, 0, 1], "hex": "#FF0"}},
#     "blue": {"category": "hue", "type": "primary", "code": {"rgba": [0, 0, 255, 1], "hex": "#00F"}},
#     "yellow": {"category": "hue", "type": "primary", "code": {"rgba": [255, 255, 0, 1], "hex": "#FF0"}},
#     "green": {"category": "hue", "type": "secondary", "code": {"rgba": [0, 255, 0, 1], "hex": "#0F0"}}
# }

# class TakeDict:
#     def __init__(self, dic) -> None:
#         self.dic = dic

#     def get_keys_tuple(self):
#         keys = []
#         for i in self.dic.keys():
#             keys.append(i)

#             a = self.dic.get(i)
#             for j in a.keys():
#                 keys.append(j)

#                 try:
#                     d = a.get(j)
#                     for s in d.keys():
#                         keys.append(s)
#                 except:
#                     pass

#         print(tuple(keys))

#     def get_values_tuple(self):
#         values = []

#         for i in self.dic.values():
#             values.append(i)

#             a = i.values()
#             for j in a:
#                 values.append(j)
#                 try:
#                     b = j.values()
#                     for c in b:
#                         values.append(c)

#                         d = c.vlaues()
#                         for e in d:
#                             values.append(e)

#                             f = e.values()
#                             for h in f:
#                                 values.append(h)
#                 except:
#                     pass

#         print(tuple(values))

#     def get_keys_list(self):
#         keys = []
#         for i in self.dic.keys():
#             keys.append(i)

#             a = self.dic.get(i)
#             for j in a.keys():
#                 keys.append(j)

#                 try:
#                     b = a.get(j)
#                     for k in b.keys():
#                         keys.append(k)
#                 except:
#                     pass
#         print(keys)

#     def get_value_list(self):
#         values = []
#         for i in self.dic.values():
#             values.append(i)

#             a = i.values()
#             for j in a:
#                 values.append(j)

#                 try:
#                     b = j.values()
#                     for k in b:
#                         values.append(k)

#                         c = k.valuse()
#                         for l in c:
#                             values.append(l)

#                             d = l.values()
#                             for m in d:
#                                 values.append(m)
#                 except:
#                     pass

#         print(values)

#     def get_keys_set(self):
#         sets = []
#         for i in self.dic.keys():
#             sets.append(i)

#             a = self.dic.get(i)
#             for j in a.keys():
#                 sets.append(j)

#                 try:
#                     b = a.get(j)
#                     for k in b.keys():
#                         sets.append(k)
#                 except:
#                     pass

#         print(set(sets))


# t = TakeDict(colors)
# t.get_keys_tuple()
# t.get_values_tuple()
# t.get_keys_list()
# t.get_value_list()
# t.get_keys_set()







# 4)AK-47
# Soldier Ryan has an AK47
# Soldiers can fire ("tigi-tigitishh").
# Guns can fire bullets.
# Guns can fill bullets - increase the number of bullets(reloads)
# Create class Act_of_Shooting, which will inheritates from class Soldier, class Guns.
# Where soldier will fire from a gun and reload, and fire one more time.

# class Soldier:
#     def __init__(self, name = 'Ryan') -> None:
#         self.name = name

# class Gun(Soldier):
#     def __init__(self, gun = 'AK47', bullets =10) -> None:
#         self.gun = gun
#         self.bullets = bullets

# class Act_of_Shooting(Gun):
#     def fire(self):
#         while self.bullets > 0:
#             print('tah-tah')
#             self.bullets-=1
#         if self.bullets == 0:
#             print('У нас пуля закончена')
#             self.bullets+=5
#             print('перезаряжена, продолжать стрелять')
#         for i in range(self.bullets):
#             print('tah-tah')
            

# b = Act_of_Shooting()
# b.fire()









# class Human:
#     #Статические поля
#     default_name = 'No name'
#     default_age = 0

#     def __init__(self, name = default_name, age = default_age):
#         #Динамические поля
#         #Публичные
#         self.name = name
#         self.age = age
#         #Приватные
#         self.__money = 0
#         self.__house = None

#     def info(self):
#         print(f'Name: {self.name}')
#         print(f'Age: {self.age}')
#         print(f'Money: {self.__money}')
#         print(f'House: {self.__house}')

#     # Статический метод
#     @staticmethod
#     def default_info():
#         print(f'Default Name: {Human.default_name}')
#         print(f'Default Age: {Human.default_age}')


#     def earn_money(self, amount):
#         self.__money += amount
#         print(f'Earned {amount} money! Current value: {self.__money}')

#     def buy_house(self, house, discount):                   # ?????????????????
#         price = house.final_price(discount)
#         if self.__money >= price:
#             self.__make_deal(house, price)
#         else:
#             print('Not enough money!')

#     # Приватный метод
#     def __make_deal(self, house, price):                   #??????????????????
#         self.__money -= price
#         self.__house = house

# class House:

#     def __init__(self, area, price):
#         self._area = area
#         self._price = price

#     def final_price(self, discount):
#         final_price = self._price * (100 - discount) / 100
#         print(f'Final price: {final_price}')
#         return final_price

# class SmallHouse(House):
#     default_area = 40

#     def __init__(self, price):
#         super().__init__(SmallHouse.default_area, price)

# if __name__ == '__main__':                    #????????????????????????

#     Human.default_info()

#     alexander = Human('Sasha', 27)
#     alexander.info()

#     small_house = SmallHouse(8_500)

#     alexander.buy_house(small_house, 5)

#     alexander.earn_money(5_000)
#     alexander.buy_house(small_house, 5)

#     alexander.earn_money(20_000)
#     alexander.buy_house(small_house, 5)
#     alexander.info()

        
# Нужно создать класс который принимает Classroom Data #2 данные.
# И внутри класса создать несколько методов:
# Метод который вернёт все имена отелей.
# Метод который из собирает все name в один Tuple и locations в другой и возвращает dictionary c двумя ключами списками со всеми значениями.
# 3.Метод который добавит к каждому элементу в markers поле 
# status_id: 1

# data = {
#     "markers": 
#     [
#         {
#             "name": "Rixos The Palm Dubai",
#             "position": [25.1212, 55.1535]
#         },
#         {
#             "name": "Shangri-La Hotel",
#             "location": [25.2084, 55.2719]
#         },
#         {
#             "name": "Grand Hyatt",
#             "location": [25.2285, 55.3273]
#         }
#     ]
# }
        
# class Data:

#     def __init__(self, data):
#         self.data = data

    
#     def get_names_tuple(self):
            
#         names = []
#         for value in self.data.get('markers'):
#             names.append(value['name'])

#         return tuple(names)

#     def get_location_tuple(self):
#         loc = []

#         for values in self.data.get('markers'):
#             for key, value in values.items():
#                 if key in ['location','position']:
#                     loc.append(value)

#         return tuple(loc)
    
#     def get_dict_all(self):
#         markers = {
#             'name':self.get_names_tuple(),
#             'location': self.get_location_tuple()
#             }
#         return markers

#     def add_field_id(self):
#         for key, val in self.data.items():
#             for i in val:
#                 i['status_id'] = 1
#                 print(i)
            

# d  = Data(data)
# # print(d.get_names_tuple())
# # print(d.get_location_tuple())
# # print(d.get_dict_all())
# d.add_field_id()











