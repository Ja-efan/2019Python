# 07092019
# 10-02 p.360

class Person(object):
    def __init__(self, name):
        self.name = name

    def language(self):
        pass

class Earthling(Person):
    def language(self,language):
        return language

class Groot(Person):
    def language(self, language):
        return "I'm Groot!"

name = ["Gachon","Dr.strange","Groot"]
country = ["Korea","USA","Galaxy"]
language = ["Korean","English","Groot"]

for idx, name in enumerate(name):
    if country[idx].upper() != "GALAXY":
        person = Earthling(name)
        print(person.language(language[idx]))

    else:
        groot = Groot(name)
        print(groot.language(language[idx]))
