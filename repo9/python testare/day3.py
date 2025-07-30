"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def salut(self):
        print("Hello, my name is " + self.name)

    def met(self):
        if self.age >= 18:
            print("Sunt major")
        else:
            print("Sunt minor")

    def mod(self,age):
        self.age = age


ana=Student("Ana", 18)
maria=Student("Maria", 17)
david=Student("David", 134)
david.salut()
david.met()
david.mod(15)
david.met()
"""
#ex2

"""
class Carte:
    def __init__(self,titlu,autor,an_aparitie):
        self.titlu = titlu
        self.autor = autor
        self.an_aparitie = an_aparitie

    def descriere(self):
        print("detaliile despre carte sunt : ")
        print(self.titlu)
        print(self.autor)
        print(self.an_aparitie)

class Biblioteca(Carte):
    def __init__(self,list):
        self.list = list

    def adaugare(self,carte):
        self.list.append(carte)

    def listare(self):
        print("Cartile din biblioteca sunt :")
        i=0
        for x in self.list:

            print(list[i].descriere())
            i=i+1

    def cautare(self,carte):
        if carte in list:
            print("Exista cartea ")
            print(carte.titlu)

    def __eq__(self, other):
        return self.titlu == other.titlu and self.autor == other.autor


carte1=Carte("titlu1","autor1",2010)
carte2=Carte("titlu2","autor2",2016)
carte3=Carte("titlu3","autor3",2017)
carte4=Carte("titlu4","autor4",2018)
carte6=Carte("titlu5","autor5",2019)

carte2.descriere()
carte3.descriere()

list=[carte1,carte2,carte3,carte4]

biblioteca1=Biblioteca(list)
biblioteca1.listare()

biblioteca1.cautare(carte1)

biblioteca1.adaugare(carte6)
biblioteca1.listare()

print(carte2==carte2)
"""
"""
#ex3

class Animal:
    def __init__(self, nume,varsta, rasa):
        self.nume = nume
        self.__varsta = varsta
        self.rasa = rasa
    def sunet(self):
        pass
    def getvarsta(self):
        return self.__varsta

    def setvarsta(self,varsta):
        self.__varsta = varsta


class caine(Animal):
    def __init__(self, nume, varsta, rasa):
        super().__init__(nume, varsta, rasa)


    def sunet(self):
        print("Cainele face ham")



class pisica(Animal):
    def __init__(self, nume, varsta, rasa):
        super().__init__(nume, varsta, rasa)
        
    def sunet(self):
        print("Pisica face miau")




caine1=caine("max",2,"caucazian")
caine2=caine("hugo",3,"husky")
pisica1=pisica("misha",3,"toberonez")
pisica2=pisica("david",1,"just a little boy")

list=[caine1,caine2,pisica1,pisica2]

for x in list:
    x.sunet()

v=caine1.getvarsta()
print(v)

caine2.setvarsta(22)
v=caine2.getvarsta()
print(v)

"""

#3

"""
class Motor:
    def __init__(self,namem,agem):
        self.namem = namem
        self.agem = agem


class Masina(Motor):
    def __init__(self,marca,agemas,namem,agem):
        super().__init__(namem,agem)
        self.marca = marca
        self.agemas = agemas
        self.stare=True

    def porneste(self):
        stare=True
        print("Masina se porneste")

    def opreste(self):
        stare=False
        print("Masina se opreste")

    def __str__(self):
        return f"{self.marca}({self.agemas})({self.namem})({self.agem})"

    

masina1=Masina("Marca1",2,"motor1","12")

print(str(masina1))


"""
"""
class Forma:
    def __init__(self,culoare):
        self.culoare = culoare


    def arie(self):
        pass

class dreptunghi (Forma):
    def __init__(self,culoare,lmic,lmare):
        super().__init__(culoare)
        self.lmic = lmic
        self.lmare = lmare

    def arie(self):
        return self.lmic*self.lmare

class Cerc(Forma):
    def __init__(self,culoare,raza):
        super().__init__(culoare)
        self.raza = raza

    def arie(self):
          return self.raza*3.14


drept= dreptunghi("rosu",12 ,10)
a1=drept.arie()
print(a1)
cer=Cerc("negru",10)
a2=cer.arie()
print(a2)

"""

class Cont:
    def __init__(self,nume,id):
        self.nume= nume
        self.id = id

class ContEconomii(Cont):
    def __init__(self,nume,id):
        super().__init__(nume,id)
        self.sold=0
    def depunere(self,suma):
            self.sold=self.sold+suma

    def retragere(self,suma):
        if 0<suma<self.sold:
            self.sold=self.sold-suma

    def sold(self):
        return self.sold


class ContulCurent(Cont):
    def __init__(self,nume,id):
        super().__init__(nume,id)
        self.sold=0
    def depunere(self,suma):
        self.sold=self.sold+suma
    def retragere(self,suma):
        if 0<suma<self.sold:
            self.sold=self.sold-suma

    def sold(self):
        return self.sold


cont3=ContEconomii("flavius",1243251)
cont2=ContulCurent("david",1231231)
print(cont2.sold)
print(cont3.sold)