#создание класса
class Car:#имя класса
    def move(self):#метод, self - это указание на определенны экземляр класса Car
        print("Car is moving")

    def stop(self):#метод, класса Car
        print("Car stopped")

my_car = Car()#создание экземляра класса Car

# print(type(my_car))
# print(isinstance(my_car, Car))
# print(isinstance(my_car, object))
# print(dir(my_car))
# print(my_car.__dict__)


my_car.move()#вызов методов класса Car
my_car.stop()#вызов методов класса Car

my_second_car = Car()
print(my_car == my_second_car)#два независимых объекта
print(id(my_car), id(my_second_car))

Car.move(my_car)
