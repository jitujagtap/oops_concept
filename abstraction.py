from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def tyres(self):
        pass

    @abstractmethod
    def assemble(self):
        pass

class Bmw(Vehicle):
    def engine(self):
        print("Manufacture enginer")

class Mrf(Vehicle):
    def tyres(self):
        print("Manufacture Tyres")

class Tata(Vehicle):
    def engine(self):
        print("Use engine manufactured by BMW")

    def tyres(self):
        print("use tyres manufactured by MRF")

    def assemble(self):
        print("Assemble the car")

    def ev(self):
        print("Manufacture Electronic Vehicle")

t = Tata()
t.tyres()
t.engine()
t.ev()
t.assemble()

class Audi(Tata):
    def engine(self):
        print("Use Tata engine")

    def assemble(self):
        print("Assemble the car")

    def tyres(self):
        print("Use Tyres of Bridgestone")

A = Audi()
A.tyres()

