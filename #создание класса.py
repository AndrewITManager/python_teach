#создание класса
class Car:#имя класса
    def move(self):#метод, self - это указание на определенны экземляр класса Car
        print("Car is moving")

    def stop(self):
        print("Car stopped")

my_car = Car()

print(type(my_car))
print(isinstance(my_car, Car))

my_car.move()#вызов методов класса Car
my_car.stop()#вызов методов класса Car