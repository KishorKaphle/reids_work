
class Robot:
    def __init__ (self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print('My name is ' + self.name)

r = Robot('Tom', 'Brown', '40')
r.introduce_self()

