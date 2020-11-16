import os
from math import sin, cos, radians, acos

# расчет расстояния между аэропортами
def calc_dist_fixed(city_a, city_b): # Координати в десяткових градусах з сайту https://dateandtime.info/uk/citycoordinates.php?id=703448
    """all angles in degrees"""
    EARTH_RADIUS_IN_MILES = 3958.761 
    lat_a, long_a = float(city_a[0]), float(city_a[1])
    lat_b, long_b = float(city_b[0]), float(city_b[1])
    lat_a = radians(lat_a)
    lat_b = radians(lat_b)
    delta_long = radians(long_a - long_b)
    cos_x = (
        sin(lat_a) * sin(lat_b) +
        cos(lat_a) * cos(lat_b) * cos(delta_long)
        )
    return acos(cos_x) * EARTH_RADIUS_IN_MILES / 0.62137 #km = mi/0.62137

# чтение данных про аэропорты
def read_all_ports(folder = 'ports'):
    port = []
    port_files = os.listdir(folder)#открываем папку с файлами аэропортов
    for one_port in port_files: #читаем по одному файлу в папке и загоняем данные с файлов в список self.port = []
        file_name = os.path.join(folder, one_port)
        port.append(read_port(file_name))
    return port
        
# чтение данных про отдельный аэропорт
def read_port(file_name):
    f = open(file_name, 'r')
    t = f.readlines()
    f.close()
    
    port_dict = {} #словарь данных одного аэропорта
    for i in t:#читаем файл построчно и передаем данные в словарь. 
               #В каждой строке файла только два элемента: ключ и значение. Напр. (name: Борисполь), (code: UKBB) ....
        if ':' in i:
            s = i.split(':')
            port_dict[s[0]] = s[1].strip()
    #двойные скобки - список в списке. Список аэропортов, каждый аэропорт - вложенный список ((..,..,..), (..,..,..))
    return port_dict['name'], port_dict['code'], int(port_dict['polosa']), int(port_dict['capacity']), port_dict['coordinates']

# запись в файл нового аэропорта
def add_port(airport_name, code, lane_width, planes_capacity, coordinates):
    folder = 'ports'
    f2 = open(folder + '/' + airport_name + '.txt', 'w')
    f2.write('name: ' + airport_name + '\n' +
            'code: ' + code + '\n' +
            'polosa: ' + str(lane_width) + '\n' +
            'capacity: ' + str(planes_capacity) + '\n' +
            'coordinates: ' + coordinates )
    f2.close()


def del_airport(name):
    data_a = data_handling.read_port()
    n = Airport(data_a[1][0], data_a[1][1], data_a[1][2], data_a[1][3], data_a[1][4]) # Порт № 1
    n2 = Airport(data_a[2][0], data_a[2][1], data_a[2][2], data_a[2][3], data_a[2][4]) # Порт № 2


# удаление файла
def del_file(folder, name):
    os.listdir(folder)#открываем папку с файлами 
    os.remove(folder + '/' + name + '.txt')

# IO PLANES  чтение данных про аэропорты
def read_planes(folder = 'planes'):
    planes = []
    plane_files = os.listdir(folder)
    for one_plane in plane_files: 
        f = open(os.path.join(folder, one_plane), 'r')
        t = f.readlines()
        f.close()
        plane_dict = {} 
        for i in t:
            if ':' in i:
                s = i.split(':')
                plane_dict[s[0]] = s[1].strip()
            # print(plane_dict)
        planes.append((plane_dict['name'], int(plane_dict['width']), int(plane_dict['dist']), int(plane_dict['speed']), plane_dict['place']))
    return planes

# новый файл самолет
def add_plane(plane_name, plane_width, plane_dist, plane_speed, place):
    folder = 'planes'
    f2 = open(folder + '/' + plane_name + '.txt', 'w')
    f2.write('name: ' + plane_name + '\n' +
            'width: ' + plane_width + '\n' +
            'dist: ' + plane_dist + '\n' +
            'speed: ' + plane_speed + '\n' +
            'place: ' + place )
    f2.close()
