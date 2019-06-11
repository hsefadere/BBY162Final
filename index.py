from tkinter import *
from tkinter import messagebox


bilgi = ["ankara", "2171"]

ilkSayfa = Tk()

fotograf = PhotoImage(file = "resim01.gif")
resim = Label (ilkSayfa, image=fotograf)
resim.pack()


ilkSayfa.title("Hacettepe Üniversitesi Kitap Arama Motoru")
ilkSayfa.geometry("500x500+10+10")
ilkSayfa.configure(background="turquoise")

başlangıç = Label(ilkSayfa)
başlangıç.config(text="KÜTÜPHANE KATALOĞUNA HOŞGELDİNİZ \n Lütfen Giriş Yapınız",bg="turquoise")
başlangıç.pack()

kullanıcıAdı= Label(ilkSayfa)
kullanıcıAdı.config(text="Kullanıcı Adı", bg="turquoise", fg="brown",font=("Monotype Corsiva", 13))
kullanıcıAdı.pack()

kullanıcıGir = Entry(ilkSayfa)
kullanıcıGir.pack()

şifreYazı = Label(ilkSayfa)
şifreYazı.config(text="şifre", bg="turquoise", fg="brown",font=("Monotype Corsiva", 13))
şifreYazı.pack()

şifreGir = Entry(ilkSayfa,show="*")
şifreGir.pack()



sonuç = Label(ilkSayfa)
sonuç.config(text="Giriş yapılmadı",bg="white", fg="black", font=("times new roman", 10))
sonuç.pack()


def gir():
    kullanıcıA = kullanıcıGir.get()
    şifre = şifreGir.get()
    if kullanıcıA == bilgi[0] and şifre == bilgi[1]:
        yeni()

    elif kullanıcıA != bilgi[0] and şifre == bilgi[1]:
        sonuç.config(text="kullanıcı adınız yanlış girilmiştir")
    elif kullanıcıA == bilgi[0] and şifre != bilgi[1]:
        sonuç.config(text="şifreniz yanlış girilmiştir")
    else:
        sonuç.config(text="Tekrar Deneyiniz")

girbutonu = Button(ilkSayfa)
girbutonu.config(text="Giriş Yap",bg="yellow", font=("times new roman", 10), cursor="star", command=gir)
girbutonu.pack()

def yeni():

    def kitap_ekle():
        global kitap,yazar,tur,isbn,yayinyili,pencere01
        pencere01 = Tk()
        baslik01 = pencere01.title("Kitap Kayıt Penceresi")
        pencere01.configure(background="turquoise")

        kitap= Entry(pencere01,width=30)
        kitap.grid(column=2, row=1)
        yazar = Entry(pencere01, width=30)
        yazar.grid(column=2, row=2)
        tur = Entry(pencere01, width=30)
        tur.grid(column=2, row=3)
        isbn = Entry(pencere01, width=30)
        isbn.grid(column=2, row=4)
        yayinyili = Entry(pencere01, width=30)
        yayinyili.grid(column=2, row=5)

        kaydet = Button(pencere01, text= "Kaydet",command=kitap_kaydet,bg="yellow", fg="black", )
        kaydet.grid(column=1, row=6)
        cikis = Button(pencere01 ,text = "Kapat", command=pencere01.destroy,bg="yellow", fg="black",cursor="man")
        cikis.grid(column=3, row=6)


        Label(pencere01,bg="turquoise",text='Kitap Adı: ').grid(column=1, row=1)
        Label(pencere01,bg="turquoise",text='Yazar Adı: ').grid(column=1, row=2)
        Label(pencere01,bg="turquoise",text='Kitabın Türü: ').grid(column=1, row=3)
        Label(pencere01,bg="turquoise",text='ISBN :').grid(column=1, row=4)
        Label(pencere01,bg="turquoise",text='Yayın Yılı :').grid(column=1, row=5)

    def kitap_kaydet():

        liste = str(("\nKitap Adı:" +kitap.get() + "-Yazar Adı:" + yazar.get() + "-Tür:" + tur.get() + "-ISBN:" + isbn.get() + "-Yayın Yılı:" + yayinyili.get()) + "\n\n")
        dosya = open("katalog.txt", "a")
        for i in liste:
            dosya.write(i)
        dosya.close()
        messagebox.showinfo('Sonuç','Kaydetme işleminiz başarıyla gerçekleşmiştir!')
        command = pencere01.destroy()

    def kitaplist():
            pencere02= Tk()
            baslik02 = pencere02.title("Kayıtlı Kitaplar")
            pencere02.configure(background="turquoise")
            file = open("katalog.txt")
            yaz = file.read()
            file.close()


            kitaplist = Label(pencere02, text=yaz, bg="turquoise")
            kitaplist.pack()

            cikis = Button(pencere02 ,text = "Kapat", bg="turquoise",fg="black",cursor="man",command=pencere02.destroy)
            cikis.pack()


    global ısbn, ısbnalanı
    global kitap, kitapadıalanı
    global yazaradı, yazaradıalanı
    global yıl, yayınyılı

    anaSayfa = Tk()
    anaSayfa.title("==============Kitap Arama Motoru==============")


    anaSayfa.configure(background="turquoise")
    anaSayfa.geometry("415x500+500+60")
    anaSayfa.resizable(0,0)
    giriş = Label(anaSayfa,text="Kütüphane Kataloğu",bg="turquoise", fg="red", font=("gabriola", 19)).grid()

    ısbn = ["74161", "18462", "90872","69425"]
    kitapadıalanı = ["tutunamayanlar","iyi vatandaş iyi insan","yokuşa doğru","hasretinden prangalar eskittim"]
    yazaradıalanı = ["oğuz atay", "hasan ali yücel","suut kemal yetkin","ahmed arif"]
    yayınyılı = ["1972", "1971", "1963", "1990"]

    kitap_ekle = Button(anaSayfa, text="Kitap Ekle", bg="lightblue", fg="red", cursor="star", font="bold",command=kitap_ekle)
    kitap_ekle.grid(row="1")

    kitapları_listele = Button(anaSayfa, text="Kitapları Listele",bg="lightblue",fg="red",cursor="star",font="bold", command=kitaplist)
    kitapları_listele.grid(row="2")




    kitaparama = Label(anaSayfa, text="Lütfen ISBN Giriniz:", bg="turquoise", fg="brown", font=("Times New Roman", 13)).grid(row=3,sticky=W )
    ısbnalanı = Entry(anaSayfa,width=27)
    ısbnalanı.grid(row=3,sticky=E)
    aramabutonu = Button(anaSayfa,text="ARA", bg="white", fg="black", font=("calibri", 10), cursor="star", command=giris4).grid(row=3, column=2)


    kitaparama = Label(anaSayfa, text="Lütfen Kitap Adı Giriniz:", bg="turquoise", fg="brown",font=("Times New Roman", 13)).grid(row=4, sticky=W)
    kitap = Entry(anaSayfa,width=27)
    kitap.grid(row=4,sticky=E)
    aramabutonu = Button(anaSayfa, text="ARA", bg="white", fg="black", font=("calibri", 10), cursor="star", command=giris3).grid(row=4, column=2)


    kitaparama= Label(anaSayfa, text="Lütfen Yazar Adı Giriniz:", bg="turquoise", fg="brown",font=("Times New Roman", 13)).grid(row=5, sticky=W)
    yazaradı = Entry(anaSayfa,width=27)
    yazaradı.grid(row=5, sticky=E)
    aramabutonu = Button(anaSayfa, text="ARA", bg="white", fg="black", font=("calibri", 10), cursor="star",command=giris2).grid(row=5,column=2)

    kitaparama=Label(anaSayfa, text="Lütfen Yayın Yılını Giriniz:", bg="turquoise", fg="brown",font=("Times New Roman", 13)).grid(row=6, sticky=W)
    yıl = Entry(anaSayfa,width=27)
    yıl.grid(row=6, sticky=E)
    aramabutonu = Button(anaSayfa, text="ARA", bg="white", fg="black", font=("calibri", 10), cursor="star", command=giris1).grid(row=6, column=2)

    cikis = Button(anaSayfa, text="Kapat", command=exit, fg="black", bg="yellow", cursor="man")
    cikis.grid(row=7, column=2)

    hakkindabutonu = Button(anaSayfa, text="Hakkında", cursor="star", command=hakkinda)
    hakkindabutonu.grid()


    duyuru = Label(anaSayfa, text="   |===============DUYURU TABLOSU================|"
                                  "\n  **2.000 yeni kitap-makale-deneme bilgileri sayfamıza eklenmiştir"
                                  "\n  **Kitap güncelleme bölümü çok yakında hizmetinize sunulacaktır "
                                  "\n  |============================================|",bg="red").grid(row=9,sticky=W)
    iletişimbutonu = Button(anaSayfa, text="İletişim", cursor="star", command=iletisim)
    iletişimbutonu.grid()


def giris1():
    yılı = yıl.get()

    if yılı == yayınyılı[0]:
        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI: Tutunamayanlar\n YAZAR ADI: Oğuz Atay\n TÜR: Roman\n YAYIN YILI: 1972\n ISBN: 74161")
    elif yılı ==yayınyılı[1]:
        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI:İyi Vatandaş İyi İnsan\n YAZAR ADI:Hasan Ali Yücel\n TÜR:Makale\n ISBN:18462\n YAYIN YILI:1971")


    elif yılı == yayınyılı[2]:
        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI:Yokuşa Doğru\n YAZAR ADI:Suut Kemal Yetkin\n TÜR:Deneme\n ISBN:90872\n YAYIN YILI:1963")

    elif yılı == yayınyılı[3]:
        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI:Hasretinden Prangalar Eskittim\n YAZAR ADI:Ahmet Arif\n TÜR:Şiir Kitabı\n ISBN:69425\n YAYIN YILI:1990")
    else:
        tekrar_iptal = messagebox.askretrycancel("Sonuç","Aradığınız kitap kütüphanemizde bulunmamaktadır!")



def giris2():
    yaz = yazaradı.get()

    if yaz == yazaradıalanı[0]:
        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI: Tutunamayanlar\n YAZAR ADI: Oğuz Atay\n TÜR: Roman\n YAYIN YILI: 1972\n ISBN: 74161")

    elif yaz ==yazaradıalanı[1]:
        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI:İyi Vatandaş İyi İnsan\n YAZAR ADI:Hasan Ali Yücel\n TÜR:Makale\n ISBN:18462\n YAYIN YILI:1971")

    elif yaz == yazaradıalanı[2]:
        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI:Yokuşa Doğru\n YAZAR ADI:Suut Kemal Yetkin\n TÜR:Deneme\n ISBN:90872\n YAYIN YILI:1963")

    elif yaz == yazaradıalanı[3]:
        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI:Hasretinden Prangalar Eskittim\n YAZAR ADI:Ahmet Arif\n TÜR:Şiir Kitabı\n ISBN:69425\n YAYIN YILI:1990")
    else :
        tekrar_iptal = messagebox.askretrycancel("Sonuç","Aradığınız kitap kütüphanemizde bulunmamaktadır!")




def giris3():
    adı = kitap.get()

    if adı == kitapadıalanı[0]:

        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI: Tutunamayanlar\n YAZAR ADI: Oğuz Atay\n TÜR: Roman\n YAYIN YILI: 1972\n ISBN: 74161")

    elif adı == kitapadıalanı[1]:
        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI:İyi Vatandaş İyi İnsan\n YAZAR ADI:Hasan Ali Yücel\n TÜR:Makale\n ISBN:18462\n YAYIN YILI:1971")

    elif adı == kitapadıalanı[2]:
        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI:Yokuşa Doğru\n YAZAR ADI:Suut Kemal Yetkin\n TÜR:Deneme\n ISBN:90872\n YAYIN YILI:1963")

    elif adı == kitapadıalanı[3]:
        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI:Hasretinden Prangalar Eskittim\n YAZAR ADI:Ahmet Arif\n TÜR:Şiir Kitabı\n ISBN:69425\n YAYIN YILI:1990")
    else:
        tekrar_iptal = messagebox.askretrycancel("Sonuç","Aradığınız kitap kütüphanemizde bulunmamaktadır!")



def giris4():
    ısbnn = ısbnalanı.get()

    if ısbnn == ısbn[0]:

        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI: Tutunamayanlar\n YAZAR ADI: Oğuz Atay\n TÜR: Roman\n YAYIN YILI: 1972\n ISBN: 74161")

    elif ısbnn == ısbn[1]:
        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI:İyi Vatandaş İyi İnsan\n YAZAR ADI:Hasan Ali Yücel\n TÜR:Makale\n ISBN:18462\n YAYIN YILI:1971")

    elif ısbnn == ısbn[2]:
        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI:Yokuşa Doğru\n YAZAR ADI:Suut Kemal Yetkin\n TÜR:Deneme\n ISBN:90872\n YAYIN YILI:1963")

    elif ısbnn == ısbn[3]:
        messagebox.showinfo("Aradığınız Kitap","KİTAP ADI:Hasretinden Prangalar Eskittim\n YAZAR ADI:Ahmet Arif\n TÜR:Şiir Kitabı\n ISBN:69425\n YAYIN YILI:1990")
    else:
        tekrar_iptal = messagebox.askretrycancel("Sonuç","Aradığınız kitap kütüphanemizde bulunmamaktadır!")


def hakkinda():
    hakkinda = Tk()
    hakkinda.title("Hakkında")
    hakkinda.geometry("180x200+250+200")
    Label(hakkinda, text="\n\n\n**Hacettepe Üniversitesi** \n tarafından gerçekleştirilen \n yeni kitap arama motoru \n 2019 yılında \n hizmete sunulmuştur.").pack()

def iletisim():
    iletisim = Tk()
    iletisim.title("İletişim bilgileri")
    iletisim.geometry("140x150+250+200")
    Label(iletisim, text="\n\n\nankara@gmail.com\n Faks= +90 312 123 45 67").pack()


mainloop()