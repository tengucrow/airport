import data_handling
import os
import time
import datetime

dtn = datetime.datetime


class Airport:
    def __init__(self, airport_name, code, lane_width, planes_capacity, coordinates):
        self.airport_name = airport_name
        self.code = code
        self.lane_width = lane_width
        self.planes_capacity = planes_capacity
        self.coordinates = coordinates
        self.planes = []
        self.all_airports = []

    def add_plane(self, plane):  # добавить самолет на стоянку в аэропорт
        sum_planes = len(self.planes)
        if sum_planes < self.planes_capacity:
            self.planes.append(plane)

    def add_airport(self, name, code, width, capacity, coordinates):  # добавить новый аэропорт
        if name not in self.all_airports:
            data_handling.add_port(name, code, width, capacity, coordinates)
        else:
            # raise ValueError("Such airport already exists")
            print('Such airport already exists')

    def remove_airport(self, name):  # удалить аэропорт
        folder = 'ports'
        data_handling.del_file(folder, name)

    def data_airport(self):  # вывести на экран инфо о данном аэропорте
        return 'Название: ' + self.airport_name + ', код: ' + self.code + ', полоса: ' + str(
            self.lane_width) + ', вместимость: ' + str(self.planes_capacity) + ', координаты: ' + self.coordinates

    def see_all_airports(self):  # посмотреть все аэропорты
        k = data_handling.read_port()
        for i in k:
            j = list(i)
            self.all_airports.append(j[0])
        return self.all_airports

    def list_of_planes(self):  # выіести какие самолеты сейчас в аэропорту
        return (self.all_airports)

    def __repr__(self):
        return self.airport_name + ' ' + self.code + ' ' + self.coordinates


class Flight:
    def __init__(self, flight_number, departure_airport, arrival_airport, plane_name):
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.plane_name = plane_name
        self.flight_dist = round(data_handling.calc_dist_fixed(departure_airport.coordinates, arrival_airport.coordinates)) # Вычисляю расстояние между аэропортами и округляю его чтобы передать как целое число

    def __repr__(self):
        return str(self.flight_number)


class Commander:

    # Метод добавления рейса. Рейс добавляется автоматически. Значения вытягиваются из параметров добавленных классов
    def add_flight(self, fl):
        f = open('Future_f.txt', 'r')
        t = f.readlines()
        f.close()

        for i in t:  # Проверяю существует ли уже в файле такой рейс
            a = i.strip()
            if str(fl.flight_number) == i.split(';')[0]:
                print(f'Flight number {fl.flight_number} aleady exists')
                break
        else:  # Eсли рейс не существует, добавляю его

            f2 = open('Future_f.txt', 'a')
            f2.write(
                f'{str(fl.flight_number)}; {fl.departure_airport.airport_name}; {fl.arrival_airport.airport_name}; {fl.plane_name.plane_name}; {str(fl.flight_dist)}\n')
            f2.close()
            print(f'Flight {fl} was successfully added')



    def start_flight(self, fl):

        d = fl.departure_airport # departure airport object
        a = fl.arrival_airport # arrival airport object
        p = fl.plane_name   # plane object 
        n = fl.flight_number # flight number

        f = open('Future_f.txt','r')
        Future_f = f.readlines()
        f.close()

        f = open('Flight.txt', 'r')
        Flight = f.readlines()
        f.close()

        f = open('End_f.txt', 'r')
        End_f = f.readlines()
        f.close()
        
        flight = '' # Пустая переменная в которую будет помещаться строка с данными о рейсе, которая будет помещаться в соответствуюзий документ в зависимости от статуса

        for i in Future_f:

            if str(fl.flight_number) == i.split(';')[0]: # Валидация по наличию самолёта в аэропорту отправки, ширине полосы и свободному месту в аэропорту прибытия

                if p not in d.planes: 
                    print(f'There is no {p.plane_name} plane in {d.airport_name} airport') 
                    
                elif len(a.planes) >= a.planes_capacity:
                    print(f'The hangar of {a.airport_name} airport is full. Not possible to land {p.plane_name} plane')

                elif p.plane_width > a.lane_width:
                    print(f'Line width of the {a.airport_name} airpord doesn\'t support the {p.plane_name} plane model')

                else:
                    flying_index = Future_f.index(i) # Находим индекс рейса в документе
                    flying_data = Future_f.pop(flying_index) # Забираем строку рейса из документа
                    flight = flying_data # Присваивает пустой перенной рейс как значение


        f = open('Future_f.txt', 'w') # Стираем данные из документа
        f.close()

        for i in Future_f: # Заполняем документ будующх полётов данными, без строки о текущем полёте
            f = open('Future_f.txt', 'a')
            f.write(i)
            f.close()

                
        plane_index = d.planes.index(p) # Вычисляю индекс самолёта в списке эропорта отлёта
        plane_in_air = d.planes.pop(plane_index) # Вытаскиваю самолёт из списка на взлёте

        
        Flight.append(flight) # Помещаю текущий полёт в документ с полётами в процессе 

        f = open('Flight.txt', 'a')
        f.write(flight)
        f.close()
        
        p.fly(fl.flight_dist, a.airport_name, d.airport_name) # Взлёт самолёта и приземление
        
        a.planes.append(plane_in_air) # Помещаю приземлившийся самолёт в список аэропорта прибытия

        for i in Flight: # Удаляю строку о завершенном полёте из списка полётов в процессе и добавляю его в список завершённых полётов. 
            if str(fl.flight_number) == i.split(';')[0]:
                flight_index = Flight.index(i)
                flight = Flight.pop(flight_index)

        f = open('Flight.txt', 'w')
        f.close()

        for i in Flight:
            f = open('Flight.txt', 'a')
            f.write(i)
            f.close()

        f = open('End_f.txt', 'a')
        f.write(flight)
        f.close() 

    # Метод удаления рейса. В кач-ве аргументов берёт объект рейса и название документа с рейсом, который нужно удалить. Удаляет все записи, которые содержат номер полёта(flight_number)      
    def remove_flight(self, fl, doc):
    
        file_name = doc + '.txt'
        if file_name in os.listdir():

            f = open(file_name, 'r')
            t = f.readlines()
            f.close()

            flights = []
            
            for i in t:

                if str(fl.flight_number) == i.split(';')[0]: 
                    i = ''

                if i != '':
                    flights.append(i)
                    
            f = open(file_name, 'w')
            f.close()

            f = open(file_name, 'a')
            for i in flights:
                f.write(i)
            f.close()
            
            print(f'Flight {fl} was successfully removed')
        else:
            print('There is no such file')

    # Метод чтения данных из документов с рейсами. В кач-ве аргументов барёт название документа, список рейсов из которого нужно вывести      
    def see_all_flights(self, flights):

        file_name = flights + '.txt'

        if file_name in os.listdir():
            f = open(file_name, 'r')
            t = f.readlines()
            f.close()

            for i in t:
                print(i.strip())
        else:
            print('There is no such file')
            

    def __repr__(self):
        return self.flight_number


class Plane:
    def __init__(self, plane_name, plane_width, plane_dist, plane_speed, place):
        self.plane_name = plane_name
        self.plane_width = plane_width
        self.plane_dist = plane_dist
        self.plane_speed = plane_speed
        self.place = place
        self.all_planes = []

    def add_plane(self, plane_name, plane_width, plane_dist, plane_speed, place):  # добавить новый самолет
        if plane_name not in self.all_planes:
            data_handling.add_plane(plane_name, plane_width, plane_dist, plane_speed, place)
        else:
            # raise ValueError("Such plane already exists")
            print('Such plane already exists')

    def remove_plane(self):  # удалить самолет
        folder = 'planes'
        data_handling.del_file(folder, plane_name)

    def see_all_planes(self):  # посмотреть все самолеты
        k = data_handling.read_planes()
        for i in k:
            j = list(i)
            self.all_planes.append(j[0])
        return self.all_planes

    def fly(self, flight_dist, departure_airport, arrival_airport):
        self.place = departure_airport
        print(self.plane_name + " departed from " + self.place + " to " + arrival_airport + " at " + dtn.now().strftime(
            '%H:%M:%S.'), " Distance to go: " + str(flight_dist) + " km")
        self.place = "At flight"
        print(self.place)
        for i in range(flight_dist // self.plane_speed):
            time.sleep(1)
        self.place = arrival_airport
        print(self.plane_name + " arrived to " + self.place + " at " + dtn.now().strftime('%H:%M:%S'))

    def __repr__(self):
        return self.plane_name

Commander = Commander() #Создание объекта диспетчера 

MIA = data_handling.add_port("Miami", "MIA", "200", "100", "25.795911, -80.287062")

data_a = data_handling.read_port()
IST = Airport(data_a[0][0], data_a[0][1], data_a[0][2], data_a[0][3], data_a[0][4])  # Стамбул
KBP = Airport(data_a[1][0], data_a[1][1], data_a[1][2], data_a[1][3], data_a[1][4])  # Киев
MIA = Airport(data_a[2][0], data_a[2][1], data_a[2][2], data_a[2][3], data_a[2][4])  # Маями
ODS = Airport(data_a[3][0], data_a[3][1], data_a[3][2], data_a[3][3], data_a[3][4])  # Одесса

# B747 = data_handling.add_plane("Boieng 747", "100", "10000", "700", "Istanbul")

data_p = data_handling.read_planes()
AN_2 = Plane(data_p[0][0], data_p[0][1], data_p[0][2], data_p[0][3], data_p[0][4])  # AN-2
B737 = Plane(data_p[1][0], data_p[1][1], data_p[1][2], data_p[1][3], data_p[1][4])  # BOIENG 737
B747 = Plane(data_p[2][0], data_p[2][1], data_p[2][2], data_p[2][3], data_p[2][4])  # BOIENG 747

ODS.add_plane(B737)  # Добавить самолет в аеропорт
IST.add_plane(B747)  # Добавить самолет в аеропорт

F101 = Flight(101, ODS, IST, B737) # Создание рейса
Commander.add_flight(F101) # Добавление рейса в документ
Commander.start_flight(F101) # Запуск рейса
Commander.remove_flight(F101, 'End_f') # Удаление рейса из документа

# F102 = Flight(102, IST, MIA, B747) # Создание рейса
# F102.add_flight() # Добавление рейса в документ
# F102.start_flight() # Запуск рейса


