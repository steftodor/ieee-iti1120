from Animal import Animal
class Bird(Animal):
    
    def speak(self):
        print('{}!'.format(self.language)*3)