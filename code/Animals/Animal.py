class Animal: 
    'represents a generic animal'

    def setSpecies(self, specs):
        'set the species of the animal'
        self.species = specs
    def setLanguage(self, lang):
        'set the language of the animal'
        self.language = lang
    def speak(self):
        'prints a sentence by the animal'
        print('I am a ' + self.species + ' and I speak ' + self.language)
    def getSpecies(self):
        'returns the species of the animal'
        return self.species