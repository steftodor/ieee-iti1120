from Animal import Animal
from Bird import Bird
from Dog import Dog

squirrel = Animal()
squirrel.setSpecies('Flying squirrel')
squirrel.setLanguage('Squeak')
print(squirrel.getSpecies())
squirrel.speak()

parrot = Bird()
parrot.setSpecies('Parrot')
parrot.setLanguage('Squawk')
print(parrot.getSpecies())
parrot.speak()

dog = Dog()
dog.setSpecies('Dog')
dog.setLanguage('Woof')
print(dog.getSpecies())
dog.speak()

