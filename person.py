from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job = None, pay = 0): #конструктор
        self.name = name #заполнение атрибутов
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent)) #управление состоянием объекта

    #def __str__(self): #будет унаследован от AttrDisplay
    #    return '[Person: %s, %s]' %(self.name, self.pay) #метод автоматически вызвается при print() и str()

class Manager(Person): #наследование
    def __init__(self, name, pay): #конструктов дочернего класса
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus = 0.1): #переопределние метода (уточнение работы унаследованного метода)
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__': #при тестировании
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', 'dev', 100)

    print(bob)
    print(sue)
    print(bob.name.split())
    sue.pay *= 1.1
    print(sue.pay)
    print('----------')
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(0.2)
    print(sue)
    print('----------')
    tom = Manager('Tom Jones', 200)
    tom.giveRaise(0.1)
    print(tom)
    print('--All three--')
    for object in (bob,sue,tom):
        object.giveRaise(0.1)
        print(object)
