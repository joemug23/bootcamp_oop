
class Person(object):

    def __init__(self, names, age, salary):
        self.names = names
        self.age = age
        # a private variable that ca not be accessed outside of the class
        self.__salary = salary

    def set_names(self, names):
        self.names = names
        print(str(self.names)+'  ')
    
    def lived(self):
        days_lived = self.age * 365
        print(str(days_lived)+'  ')

class Player(Person):
    # inherit from person
    def __init__(self, sport):
        self.sport = sport
    
    def set_salary(self):
        self._Person__salary = "120M"
        print(self._Person__salary)
    
player = Player("Football")
player.set_names("Messi Leo")
# player.salary = 234
player.set_salary()
player.age = 29
player.lived()
print(player.sport)