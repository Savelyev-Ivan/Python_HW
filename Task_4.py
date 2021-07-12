#Реализуйте базовый класс Car.
#у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def police(self):
        if self.is_police:
            return 'Полицейская машина'
        else:
            return 'Гражданская машина'

    def full_info(self):
        return " {} {} Cкорость {} км/ч ".format(self.color, self.name, str(self.speed))

    def go(self):
        return "Машина поехала"

    def stop(self):
        return"Машина остановилась"

    def turn(self):
        return"Машина повернула"

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        return f' {self.name}: Скорость автомобиля {self.speed}  км/ч. Превышение скорости!' \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        return f' {self.name}: Скорость автомобиля {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f" {self.name}: Скорость автомобиля {self.speed} км/ч"

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


t_c = TownCar(160, "Black", "Vesta", False)
print(t_c.police() + t_c.full_info() + t_c.turn() + t_c.show_speed())

s_c = SportCar(250, "Red", "Audi", False)
print(s_c.police() + s_c.full_info() + s_c.go())

w_c = WorkCar(50, "Brown", "UAZ", False)
print(w_c.police() + w_c.full_info() + w_c.stop() +w_c.show_speed())

p_c = PoliceCar(400, "White", "Bugatti", True)
print(p_c.police() + p_c.full_info() + p_c.go())