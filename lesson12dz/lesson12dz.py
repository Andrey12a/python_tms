class Moving:
    def move(self):
        raise NotImplementedError


class Animal(Moving):
    def voice(self):
        raise NotImplementedError


class Transport(Moving):
    def launch(self):
        raise NotImplementedError


class Duck(Animal):
    def voice(self):
        print('krykry')

    def move(self):
        print('duck swims')


class Tiger(Animal):
    def voice(self):
        print("rrrrr")

    def move(self):
        print('tiger is running')


class Car(Transport):
    def __init__(self):
        self.started = 'car is started'
        self.silenced = 'car is not started'

    def launch(self):
        print(f'Status car: {self.started}')

    def move(self):
        if self.silenced:
            print("car doesn't go")
        else:
            print('car is driving')
