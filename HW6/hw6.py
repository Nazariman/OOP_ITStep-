'''
Завдання 1
Створіть клас Passenger з атрибутами
 name – ім’я
 destination – місце, куди прямує

Завдання 2
Створіть клас Transport з атрибутами
 speed – швидкість
Методи
 move(destination, distance) – рухається до місця
призначення, виводить інформацію як довго їхали

Завдання 3
Створіть клас Bus з атрибутами
 passengers – список пасажирів(об’єкти класу Passenger)
 capacity – максимальна можлива кількість пасажирів
Методи
 board_passenger(passenger) – якщо є місце, додає
пасажира
 move(destination, distance) – висаджує всіх пасажирів, які
хочуть вийти в даному місці(виводить їхню загальну
кількість) та викликає батьківський метод move()
'''

class Passenger(): 
    def __init__ (self, name, destination): 
        self.name = name
        self.destination = destination
    
class Transport(): 
    def __init__ (self, speed): 
        self.speed = speed
    
    def move(self, destination, distance):
        time = distance / self.speed
        print(f"Транспорт рухається до {destination}. Час у дорозі: {time:.2f} год.")
        
class Bus(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed)
        self.capacity = capacity
        self.passengers = []
        
    def board_passenger(self, passenger): 
        if len(self.passengers) < self.capacity: 
            self.passengers.append(passenger)
            print(f"Пасажир {passenger.name} сів у автобус і їде до {passenger.destination}.")
        else:
            print("Автобус заповнений! Пасажир не може сісти.") 
    
    def move(self, destination, distance):
        exiting_passengers = [p for p in self.passengers if p.destination == destination]
        self.passengers = [p for p in self.passengers if p.destination != destination]
        
        print(f"Автобус прибув у {destination}. Вийшло {len(exiting_passengers)} пасажирів.")
        super().move(destination, distance)
        
 