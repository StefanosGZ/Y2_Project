import unittest
from Kuvaaja import Window
from Kuvaaja import Meno
from Kuvaaja import Muut
from Kuvaaja import Tulo
from Kuvaaja import Tarkeydet
from Kuvaaja import Saasta
from Meno import meno
from Avaa_tiedosto import avaa

#Kaikki testauksest
class Test(unittest.TestCase):

    def testaa1(self):
        self.meno=meno(-300,"McDonalds",1)
        self.assertEqual(self.meno.get_tarkeys(),1)

    def testaa2(self):
        self.meno=meno(-300,"McDonals",1)
        self.assertEqual(self.meno.get_maara(),-300)

    def testaa3(self):
        self.meno=meno(-300,"McDonals",1)
        self.assertEqual(self.meno.get_paikka(),"McDonals")

    def testaa4(self):
        self.meno=meno(-300,"McDonals",1)
        self.meno.add_tarkeys()
        self.assertEqual(self.meno.get_tarkeys(),2)

    def testaa5(self):
        self.meno=meno(-300,"McDonals",1)
        self.meno.muuta_tarkeys(200)
        self.assertEqual(self.meno.get_tarkeys(),20)

    def testaa6(self):
        self.meno=meno(-300,"McDonals",1)
        self.meno.muuta_tarkeys(0)
        self.assertGreater(self.meno.get_tarkeys(),0)

    def testaa7(self):
        self.meno=meno(-300,"McDonals",1)
        self.meno.add_maara(-300)
        self.assertEqual(self.meno.get_maara(),-600)

    def testaa8(self):
        #Käytä arvoja 1 ja 0
        self.avaa=avaa()
        testaa="Wolt"
        self.assertIn(testaa,self.avaa.yrityslista)

    def testaa9(self):
        #Käytä arvoja 2 ja 0
        self.avaa=avaa()
        testaa="Wolt"
        self.assertNotIn(testaa,self.avaa.yrityslista)

    def testaa10(self):
        #Käytä arvoa 1 ja 0
        self.avaa=avaa()
        self.assertEqual(self.avaa.z,1)

    def testaa11(self):
        #Käytä arvoa 2 ja 0
        self.avaa=avaa()
        self.assertEqual(self.avaa.z,1)

    def testaa12(self):
        self.meno=meno(-300,"McDonalds",2)
        avaa.kokeile(self,"Kayttotili.csv")
        avaa.dictionary={"McDonalds":self.meno}
        avaa.muuta_tarkeys(avaa(),"McDonalds",15)
        self.assertEqual(15,meno.get_tarkeys())

if __name__ == '__main__':
    unittest.main()