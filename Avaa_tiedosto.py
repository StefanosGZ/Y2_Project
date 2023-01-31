import csv
import sys

from Meno import meno

#Avaa tiedoston ja luo meno olioita
class avaa:

    def __init__(self):
        self.kumulatiivinen_meno = 0
        self.kumulatiivinen_tulo = 0
        self.dictionary = {}
        self.yrityslista = []
        tiedosto=input("Minkä tiedoston haluat avata? (Nopeuttaminen: Kayttotili=1,Kokeilu=2, Rikki=3)\n")
        if tiedosto=="0":
            print("Yhtäkään tiedostoa ei avattu, joten ohjelma sulkeutuu")
            sys.exit()
        self.z=0

        #Kysyy, minkä tiedoston haluat avata
        while tiedosto!="0":
            try:
                if tiedosto=="1":
                    tiedosto="Kayttotili.csv"
                elif tiedosto=="2":
                    tiedosto="Kokeilu.csv"
                elif tiedosto=="3":
                    tiedosto="Rikki.csv"
                elif ".csv" not in tiedosto:
                    tiedosto=tiedosto+".csv"
                self.kokeile(tiedosto)
                tiedosto=input("Minkä tiedoston haluat avata? Jos et halua avata uutta tiedostoa anna 0\n")
            except:
                print("Tiedostoa ei ole")
                tiedosto=input("Minkä tiedoston haluat avata? Jos et halua avata uutta tiedostoa anna 0\n")
        if self.z==0:
            print("Yhtäkään tiedostoa ei avattu, joten ohjelma sulkeutuu")
            sys.exit()
    def kokeile(self,tiedosto):
        # Itselleni hyödyllisiä if lauseita
        # tiedosto=input("Minkä tiedoston haluaisit avata? (.csv)\n")
        # tiedosto=tiedosto+".csv"
        # jakaja=input("Minkälainen jakaja on käytössä? (esim ,;:)\n")
        # Luodaan juttuja, joita käytetään myöhemmin
        # avataan tiedosto ja käydään läpi rivi kerrallaan
        with open(tiedosto) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=";")

            header = next(readCSV)
            try:
                Lapimeni=[]
                for testaus in readCSV:
                    maara=testaus[1]
                    maara=maara.replace(",",".")
                    maara=float(maara)
                    paikka=testaus[5]
                    Lapimeni.append(testaus)
                self.z=1
                for rivi in Lapimeni:
                    self.maara = rivi[1]
                    self.maara = self.maara.replace(",", ".")
                    self.maara = float(self.maara)
                    # Käytän integeriä, koska helpompi käsitellä eikä tule floatin minimaalisia virheitä.
                    # Kun määrät näytetään jaetaan ne sadalla
                    self.maara = int(self.maara * 100)
                    self.paikka = rivi[5]
                    self.testaukset()
                    self.tutki()
            except:
                print("Rivissä {} on virhe.".format(testaus))
                print("Jos haluat avata kyseisen tiedoston korjaa edellä esitetty rivi")
                print("")
                print("Huomioi, että tiedosto pitää olla muotoa:\nKirjauspäivä;Määrä;Maksaja;Maksunsaaja;Nimi;Otsikko;Viitenumero;Valuutta")
                print("Näistä pakolliset ovat Määrä indeksissä 1 sekä paikka indeksissä 5")
                print("")
    # tutkitaan, onko meno vai tulo
    def tutki(self):
        if self.maara < 0:
            self.kumulatiivinen_meno += self.maara
            self.lisaa_meno()
        else:
            self.kumulatiivinen_tulo += self.maara

#Tässä on tärkeys tekoäly.
#Luo uuden meno olion tai lisää menoja ja tärkeyttä vanhaan.
    def lisaa_meno(self):
        if self.paikka not in self.yrityslista:
            self.yrityslista.append(self.paikka)
            if self.paikka=="Bussilippu":
                self.tarkeys=20
            elif self.paikka=="Vuokra":
                self.tarkeys=20
            elif self.maara<=-20000:
                self.tarkeys=20
            elif self.maara<=-15000:
                self.tarkeys=15
            elif self.maara<=-10000:
                self.tarkeys=10
            elif self.maara<=-5000:
                self.tarkeys=5
            else:
                self.tarkeys=1
            self.meno_olio = meno(self.maara, self.paikka,self.tarkeys)
            self.dictionary.update({self.paikka: self.meno_olio})

        else:
            self.dictionary[self.paikka].add_maara(self.maara)
            if self.maara<=-20000:
                self.dictionary[self.paikka].muuta_tarkeys(20)
            elif self.maara<=-15000:
                if int(meno.get_tarkeys(self.dictionary[self.paikka]))<15:
                    self.dictionary[self.paikka].muuta_tarkeys(15)
                else:
                    self.dictionary[self.paikka].add_tarkeys
            elif self.maara<=-10000:
                if int(meno.get_tarkeys(self.dictionary[self.paikka]))<10:
                    self.dictionary[self.paikka].muuta_tarkeys(10)
                else:
                    self.dictionary[self.paikka].add_tarkeys
            elif self.maara<=-5000:
                if int(meno.get_tarkeys(self.dictionary[self.paikka]))<5:
                    self.dictionary[self.paikka].muuta_tarkeys(5)
                else:
                    self.dictionary[self.paikka].add_tarkeys
            else:
                meno.add_tarkeys(self.dictionary[self.paikka])

#Itselleni hyödyllisiä paikan nimen muutoksia
    def testaukset(self):
        if "VFI*" in self.paikka:
            self.paikka = self.paikka.replace("VFI*", "")

        if "Burger King" in self.paikka or "CANDY TEAM" in self.paikka or "Pizza Hut" in self.paikka or "ESPRESSO HOUSE" in self.paikka:
            self.paikka = self.paikka.split(" ")
            self.paikka = self.paikka[0] + " " + self.paikka[1]

        elif "MOB.PAY*HELSINGIN" in self.paikka:
            self.paikka = "Bussilippu"

        elif "MOB.PAY*COMPASS" in self.paikka or "Teknologforeningen" in self.paikka:
            self.paikka = "Kouluruoka"

        elif "WOLT" in self.paikka:
            self.paikka = "Wolt"

        elif "MCD" in self.paikka:
            self.paikka = "McDonalds"

        elif "Teboil" in self.paikka:
            self.paikka = "Teboil"

        elif "barber" in self.paikka or "Barber" in self.paikka or "Parturi" in self.paikka or "parturi" in self.paikka:
            self.paikka = "Parturi"
        elif "PAYPAL" in self.paikka:
            self.paikka = "Hotelli"

        elif "ALEPA" in self.paikka or "Alepa" in self.paikka:
            self.paikka = "Alepa"


        elif " " in self.paikka:
            self.paikka = self.paikka.split(" ")
            self.paikka = self.paikka[0]

        if "K-Market" in self.paikka or "k-market" in self.paikka or "K-market" in self.paikka:
            self.paikka = "K-Market"

#Luo kolmiulotteisen listan menosta,nimestä sekä tärkeydestä
    def kaksulotteinen(self):
        self.tyhjalista = []
        self.kaksiulotteinenlista = []
        for yritys in self.yrityslista:
            maara = meno.get_maara(self.dictionary[yritys])
            tarkeys = meno.get_tarkeys(self.dictionary[yritys])
            self.tyhjalista.append(maara)
            self.tyhjalista.append(yritys)
            self.tyhjalista.append(tarkeys)
            self.kaksiulotteinenlista.append(self.tyhjalista)
            self.tyhjalista = []

#Sama kuin aikaisempi
    def kaksulotteinen2(self):
        self.tyhjalista = []
        self.kaksiulotteinenlista = []
        for yritys in self.yrityslista:
            maara = meno.get_maara(self.dictionary[yritys])
            tarkeys = meno.get_tarkeys(self.dictionary[yritys])
            self.tyhjalista.append(maara)
            self.tyhjalista.append(yritys)
            self.tyhjalista.append(tarkeys)
            self.kaksiulotteinenlista.append(self.tyhjalista)
            self.tyhjalista = []

#Lisää menon, joko luo uuden tai lisää vanhaan
    def lisaa_uusi_meno(self, maara, paikka,tarkeys):
        self.paikka = paikka
        self.maara = maara
        self.tarkeys=tarkeys
        self.lisaa_meno()

    def get_kumulatiivinen_tulo(self):
        return self.kumulatiivinen_tulo

    def get_kumulatiivinen_meno(self):
        return self.kumulatiivinen_meno

    def get_yrityslista(self):
        return self.yrityslista

    def get_kaksulotteinenlista(self):
        return self.kaksiulotteinenlista

    def get_dictionary(self):
        return self.dictionary

    def muuta_tarkeys(self,yritys,tarkeys):
        self.dictionary[yritys].muuta_tarkeys(tarkeys)
    def nollaa(self,yks):
        meno.nollaa(self.dictionary[yks[1]])

    def muuta(self,yks,maara):
        meno.muuta(self.dictionary[yks[1]],maara)