    ## Skriv ner vad du tror kommer skrivas ut.
    ## Skriv sedan in koden i din IDE, exakt som den står, och kör den.
    ## Fick du samma resultat som du trodde? Om inte, varför?

    ##Anakonda och Boaorm sparas i SafeStorage.
    ## Sedan hämtas Anakonda till variabeln x och Boaorm hämtas till variabeln y.
    ## Print - "Anakonda", "Boaorm"

class SafeStorage:
    __data = None
    def get(self):
        return self.__data
    def put(self, data):
        self.__data = data

safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()
safe.put("Boaorm")
y = safe.get()
#print(x, y)


    ## 2a. Vad gör följande kod? Fixa eventuella fel.
    ## Koden skriver ut ett djurläte på det djur som anropas. Om det inte finns ett ljud så skickas
    ## Felaktig indent på rad 43. Ändrade shelf till self på rad 46. Ändrade alla print till return.
    ## La till __init__ och __str__ för att kunna skicka med en kommentar.
    ## La till en klass för rooster och lade till super().make_noise() eftersom jag inte har ljudet tillgängligt.
    ## 2b. La till en klass för parrot och lade till super().make_noise() eftersom jag inte har ljudet tillgängligt.

class Animal:
    def make_noise(self):
        return "No sound available for this animal."

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}: {self.make_noise()}"

class Dog(Animal):
    def make_noise(self):
         return "Voff!"

class Cat(Animal):
    def make_noise(self):
        return "Mjau!"

class Rooster(Animal):
    def make_noise(self):
        super().make_noise()
        return super().make_noise()

class Parrot(Animal):
    def make_noise(self):
        return super().make_noise()

def sound_of(animal):
    return f"{animal}"

c = Cat("Cat")
d = Dog("Dog")
h = Rooster("Rooster")
p = Parrot("Parrot")

foo = [c, d, h, p]

for animal_sound in foo:
    print(f"{sound_of(animal_sound)}")

