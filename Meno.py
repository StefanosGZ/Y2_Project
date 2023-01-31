#Luo meno olion
class meno:
    def __init__(self, maara, paikka,tarkeys):
        self.maara=maara
        self.paikka=paikka
        self.tarkeys=tarkeys

    def get_maara(self):
        return self.maara

    def get_paikka(self):
        return self.paikka

    def get_tarkeys(self):
        return self.tarkeys

#Lisää olion menon määrää
    def add_maara(self,maara):
        self.maara+=maara
        if self.maara>20:
            self.maara=20

#Lisää tärkeyttä per kerta
    def add_tarkeys(self):
        self.tarkeys+=1

#Muuttaa tärkeyttä
    def muuta_tarkeys(self,tarkeys):
        if tarkeys<20:
            self.tarkeys=tarkeys
        elif tarkeys<=0:
            self.tarkeys=1
        else:
            self.tarkeys=20

    def nollaa(self):
        self.maara=0
        self.tarkeys=0

    def muuta(self,maara):
        self.maara=maara