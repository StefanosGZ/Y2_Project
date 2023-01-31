from PyQt5 import QtWidgets
import sys
from PyQt5 import QtGui
from Meno import meno
from PyQt5 import QtCore
from PyQt5.Qt import QColor
from Avaa_tiedosto import avaa
#moi
#Luo säästä ikkunan, jossa voit valita kuinka paljon haluat säästää rahaa
class Saasta(QtWidgets.QMainWindow):
    def __init__(self):
        super(Saasta,self).__init__()
        self.setWindowTitle("Säästä")
        self.setGeometry(700,400,500,250)
        self.setStyleSheet("background:#8dba92")
        self.nappi_ja_teksti()

#Luo napin ja tekstin, liittyen säästöön
    def nappi_ja_teksti(self):
        self.teksti=QtWidgets.QLineEdit(self)
        self.teksti.setPlaceholderText("Paljonko haluat säästää?")
        self.teksti.move(100,70)
        self.teksti.resize(300,50)
        self.teksti.setStyleSheet("font color:black")
        m = self.teksti.font()
        m.setPointSize(14)
        self.teksti.setFont(m)

        self.saasto_nappi = QtWidgets.QPushButton("Säästä!", self)
        self.saasto_nappi.move(100, 130)
        self.saasto_nappi.resize(300, 50)
        self.saasto_nappi.setStyleSheet("background-color: seagreen; font-size:12pt;font-weight: bold;color:oldlace")

#Luo tärkeydet ikkunan, jossa voit muuttaa menojen tärkeyksiä monta kerrallaan tai yksitellen.
class Tarkeydet(QtWidgets.QMainWindow):
    def __init__(self):
        super(Tarkeydet, self).__init__()

        self.setWindowTitle("Muuta tärkeyttä")
        self.setGeometry(700,100,500,400)
        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)
        self.lay = QtWidgets.QVBoxLayout(self.centralwidget)
        self.varmistin=0
        self.teksti=QtWidgets.QLineEdit(self)
        self.teksti.setPlaceholderText("Anna tärkeyden arvo (max 20)")

        self.pybutton = QtWidgets.QPushButton('Muuta tärkeys', self)
        self.pybutton.setStyleSheet("background-color: #b38a4b; font-size:12pt;font-weight: bold;color:oldlace")

        self.valmisnappi = QtWidgets.QPushButton('Valmis', self)
        self.valmisnappi.setStyleSheet("background-color: black; font-size:12pt;font-weight: bold;color:oldlace")

        self.lay.addWidget(self.valmisnappi)
        self.lay.addStretch(-1)

        self.lay.addWidget(self.teksti)
        self.lay.addStretch(-1)


        self.lay.addWidget(self.pybutton)
        self.lay.addStretch(-1)


        self.pybutton.clicked.connect(self.take_and_add)

#Luo nappulat ikkunaan listasta
    def nappulat(self,kaksulotteinen):
        #Poistaa nappulat, jotta uudet voidaan tehdä.
        if self.varmistin!=0:
            for olio in self.nappulaoliot:
                self.lay.removeWidget(olio)


        yritykset=[]
        maarat=[]
        tarkeydet=[]
        kaksulotteinen = sorted(kaksulotteinen, key=lambda x: (-x[2], x[0]))

        for kaks in kaksulotteinen:
            yritykset.append(kaks[1])
            maarat.append(kaks[0])
            tarkeydet.append(kaks[2])

#Luo nappulat listasta
        self.i=0
        self.tyhjalista=[]
        self.nappulaoliot=[]
        self.nappidict={}
        self.loppulista=[]
        while self.i<len(yritykset):
            self.btn = QtWidgets.QPushButton('{}: Tärkeys {}'.format(yritykset[self.i],tarkeydet[self.i]), self)
            text = self.btn.text()
            self.btn.setStyleSheet("background-color:#e6b873; font-weight:bold")
            lisää = {yritykset[self.i]: self.btn}
            self.nappulaoliot.append(self.btn)
            self.nappidict.update(lisää)
            self.btn.clicked.connect(lambda ch, text=text: self.hide_button(text))
            self.lay.addWidget(self.btn)
            self.i+=1

        self.varmistin=1

#Ottaa tekstin, teksti kentästä
    def take_and_add(self):
        if self.teksti.text().isnumeric():
            pyorista=int(self.teksti.text())
            teksti = [pyorista]
            if teksti != ""  and self.tyhjalista != []:
                self.tyhjalista = teksti + self.tyhjalista
                self.loppulista.append(self.tyhjalista)
            self.tyhjalista = []
            self.teksti.clear()

#Tekee painetusta nappulasta ei painettavan
    def hide_button(self, text):
        text=text.split(":")
        text=text[0]
        nappi = self.nappidict[text]
        nappi.setEnabled(False)
        self.tyhjalista.append(text)

#Luo muut ikkunan, joka näyttää kaikki menot, jotka eivät mahdu top10
class Muut(QtWidgets.QMainWindow):
    def __init__(self):
        super(Muut, self).__init__()
        self.setWindowTitle("Muut")
        self.setGeometry(700,350,500,400)
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setBackgroundBrush(QColor("#bab3e3"))
        self.graphicview = QtWidgets.QGraphicsView(self.scene, self)

        self.graphicview.setGeometry(0, 0, 500, 400)

#Luo tekstit muut ikkunaan
    def luo_tekstit(self,muutmaara,muutpaikka,menot,muutmenot):
        self.scene.clear()
        q = 0
        muutmenot = muutmenot / 100
        self.laske = 0


        while q < len(muutpaikka):
            maara = -muutmaara[q] / 100
            self.muutprosentti = round((maara / muutmenot) * 100)
            self.kokoprosentti = -round((maara / menot) * 100)
            self.muutteksti = QtWidgets.QGraphicsTextItem(
                "{} {:.2f}€ ({}%)".format(muutpaikka[q], maara, self.kokoprosentti))
            self.muutteksti.setPos(-400, -400 + self.laske)
            self.muutteksti.setScale(1.3)
            self.scene.addItem(self.muutteksti)
            self.laske += 25
            q += 1



#Päivittää tekstit
    def paivita(self,maara,paikka):
        self.muutprosentti=round((maara/self.muutmenot)*100)
        self.kokoprosentti=round((maara/self.kokoprosentti)*100)
        self.muutteksti = QtWidgets.QGraphicsTextItem("{} {:.2f}€ {}% ({}%)".format(paikka, maara, self.muutprosentti, self.kokoprosentti))
        self.muutteksti.setPos(-400, -400 + self.laske)
        self.muutteksti.setScale(1.3)
        self.scene.addItem(self.muutteksti)
        self.laske += 25

#Luo jaottelu ikkunan, jossa voi yhdistää menoja iE. Alepa, Lidl, K-market => Ruokakaupat.
#Pystyy myös vaihtaa yksittäisen kaupan nimen.
class Jaottelu(QtWidgets.QMainWindow):
    def __init__(self):
        super(Jaottelu, self).__init__()

        self.setWindowTitle("Lisää ryhmittely")
        self.setGeometry(700,100,500,400)
        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)
        self.lay = QtWidgets.QVBoxLayout(self.centralwidget)
        self.varmistin=0
        self.teksti=QtWidgets.QLineEdit(self)
        self.teksti.setPlaceholderText("Lisää ryhmittelyn nimi")

        self.pybutton = QtWidgets.QPushButton('Lisää ryhmittely', self)
        self.pybutton.setStyleSheet("background-color: peru; font-size:12pt;font-weight: bold;color:oldlace")

        self.valmisnappi = QtWidgets.QPushButton('Valmis', self)
        self.valmisnappi.setStyleSheet("background-color: black; font-size:12pt;font-weight: bold;color:oldlace")

        self.lay.addWidget(self.valmisnappi)
        self.lay.addStretch(-1)

        self.lay.addWidget(self.teksti)
        self.lay.addStretch(-1)


        self.lay.addWidget(self.pybutton)
        self.lay.addStretch(-1)


        self.pybutton.clicked.connect(self.take_and_add)

#Luo nappulat listasta
    def nappulat(self,kaksulotteinen):
        #Poistaa nappulat
        if self.varmistin!=0:
            for olio in self.nappulaoliot:
                self.lay.removeWidget(olio)


        yritykset=[]
        maarat=[]

        for kaks in kaksulotteinen:
            yritykset.append(kaks[1])
            maarat.append(kaks[0])


        self.i=0
        self.tyhjalista=[]
        self.nappulaoliot=[]
        self.nappidict={}
        self.loppulista=[]
        while self.i<len(yritykset):
            self.btn = QtWidgets.QPushButton('{}'.format(yritykset[self.i]), self)
            text = self.btn.text()
            self.btn.setStyleSheet("background-color:#f5cca4; font-weight:bold")
            lisää = {yritykset[self.i]: self.btn}
            self.nappulaoliot.append(self.btn)
            self.nappidict.update(lisää)
            self.btn.clicked.connect(lambda ch, text=text: self.hide_button(text))
            self.lay.addWidget(self.btn)
            self.i+=1

        self.varmistin=1

#Ottaa tekstin tekstikentästä
    def take_and_add(self):
        teksti=[self.teksti.text()]
        if teksti!="" and self.tyhjalista!=[]:
            self.tyhjalista=teksti+self.tyhjalista
            self.loppulista.append(self.tyhjalista)
        self.tyhjalista=[]
        self.teksti.clear()

#Tekee painetusta nappulasta, ei painettavan
    def hide_button(self,text):
        nappi=self.nappidict[text]
        nappi.setEnabled(False)
        self.tyhjalista.append(text)

#Avaa tulo ikkunan, jossa voi lisätä tuloja
class Tulo(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Tulo, self).__init__(parent)
        self.setWindowTitle("Lisää tulo")
        self.setGeometry(700,400,500,250)
        self.setStyleSheet("background:#9bfaac")
        self.teksti1()
        self.Tulo_Nappi()

#Luo napin
    def Tulo_Nappi(self):
        self.Meno_nappi=QtWidgets.QPushButton("Lisää tulo",self)
        self.Meno_nappi.move(100,130)
        self.Meno_nappi.resize(300,50)
        self.Meno_nappi.setStyleSheet("background-color: seagreen; font-size:12pt;font-weight: bold;color:oldlace")

#Luo tekstikentän
    def teksti1(self):
        self.maara=QtWidgets.QLineEdit(self)
        self.maara.move(100,70)
        self.maara.resize(300,50)
        self.maara.setPlaceholderText("Lisää tulon määrä")
        m=self.maara.font()
        m.setPointSize(14)
        self.maara.setFont(m)

#Avaa meno ikkuan, jossa voi luoda uuden menon
class Meno(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Meno, self).__init__(parent)
        self.setWindowTitle("Lisää meno")
        self.setGeometry(700,450,500,300)
        self.setStyleSheet("background-color: #facf9b")
        self.Meno_Nappi()
        self.teksti1()

#Luo napin
    def Meno_Nappi(self):
        self.Meno_nappi=QtWidgets.QPushButton("Lisää meno",self)
        self.Meno_nappi.move(100,200)
        self.Meno_nappi.setStyleSheet("background-color: tomato; font-size:12pt;font-weight: bold;color:oldlace")
        self.Meno_nappi.resize(300,50)

#Luo tekstikentän
    def teksti1(self):
        self.maara=QtWidgets.QLineEdit(self)
        self.maara.move(100,125)
        self.maara.resize(300,50)
        self.maara.setPlaceholderText("Lisää menon määrä")
        m=self.maara.font()
        m.setPointSize(14)
        self.maara.setFont(m)




        self.paikka=QtWidgets.QLineEdit(self)
        self.paikka.move(100,50)
        self.paikka.resize(300,50)
        self.paikka.setPlaceholderText("Lisää yrityksen nimi")
        p=self.paikka.font()
        p.setPointSize(14)
        self.paikka.setFont(p)

#Luo pääikkunan
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.brush=""
        self.varmistin=False
        self.saastopaalla=False
        self.setWindowTitle("Testi")
        self.setGeometry(500,225,950,650)
        self.setStyleSheet("background-color:linen")
        self.teksti()
        self.avaa=avaa()
        self.Nappi()
        self.scene= QtWidgets.QGraphicsScene()
        self.kaksulotteinen2()
        self.top10()
        self.luo_vari()
        self.luo_piirakka_diagrammi()
        self.scene.setBackgroundBrush(QColor("white"))
        self.add_kokonaismeno_ja_tulo()


        self.tulo.Meno_nappi.clicked.connect(self.lisaa_tulo)
        self.meno.Meno_nappi.clicked.connect(self.lisaa_meno)
        self.jaottelu.valmisnappi.clicked.connect(self.lisaa_jaottelu)
        self.tarkeydet.valmisnappi.clicked.connect(self.muuta_tarkeys)
        self.saasta.saasto_nappi.clicked.connect(self.tee_saasto)

        graphicview= QtWidgets.QGraphicsView(self.scene,self)
        graphicview.setGeometry(50,90,750,500)
        self.show()

#Luo tekstin
    def teksti(self):
        self.label=QtWidgets.QLabel(self)
        self.label.setText("Suurimmat menosi")
        self.label.setGeometry(50,30,500,30)
        self.label.setStyleSheet("font-size:20pt;font-weight:bold")

    #Luo napit
    def Nappi(self):
        self.nappi = QtWidgets.QPushButton("Lisää meno",self)
        self.nappi.move(819,90)
        self.nappi.resize(110,50)
        self.nappi.setStyleSheet("font: 2pt")
        self.nappi.setStyleSheet("background-color:tomato ; font-size:10pt;font-weight: bold")
        self.meno = Meno(self)
        self.nappi.clicked.connect(self.painettu_nappi_meno)

        self.nappi2 = QtWidgets.QPushButton("Lisää tulo",self)
        self.nappi2.move(819,140)
        self.nappi2.resize(110,50)
        self.nappi2.setStyleSheet("background-color: seagreen; font-size:10pt;font-weight: bold")
        self.tulo = Tulo(self)
        self.nappi2.clicked.connect(self.painettu_nappi_tulo)


        self.nappi3 = QtWidgets.QPushButton("Lisää ryhmittely",self)
        self.nappi3.move(819,275)
        self.nappi3.resize(110,50)
        self.nappi3.setStyleSheet("background-color: peru; font-size:8pt;font-weight: bold")
        self.jaottelu = Jaottelu()
        self.nappi3.clicked.connect(self.painettu_nappi_jaottelu)

        self.nappi4 = QtWidgets.QPushButton("Muut?",self)
        self.nappi4.move(819,375)
        self.nappi4.resize(110,50)
        self.nappi4.setStyleSheet("background-color: #8d89a6; font-size:10pt;font-weight: bold")
        self.muut= Muut()
        self.nappi4.clicked.connect(self.painettu_nappi_muut)

        self.nappi5 = QtWidgets.QPushButton("Poista ryhmittely", self)
        self.nappi5.move(819, 325)
        self.nappi5.resize(110, 50)
        self.nappi5.setStyleSheet("background-color: purple; font-size:7pt;font-weight: bold;color: white")
        self.nappi5.clicked.connect(self.painettu_nappi_poista_jaottelu)
        self.nappi5.hide()

        self.nappi6 = QtWidgets.QPushButton("Muuta tärkeyttä",self)
        self.nappi6.move(819,489)
        self.nappi6.resize(110,50)
        self.nappi6.setStyleSheet("background-color: #e6b873; font-size:7pt;font-weight: bold")
        self.tarkeydet=Tarkeydet()
        self.nappi6.clicked.connect(self.painettu_nappi_muuta_tarkeytta)


        self.nappi7 = QtWidgets.QPushButton("Haluan säästää",self)
        self.nappi7.move(819,539)
        self.nappi7.resize(110,50)
        self.nappi7.setStyleSheet("background-color: #8dba92; font-size:8pt;font-weight: bold")
        self.saasta=Saasta()
        self.nappi7.clicked.connect(self.painettu_nappi_saasta)

#Kun nappia painetaan sulkee muut ikkunat ja avaa kyseisen.
    def painettu_nappi_muut(self):
        self.muut.luo_tekstit(self.muutmaara, self.muutyritys, self.menot, self.muutkokomaara)
        self.muut.show()
        self.meno.close()
        self.tulo.close()
        self.saasta.close()
        self.jaottelu.close()
        self.tarkeydet.close()

    # Kun nappia painetaan sulkee muut ikkunat ja avaa kyseisen.
    def painettu_nappi_meno(self):
        self.meno.show()
        self.muut.close()
        self.tulo.close()
        self.saasta.close()
        self.jaottelu.close()
        self.tarkeydet.close()

    # Kun nappia painetaan sulkee muut ikkunat ja avaa kyseisen.
    def painettu_nappi_tulo(self):
        self.tulo.show()
        self.meno.close()
        self.muut.close()
        self.saasta.close()
        self.jaottelu.close()
        self.tarkeydet.close()

    # Kun nappia painetaan sulkee muut ikkunat ja avaa kyseisen.
    def painettu_nappi_jaottelu(self):
        self.jaottelu.nappulat(self.kaksulotteinen)
        self.jaottelu.show()
        self.jaottelu.nappulat(self.kaksulotteinen)
        self.meno.close()
        self.saasta.close()
        self.tulo.close()
        self.muut.close()
        self.tarkeydet.close()

    # Kun nappia painetaan sulkee muut ikkunat ja avaa kyseisen.
    def painettu_nappi_poista_jaottelu(self):
        self.varmistin=False
        self.jaottelu.close()
        self.meno.close()
        self.saasta.close()
        self.tulo.close()
        self.muut.close()
        self.tarkeydet.close()
        self.scene.clear()
        self.kaksulotteinen=[]
        self.kaksulotteinen2()
        self.top10()
        self.luo_piirakka_diagrammi()
        self.add_kokonaismeno_ja_tulo()
        self.nappi5.hide()

    # Kun nappia painetaan sulkee muut ikkunat ja avaa kyseisen.
    def painettu_nappi_muuta_tarkeytta(self):
        if not self.varmistin:
            self.kaksulotteinen2()
        self.tarkeydet.nappulat(self.kaksulotteinen)
        self.meno.close()
        self.saasta.close()
        self.muut.close()
        self.tulo.close()
        self.jaottelu.close()
        self.tarkeydet.show()

    # Kun nappia painetaan sulkee muut ikkunat ja avaa kyseisen.
    def painettu_nappi_saasta(self):
        self.meno.close()
        self.muut.close()
        self.tulo.close()
        self.jaottelu.close()
        self.tarkeydet.close()
        self.saasta.show()

#Luo värit, joita käytetään piirakka diagrammissa
    def luo_vari(self):
        self.menot= (self.avaa.get_kumulatiivinen_meno()/100)
        self.tulot= (self.avaa.get_kumulatiivinen_tulo()/100)

        numerot = [173, 116, 96, 136, 56, 45, 168, 74, 92, 214, 163, 84, 245, 213, 188, 249, 227, 203, 234, 200, 202,
                   242, 213, 248, 230, 192, 233, 191, 171, 203, 141, 137, 166]
        q = 0
        self.varit = []
        z=0
        # Tehdään värit, numerot listan avulla.
        while z<=10:
            numerolista = []
            for i in range(3):
                numerolista.append(numerot[q])
                q += 1
            self.varit.append(QColor(numerolista[0], numerolista[1], numerolista[2]))
            z+=1

    #Luo piirakan, Graphicviewhin
    def luo_piirakka_diagrammi(self):
        vari = 0
        alku_kulma = 0
        #Luo piirakan
        for yritys in self.top10maara:
            kulma = round(float((yritys/100) * 5760) / self.menot)
            self.piirakka = QtWidgets.QGraphicsEllipseItem(0, 0, 400, 400)
            self.piirakka.setPos(-150,-275)
            self.piirakka.setStartAngle(alku_kulma)
            self.piirakka.setSpanAngle(kulma)
            self.luo_neliot(vari)
            self.piirakka.setBrush(self.varit[vari])
            alku_kulma += kulma
            vari += 1
            self.scene.addItem(self.piirakka)
    #Luo neliöt ja selitteet Graphicviewhin
    def luo_neliot(self,vari):
        if vari==0:
            self.laske=0

        #Luo neliöt ja selitteet
        self.hinta=-self.top10maara[vari]/100
        self.prosentti=round(self.hinta/(-self.menot/100))
        self.nelio=QtWidgets.QGraphicsRectItem(-450,-300+self.laske,15,15)
        self.teksti=QtWidgets.QGraphicsTextItem("{} {:.2f}€ ({}%)".format(self.top10yritys[vari],self.hinta,self.prosentti))
        self.teksti.setPos(-435,-308+self.laske)
        self.teksti.setScale(1.3)
        self.scene.addItem(self.teksti)
        self.nelio.setBrush(self.varit[vari])
        self.scene.addItem((self.nelio))
        self.laske+=25

    #Luo kokonias meno ja tulo tekstit Graphicviewhin
    def add_kokonaismeno_ja_tulo(self):
        self.menoteksti=QtWidgets.QGraphicsTextItem("Kokonaismenot: {:.2f}€".format(-self.menot))
        self.menoteksti.setPos(-480,50)
        self.menoteksti.setDefaultTextColor(QtGui.QColor("firebrick"))
        self.menoteksti.setScale(2.2)
        self.scene.addItem(self.menoteksti)

        self.tuloteksti=QtWidgets.QGraphicsTextItem("Kokonaistulot: {:.2f}€".format(self.tulot))
        self.tuloteksti.setPos(-480,100)
        self.tuloteksti.setDefaultTextColor(QtGui.QColor("green"))
        self.tuloteksti.setScale(2.2)
        self.scene.addItem(self.tuloteksti)

    #Tuo kaksulotteisen listan ja pistää sen suuruus järjestykseen
    def kaksulotteinen(self):
        self.uuskaksulotteinen=self.avaa.get_kaksulotteinenlista()
        self.uuskaksulotteinen=sorted(self.uuskaksulotteinen, key=lambda x:x[0])
        self.kaksulotteinen=self.uuskaksulotteinen

    #Tuo kaksulotteisen listan ja pistää järjestykseen
    def kaksulotteinen2(self):
        self.avaa.kaksulotteinen2()
        self.uuskaksulotteinen=self.avaa.get_kaksulotteinenlista()
        self.uuskaksulotteinen=sorted(self.uuskaksulotteinen, key=lambda x:x[0])
        self.kaksulotteinen=self.uuskaksulotteinen
        self.top10()

    #Jakaa menot top 10 suurimpiin menoihin ja muihin
    def top10(self):
        self.top10maara=[]
        self.top10yritys=[]
        p=0
        try:
            while p<10:
                tupla=self.kaksulotteinen[p]
                self.top10maara.append(tupla[0])
                self.top10yritys.append(tupla[1])
                p+=1

            q=10
            self.muutmaara=[]
            self.muutyritys=[]
            self.muutkokomaara=0
            while q<len(self.kaksulotteinen):
                muut=self.kaksulotteinen[q]
                self.muutmaara.append(muut[0])
                self.muutyritys.append(muut[1])
                self.muutkokomaara+=int(muut[0])
                q+=1
            self.top10yritys.append("Muut")
            self.top10maara.append(self.muutkokomaara)
            if len(self.kaksulotteinen)>10:
                self.nappi4.show()
            else:
                self.nappi4.hide()

#Jos menoja on alle 10, piilottaa muut napin.
        except IndexError:
            self.top10maara = []
            self.top10yritys = []
            self.kaksulotteinen=sorted(self.kaksulotteinen, key=lambda x:x[0])
            for yks in self.kaksulotteinen:
                self.top10maara.append(yks[0])
                self.top10yritys.append(yks[1])
            self.nappi4.hide()

#Lisää tulon, kun tuloja lisätään
    def lisaa_tulo(self):
        ok=self.tulo.maara.text()
        z=0
        if "," in ok:
            ok=ok.split(",")

            if len(ok[1])>2:
                ok[1]=ok[1][0:2]
            ok=ok[0]+ok[1]
            z=1
        elif "." in ok:
            ok=ok.split(".")
            if len(ok[1])>2:
                ok[1]=ok[1][0:2]
            ok=ok[0]+ok[1]
            z=1
        if ok.isnumeric():
            if z==1:
                ok=int(ok)
                ok=float(ok/100)
            ok=float(ok)
            if ok>0:
                self.tulot+=ok
                self.scene.removeItem(self.menoteksti)
                self.scene.removeItem(self.tuloteksti)
                self.add_kokonaismeno_ja_tulo()
        self.tulo.maara.clear()
        self.tulo.close()

#Lisää menon, kun menoja lisätään. (Tosi monimutkainen)
    def lisaa_meno(self):
        z=0
        maara=self.meno.maara.text()
        if "-" in maara:
            maara=maara.replace("-","")
        if "," in maara:
            maara=maara.split(",")
            if len(maara[1])>2:
                maara[1]=maara[1][0:2]
            maara=maara[0]+maara[1]
            z=1
        elif "." in maara:
            maara=maara.split(".")
            if len(maara[1])>2:
                maara[1]=maara[1][0:2]
            maara = maara[0] + maara[1]

            z=1

        if maara.isnumeric():
            if maara[0]=="0" and maara[1]!="0":
                maara+="0"
            maara=float(maara)
            if z==0:
                maara=maara*100
            maara=int(maara)
            if maara>0:
                maara=-maara
            paikka=self.meno.paikka.text()
            if paikka!="":
                self.menot+=maara/100
                self.scene.clear()
                if self.varmistin==False and self.saastopaalla==False:
                    if -maara>=200:
                        tarkeys=20
                    elif -maara>=150:
                        tarkeys=15
                    elif -maara>=100:
                        tarkeys=10
                    elif -maara>=50:
                        tarkeys=5
                    else:
                        tarkeys=1
                    self.avaa.lisaa_uusi_meno(maara, paikka, tarkeys)
                    self.kaksulotteinen2()
                    self.top10()
                    self.luo_piirakka_diagrammi()

                else:
                    if paikka in self.avaa.yrityslista:
                        self.avaa.lisaa_uusi_meno(maara, paikka, 1)
                        maara=meno.get_maara(self.avaa.dictionary[paikka])
                        tarkeys=meno.get_tarkeys(self.avaa.dictionary[paikka])
                        for yritys in self.kaksulotteinen:
                            if paikka==yritys[1]:
                                self.kaksulotteinen.remove(yritys)
                                lisaa=[maara,paikka,tarkeys]
                                self.kaksulotteinen.append(lisaa)
                                break
                            else:
                                lisaa=[maara,paikka,tarkeys]
                                self.kaksulotteinen.append(lisaa)
                                break

                    else:
                        if maara <= -200:
                            tarkeys = 20
                        elif maara <= -150:
                            tarkeys = 15
                        elif maara <= -100:
                            tarkeys = 10
                        elif maara <= -5:
                            tarkeys = 5
                        else:
                            tarkeys = 1
                        self.avaa.lisaa_uusi_meno(int(maara), paikka, int(tarkeys))
                        lisaa=[maara,paikka,tarkeys]
                        self.kaksulotteinen.append(lisaa)
                    self.kaksulotteinen = sorted(self.kaksulotteinen, key=lambda x: x[0])
                    self.top10()
                    self.luo_piirakka_diagrammi()
                self.add_kokonaismeno_ja_tulo()


        self.meno.maara.clear()
        self.meno.paikka.clear()
        self.meno.close()
        self.jaottelu.nappulat(self.kaksulotteinen)

#Yhdistää jaottelussa pistetyt yritykset annetun nimen alle
    def lisaa_jaottelu(self):
        self.loppulista=self.jaottelu.loppulista
        if self.loppulista==[] :
            pass
        else:
            self.jaottelu.close()
            if not self.saastopaalla:
                self.nappi5.show()
            self.tee_jaottelu()
            self.scene.clear()
            self.top10()
            self.luo_piirakka_diagrammi()
            self.add_kokonaismeno_ja_tulo()
            self.varmistin=True

#Muuttaa kaikkien listassa olevien menojen tärkeydyt
    def muuta_tarkeys(self):
        self.tarkeyslista=self.tarkeydet.loppulista
        if self.tarkeyslista==[]:
            pass
        elif not self.varmistin:
            for yks in self.tarkeyslista:
                tarkeys=yks.pop(0)
                if tarkeys<=0:
                    tarkeys=1
                if tarkeys>20:
                    tarkeys=20
                for yritys in yks:
                    self.avaa.muuta_tarkeys(yritys,tarkeys)
        elif self.varmistin:
            for yks in self.tarkeyslista:
                tarkeys=yks.pop(0)
                if tarkeys>20:
                    tarkeys=20
                elif tarkeys<=0:
                    tarkeys=1
                for yritys in yks:
                    if yritys in self.avaa.yrityslista:
                        self.avaa.muuta_tarkeys(yritys,tarkeys)
                        for yrityskaksulotteinen in self.kaksulotteinen:
                            if yritys==yrityskaksulotteinen[1]:
                                yrityskaksulotteinen[2]=tarkeys
                    else:
                        for yrityskaksulotteinen in self.kaksulotteinen:
                            if yritys==yrityskaksulotteinen[1]:
                                yrityskaksulotteinen[2]=tarkeys

        self.tarkeydet.close()

#Poistaa listasta menoja, jotta saadaan säästettyä sopiva määrä. (Pienentää myös menoja)
    def tee_saasto(self):
        maara=self.saasta.teksti.text()
        self.saasta.close()
        self.saasta.teksti.clear()
        if "-" in maara:
            maara=maara.replace("-","")
        if "," in maara:
            maara=maara.split(",")
            if len(maara[1])>2:
                maara[1]=maara[1][0:2]
            maara=maara[0]+maara[1]
            z=1
        elif "." in maara:
            maara.split(",")
            if len(maara[1])>2:
                maara[1]=maara[1][0:2]
            maara = maara[0] + maara[1]
            z=1

        if maara.isnumeric():
            maara=int(maara)
            maara=maara*100
            laskin=0
            i=0
            if self.varmistin == True:
                lista=self.kaksulotteinen
            else:
                self.kaksulotteinen2()
                lista=self.kaksulotteinen
            lista = sorted(lista, key=lambda x: (x[2], -x[0]))
            while i==0:
                for yks in lista:
                    laskin-=yks[0]
                    if laskin<maara:
                        lista.remove(yks)
                        self.avaa.nollaa(yks)
                        if len(lista) == 0:
                            i=1
                        break

                    else:
                        uus=maara-laskin
                        yks[0]=uus
                        i=1
                        self.avaa.muuta(yks,uus)
                        break

        lista = sorted(lista, key=lambda x: x[0])
        self.saastopaalla=True
        self.menot+=(maara/100)
        self.kaksulotteinen = lista
        self.scene.clear()
        self.top10()
        self.luo_piirakka_diagrammi()
        self.add_kokonaismeno_ja_tulo()
        self.nappi5.hide()
        self.nappi6.hide()
        self.nappi7.hide()

#Tekee jaottelun apu funktio aikaisempaan jaottelu funktioon
    def tee_jaottelu(self):
        lista=self.kaksulotteinen
        for jaos in self.loppulista:
            maara=0
            tarkeys=0
            nimi=jaos.pop(0)
            for yks in jaos:
                for kaks in self.kaksulotteinen:
                    if yks==kaks[1]:
                        lista.remove(kaks)
                        tarkeys+=kaks[2]
                        maara+=kaks[0]
                        break
            if tarkeys>20:
                tarkeys=20
            lisaa=[maara,nimi,tarkeys]
            lista.append(lisaa)
        lista = sorted(lista, key=lambda x: x[0])
        self.kaksulotteinen=lista
if __name__=="__main__":
    App=QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    sys.exit(App.exec())