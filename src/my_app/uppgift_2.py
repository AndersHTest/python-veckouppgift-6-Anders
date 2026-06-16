    ## 1a, b, c, d.
    ## På Island bor det 383726 invånare och i Danmark 5961249.
    ## Skapa objekt för länderna. (Data från januari 2024. Avrunda befolkningen.)


class Country:
    def __init__(self, name, pop, area=None, lang=None):
        self.name = name
        self.population = pop
        self.area = area
        self.lang = lang


    def __str__(self):
        return f"Country: {self.name}\nPopulation: {self.population}"


    def add_language(self):
        if self.lang is not None:
            return f"Här pratar man {self.lang}."
        else:
            return ""


    def print_info(self):
        name = self.name
        pop = self.population
        area = self.area
        lang = self.lang
        if self.area is None:
            return f"\nI {name} bor det {pop} miljoner invånare.\nDet officiella språket är {self.lang}."
        else:
            return f"\nI {name} bor det {pop} miljoner invånare och arean är {self.area} km².\nDe(t) officiella språke(n/t) är {self.lang}."


lang_se = ["Svenska"]
lang_no = ["Norska"]
lang_fi = ["Finska", "Svenska"]
lang_ch = ["Rätoromanska", "Tyska", "Franska", "Italienska"]

se = Country("Sverige", 10.5, None, lang_se)
no = Country("Norge", 5.5, 33, lang_no)
fi = Country("Finland", 10.5, 303890, lang_fi)
ch = Country("Schweiz", 20, 3000, lang_ch)

print(se.print_info())
print(fi.print_info())
print(no.print_info())
print(ch.print_info())

print(se)