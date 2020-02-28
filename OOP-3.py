#her ogrencinin tc,isim,soyisim,matematik yil sonu not ortolamasi,fizik ders sonu not ortalamasi,
#turkce yil sonu not ortalamasi bilgileri olsun.
#   a)okulda kac ogrencinin oldugunu gosteren
#   b) her bir dersten gecme notunun 50 oldugunu dusunursek
#       matematik dersinden gecen ogrencilerin ismini gosteren
#       fizik dersinden gecen ogrencilerin ismini gosteren
#       turkce dersinden gecen isimlerin ismini ve notlarini birlikte gosteren
#   c)uc notun ortalamasinin 50 ustunde olanlarin isi sinifi gectigini dusunursek sinifi gecenlerin tum bilgilerini gosteren programi yaziniz.
class okul():
    isimler=[]
    soyisimler=[]
    matemetik=[]
    fizik=[]
    turk=[]
    tcler=[]

    ogrenciSayisi = 0

    def __init__(self,isim,soyisim,tc,matavarage,fizikavarage,turkavarage):

        self.isim=isim
        self.soyisim=soyisim
        self.tc = tc
        self.matavarage=matavarage
        self.fizikavarage=fizikavarage
        self.turkavarage=turkavarage
        okul.isimler.append(self.isim)
        okul.soyisimler.append(self.soyisim)
        okul.tcler.append(self.tc)
        okul.matemetik.append(self.matavarage)
        okul.fizik.append(self.fizikavarage)
        okul.turk.append(self.turkavarage)
        okul.ogrenciSayisi=okul.ogrenciSayisi+1

    @classmethod
    def matematikdersGecme(cls):
        print('Matematik dersinden gecen ogrenciler: ')
        for i in range(len(okul.matemetik)):
            if okul.matemetik[i] >= 50:
                print('isim={} soyisim={} matematik={} '.format(okul.isimler[i], okul.soyisimler[i], okul.matemetik[i]))

    @classmethod
    def fizikdersGecme(cls):
        print('Fizik dersinden gecen ogrenciler: ')
        for i in range(len(okul.fizik)):
            if okul.fizik[i] >=50:
                print('isim={} soyisim={} fizik={} '.format(okul.isimler[i], okul.soyisimler[i], okul.fizik[i]))

    @classmethod
    def turkdersGecme(cls):
        print('Turkce dersinden gecen ogrenciler: ')
        for i in range(len(okul.turk)):
            if okul.fizik[i] >= 50:
                print('isim={} soyisim={} turk={} '.format(okul.isimler[i], okul.soyisimler[i], okul.fizik[i]))

    @classmethod
    def tumdersGecme(cls):
        print('Sinifi gecen ogrenciler: ')
        for i in range(len(okul.matemetik)):
            if ((okul.fizik[i]+okul.matemetik[i]+okul.turk[i])/3) >= 50:
                print('TC={} isim={} soyisim={} matematik={} fizik={} turk={} '.format(okul.tcler[i],okul.isimler[i], okul.soyisimler[i],okul.matemetik[i],okul.fizik[i],okul.turk[i],))


ogrenci1=okul('Mehmet','Bagriyanik',11111111111,40,60,70)
ogrenci2=okul('Emre','Hamarat',22222222222,35,50,20)
ogrenci3=okul('Mustafa','Can',33333333333,90,80,90)
ogrenci4=okul('Deniz','Sert',44444444444,50,50,40)


#print(okul.ogrenciSayisi) #cevap a)okulda kac ogrenci oldugunu init fonksiyonun icine ekledigimiz ifade ile ogrenebiliriz
#print(okul.isimler)

okul.matematikdersGecme()
okul.fizikdersGecme()
okul.turkdersGecme()
okul.tumdersGecme()