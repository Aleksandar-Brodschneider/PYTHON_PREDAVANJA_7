"""
ORGANIZACIJA DELA: 1. ZAČNI Z ZAPISKI
                   2. ZAPISKE DELAJ V PREVAJALNIKU PYCHARM (da se navadiš nanj)
                   3. VSE PONOVI ZA PROFESORJEM IN GRADIVOM
                   4. PONOVI NAJMANJ 3 KRAT
                   5. NE UPORABLJAJ COPY, PASTE IN AVTOMATOV
                   6. VSE NAREDI ROČNO
                   7. VSAKO VAJO NAREDI NA VEČ NAČINOV
                   8. PREDELAJ SNOV PRED PREDAVANJI
                   9. ZA VSAKO MISEL, NAPAKO IN SPOZNANJE NAREDI ZAPISEK
                   10. PREIZKUSI VSE KODE KAR SE SPOMNEŠ
                   11. IMEJ RAD/A TO KAR DELAŠ
                   12. DELAJ Z VESELJEM
"""
"""
DEF = FUNKCIJA -> DEFINE, DEFINITION
NEZNANE PODATKE IN FORMULE PRIDOBIMO S POIZVEDBO NA SPLETU!
"""
"""
DOMAČA NALOGA - SEZNAMI
seznam1_16 = range(1,16)
for x in seznam1_16:
#ali for x in range(1,16)...krajše
    print(x)


seznam_lihe_1_30 = range(1,30,2)
for x in seznam_lihe_1_30:
    print(x)


seznam_večkratniki_50_100 = range(50,105,5)
for x in seznam_večkratniki_50_100:
    print(x)


seznam_5_oseb = ("Maja","Vija","Vaja", "Ven", "Gonzalez")
for x in seznam_5_oseb:
    print(x)

seznam_celo_realno_ime = (2,2.5,"Aja")
for x in seznam_celo_realno_ime:
    print(x)

# pazi indentacijo, index, for-in, int(input), : !
poštevanka = int(input("Vnesi poljubno število: "))
for x in range(1,11):

    print("{0} * {1} = {2}".format(x,poštevanka,x * poštevanka))

# agregatno stanje
temperatura = range(-50,60,10)
for F in temperatura:
    print(F)


    # oziroma

F = int(input("Kolikšna je temperatura vode v F? "))
C = (F - 32)* 5/9
if C > 100:
    ag_stanje = "para"
    print("Pri temperaturi", F, "F je voda", ag_stanje, ".")
elif C < 0:
    ag_stanje = "led"
    print("Pri temperaturi", F, "F je voda", ag_stanje, ".")
else:
    print("Pri temperaturi",F,"F je voda tekoča.")

number = int(input("Napiši ena: "))
emoticons = {
    1:"😄",
    2:"dva"
}

print(emoticons[1
      ])
"""
def poštevanka():
    poštevanka = int(input("Vnesi poljubno število ti lulek: "))
    for x in range(1,31):
        print("{0} * {1} = {2}".format(x,poštevanka,x * poštevanka))


def vaja_1():
    število = input("Vnesi število, ki bo deljeno z 2: ")
    print("Ostanek števila " + število + " je", int(število) % 2,'.')



def prva_definicija():

    print('to je to')

    print(3887498)

def druga_definicija():
    print("Danes je lep dan.")

def slovar():
    slovar = {
        1:"ena",
        2:"dva"
    }
    print(slovar[2][2])


# !!!!!!!!!!!VNOS KNJIŽNJICE MATH !!!!!!!!!!!!
# PAZI NA FROM MATH IMPORT SQRT
from math import sqrt
# from math import * --> vnesi vse
# Če damo import math --> moramo zmeraj vnesti math.sqrt, ali math.pi
# Če damo form math import *--> pa kličemo direkt sqrt ali pi

def pitagorov_izrek():
    a = int(input("Stranica a je? "))
    b = int(input("Stranica a je? "))
    input(("stranica b je? "))
    print(sqrt(a**2+b**2))

# print(type(pitagorov_izrek))

# type()
def kvadrat_stranica_4cm():
    a = int(input("Vnesi stranico kvadrata: "))
    print("Obseg kvadrata je",a * 4,"cm.")

def kalkulator():
    a = int(input("Vnesi število: "))
    b = int(input("Vnesi število: "))
    ploščina = a*b
    print(ploščina)

def števec():
    števec = 0
    števec += 1
    print(števec)

# za + morata biti enaka tipa, pri vejici pa so lahko različna
#  spremenimo lahko le 2 v str in ne obratno!
def ime():
    ime = input("Vpiši svoje ime: ")
    print("Dober dan ",2, "!")


# input vedno registrira string, zato moramo obleči v int
def ploščina():
    a = int(input("Vnesi dolžino stranice: "))
    ploščina = a * 4
    print(type(a))

# float doda decimalko--> .0
def a():
    a = float(4)
    print(type(a))

# Raje daš float ko int, ker je lahko vnos decimalen!
# Decimalka je pika in ne vejica!
def volumen_kvadra():
    a = float(input("Vnesi stranico a: "))
    b = float(input("Vnesi število b: "))
    c = float(input("Vnesi število c: "))
    volumen_kvadra = a*b*c
    print(volumen_kvadra)
#     ali damo v print a*b*c-->print(a*b*c)
def volumen_kvadra():
    a = float(input("Vnesi stranico a: "))
    b = float(input("Vnesi število b: "))
    c = float(input("Vnesi število c: "))
    print(a*b*c)


"""
Performance. When it comes to performance, Scala is the clear winner over Python.
One reason Scala wins on performance is that it is a statically typed programming 
language and Python is a dynamically typed programming language. 
With statically typed languages, the compiler knows each variable or expression at runtime.
"""

def ploščina_trikotnika():
    a = float(input("Vnesi stranico a: "))
    ploščina = a**2 * sqrt(3)/4
    # zaokroži ploščino na dve decimalki --> round
    print(round(ploščina,2))

import math
def funkcija_math():

    print(math.sqrt(4),",",math.pi)

# popravi izračun

from math import *
def popravi_izračun_ostanek_in_koren_1():
    stevilo = float(input("Vnesi število: "))
    print('Ostanek števila', stevilo , 'pri deljenju z 2 je', stevilo % 2,".")
    print("Kvadratni koren števila", stevilo, 'je', sqrt(stevilo),".")

# samo pri izračunu deljeno, lahko spremenimo str v int. Pluse pustimo in glavno število !
# vejico smo dali med str+str+str in int % 2 in prav tako za....oblečemo v vejice
def popravi_izračun_ostanek_in_koren_2():
    stevilo = input("Vnesi število: ")
    print('Ostanek števila ' + stevilo + ' pri deljenju z 2 je', int(stevilo) % 2,".")
    print("Kvadratni koren števila " + stevilo + ' je', sqrt(float(stevilo)),".")

#     pazi, ne dati int pri sqrt ,ker bodo decimalke

def popravi_izračun_ploščine():
    a = float(input('Vnesi stranico a: '))
    b = float(input("Vnesi stranico b: "))
    print("Ploščina pravokotnka je", a * b,".")


def pitagorov_izrek():
    a = float(input("Vnesi stranico a: "))
    b = float(input("Vnesi stranico b: "))
    formula = sqrt(a**2 + b**2)
# moti me presledek pred piko na koncu!
    print("Hipotenuza je", formula, ".")

# Površina in prostornina oktaedra (uporabnik vnese podatke;
# formule za izračun so: P=2a**2 koren3,
# V=(a**3*koren2)/3)
def površina_in_prostornina_oktaedra():
    a = float(input("Vnesi stranico oktaedra: "))
    površina = 2*a**2
    volumen = (a**3*sqrt(2)/3)
    print("Površina oktaedera je:",površina)
    print("Volumen oktaedra je:",volumen)

# pazi navodilo! Izberi pravo formulo --> polmer in višina, ker je formul več!
# Volumen stožca (formula; uporabnik vnese polmer kroga in višino)
from math import *
def volumen_stožca():
    r = float(input("Vnesi polmer kroga: "))
    v = float(input("Vnesi višino kroga: "))
    volumen_stožca = 1/3*pi*r**2*v
    print("Volumen stožca je", volumen_stožca, ".")

# pretvori iz kotne stopinje v radiane in konstanta je 9.8!
# Domet izstrelka (izračuna se po naslednji formuli
# (g = gravitacijska konstanta, alfa = kot izstrelka, v0 = hitrost): podatke vnese uporabnik
def domet_izstrelka():
    g = float(input("Vnesi gravitacijsko konstanto: "))
    alfa = float(input("Vnesi alfa spremenljivko: "))
    hitrost_vo = float(input("Vnesi hitrostno spremenljivko: "))
    formula_dometa = (hitrost_vo**2*sin(2*radians(alfa)))/g
    print("Domet izstrelka je:",formula_dometa,".")

# ali import math in vsakič math.sin ali math.pi
# ali pa from math import * (all) in vse je nameščeno. Tipkamo samo pi() ali sin().

def plaža_ankaran():
    ura = int(input("Koliko ur smo se danes kopali? "))
    print("To je to, saj " ,ura, " ur kopanja je mnogo :).")


def hiptenuza():
    a = float(input("Vnesi stranico a: "))
    b = float(input("Vnesi stranico b: "))
    hipotenuza = sqrt(a**2+b**2)
    print("Hipotenuza je", round(hipotenuza,1),".")

    # zaokroži rezultat z roundloat

def oktaeder_round():
    a = float(input("Vnesi stranico a: "))
    oktaeder_ploščina = 2 * a**2 * sqrt(3)
    oktaeder_volumen = (a ** 3 * sqrt(2))/3 #ali 1/3 * a ** 3 * sqrt(2)
    print("Površina oktaedra je",round(oktaeder_ploščina,1))
    print("Volumen oktaedra je", round(oktaeder_volumen, 1))

# pri import math(namesto from math import *) je koda bolj jasna, saj je pri vsaki vrstici razvidna vrsta knjižnice
# Uporaba import * v programih python velja za slabo navado, ker na ta način onesnažujete
# svoj imenski prostor , stavek import * uvozi vse funkcije in razrede v vaš imenski prostor,
# kar je lahko v nasprotju s funkcijami, ki jih definirate, ali funkcijami drugih knjižnic,
# ki jih uvozi. Smiselno je uporabit all, če j ekratka koda z eno knjižnico.


# avtomatski izračun oktaedra z vrednstmi od 1 do 5. Brez vnosa iz strani uporabnika.
def oktaeder_volumen_avtomat():
    a = (1, 2, 3, 4, 5)
    for a in a:
        oktaeder_volumen = (a ** 3 * sqrt(2))/3 #ali 1/3 * a ** 3 * sqrt(2)
        print("Volumen oktaedra je", round(oktaeder_volumen, 1),".")


# !!!!!!!!!!!!! FUNKCIJE - USTVARJANJE LASTNIH FUNKCIJ

def oktaeder_volumen_z_returnom(a):
    volumen = (a ** 3 * sqrt(2)) / 3  # ali 1/3 * a ** 3 * sqrt(2)
    return volumen #brez return ne deluje in se ne ponavlja
# funkcije in knjižnice se ne izvajajo, dokler jih ne pokličemo!

v1 = oktaeder_volumen_z_returnom(1)
v2 = oktaeder_volumen_z_returnom(2)
v3 = oktaeder_volumen_z_returnom(3)



"""
def oktaeder_ploščina(a):
    ploščina = 2 * a**2 * sqrt(3)# lahko damo direkt return, brez ploščine 2krat --> return = 2 * a**2 * sqrt(3)
    return ploščina

p1 = oktaeder_ploščina(1)
p2 = oktaeder_ploščina(2)
p3 = oktaeder_ploščina(3)

print(p1)
print(p2)
print(p3)

"""

# Python library is a collection of modules that contain functions and classes
# that can be used by other programs to perform various tasks.

# Brez vmesnika oziroma posrednika/dodelitve (spremeljivk) ploščina
def oktaeder_ploščina(a):
    return 2 * a**2 * sqrt(3) #return brez =!

# v mapi main je import mapa začetek, nato začetek.ime funkcije

# knjižnica = direktorij/imenik/mapa




"""
# import knjižnice matplot in izvršba modula graf

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
np.random.seed(3)
x = 2.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

# plot
fig, ax = plt.subplots()

ax.step(x, y, linewidth=2.5)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
"""

#!!!!!!!!!!!!!!!! IF - POGOJNI STAVKI !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# boolean - četrti podatkovni tip (integer, float, string in boolean)
def primerjalni_operator():
    print(100<40)
    print(type(True)) #true mora biti z veliko začetnico, ker je rezervirana. Z malo ne registrira
    print(1==2) #dvakrat = =, ker je en enačaj rezerviran za prireditveni operator za spremenljivke in funkcije
# primer A = 5 (a- ju priredimo/postane 5)

def dodelimo_in_preverimo_kaj_je_v_spremenljivki_a():
    a = 5 # prireditveni/dodelitveni operator
    print(a!=4) #preverba za a ni 4
    print("Ana"<"Brina") #primerjalni operator razvršča po abecedni vrsti-naraščajoče

def primerjava():
    a = 5
    primerjava = a <= 100 #najprej menjše, nato je enako
    print(primerjava)

def prazno(x):
    print(x)


def starost():
    starost = int(input("Vnesi svojo starost: "))
    if starost >= 18:
        print("Izvolite vstopiti.")
    else: #Brez else, v nasprotnem primeru, ne bo ispisalo ničesar!Else je torej poljuben oziroma
          #za čisto kodo
        print("Ker niste polnoletni, je  Vaš vstop v bazo prepovedan!")

# Debugger omogoča izvajanje programa korak po korak (kot pyton tutor)

# LOGIČNI 3 OPERATORJI: AND ali OR ali NOT

def vojaški_obveznik_or(): # kontra od if --> IZJAVE!
    starost = int(input('Kolišna je Vaša starost? ')) # Ne poozabi določit spremenljivko oziroma input!
    if starost <= 18 or starost == 60:  #pri logiki/logični operator and, obvezno navedi dvakrat ime spremeljivke
                                        # ali if 18 >= starost < 60:
                                        # dva enačaja!!!!!!!!!!
        print("Ste vojaški obveznik!")
    else:
        print("Niste vojaški obveznik.")

# Krajšnica --> if 18 >= starost < 60:
#v obeh primerih je vojaški obveznik
#primerjalni operator nad logičnimi

def vojaški_obveznik_premlad_obveznik_prestar():
    starost = int(input("Kolikšna je Vaša starost? "))
    if starost >=18 and starost <60:
        print("Ste vojaški obveznik. ")
    elif starost < 18:
        print("Hvala, vendar ste premlad. ")
    else:
        print("Hvala, vendar ste prestar.")
# več od 60 --> starost >= 60:
# elif je lahko mnogo, else pa samo eden-zadnji!
# elsa nima primerjave!

def not_false(): # Obratna izjava
    print(not False)

# NAVODILA:
# Članstvo v VIP klubu pridobi vsak član mimovrste=), ki v tekočem koledarskem letu opravi:
# vsaj 10 zaključenih nakupov v minimalni vrednosti posameznega nakupa 50 € ali
# skupno vrednost zaključenih nakupov za 800 €.

def članstvo_vip_mimovrste():
    nakup = float(input("Koliko nakupov ste opravili v tekočem letu? "))
    vrednost_nakupa = float(input("Ali je bila vrednost vsakega nakupa večja od 50 evrov? "))
# še lažje --> nakup_nad_50_evrov = int(input("Koliko nakupov nad 50 evrov imaš? ")
    skupna_vrednost = float(input("Kolikšna je bila skupna vrednost vseh nakupov? "))
    if nakup >= 10 and vrednost_nakupa >=50 or skupna_vrednost >=800:
        print("Vi ste naš V.I.P. član.")
    else:
        print("Žal niste član V.I.P., ker ne dosegate nakupne norme. ")

def članstvo_vip_mimovrste_šolska():

    nakup_nad_50_evrov = int(input("Koliko nakupov nad 50 evrov imaš? "))
    skupna_vrednost = float(input("Kolikšna je bila skupna vrednost vseh nakupov? "))
    vip = nakup_nad_50_evrov >= 10 or skupna_vrednost >=800

    if vip:  # if vip == True
        print("Vi ste naš V.I.P. član.")
    else: # ali if not vip:
        print("Žal niste član V.I.P., ker ne dosegate nakupne norme. ")

#????Kako narediti odgovor boolean true or false???


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Z A N K E !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# importiraš
# random knjižnico in izbereš modul randint
import random # ali from random import *
def metanje_kocke():
    for i in range(1,6):
         print(random.randint(i,6))
# ali
#while ponavlja, for gre skozi
def metanje_kocke_šolska():
    kocka = 0 #pazi, najprej je variabla 0.
    while kocka != 6: # pazi: dokler kocka ni 6 meči kocko!
        kocka = random.randint(1, 6) #nato random
        print(kocka)
# tukaj ne potrebujemo break!

# dodamo števec metov
# ustvarimo pred vstopom v zanko in ustvarimo začetne vrednosti --> 0




def metanje_kocke_šolska_s_števcem_metov():
    kocka = 0
    #global števec_metov # LAHKO DODAMO GLOBALNO SPREMENLJIVKO, DA JO LAHKO POKLIČEMO IZVEN FUNKCIJE
                        # VENDAR MORAMO NAJPREJ POKLICATI FUNKCIJO, DA JO ZAZNA, TAKO DA NE
                        # POTREBUJEMO GLOBALNE SPREMENLJIVKE!
    števec_metov = 0
    while kocka != 6: # while je dokler

        kocka = random.randint(1,6)
        števec_metov = števec_metov + 1


        print("Padla je številka " + str(kocka) + ".") # pri plus je  pika na mestu,
                                                       # vendar moramo številko spremeniti v int
    print("Kocka je padla",števec_metov,"krat.") # ! enostavno daš v pravilno indentacijo in print števec pride na konec!



# Koliko zaporednih pozitivnih celih števil lahko seeštejem, da ne presežem števila 100?
# (predavanje 2.3 - 16 min)
"""  NAROBE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def števila_do_100():
    rezultat = int(0)
    count = int(0)
    število in range(1,101)
    while rezultat !=100: #pazi, samo do 100, ker rezultat doda še eno
        rezultat = število + (število + 1)
        count = count + 1
        print("Rezultat je ", rezultat,".")
    print("Lahko seštejemo ",count," števil.")
"""

def števila_do_100(): #naredi načrt/skico
    #1+2 = 3    ali    1, 1+2, 1+2+3
    #2+3 = 5
    #3+4 = 7
    število = 0
    vsota = 0
    count = 0
    # pred vstopom v zanko VEDNO POSKRBIM ZA ZAČETNE VREDNOSTI/ŠTARTNE VREDNOSTI!!
    # ANALOGIJA S PRODAJO KART --> PREDEN PRODAJAŠ KARTE, MORAŠ VEDETI KOLIKO SI JIH ŽE PRODAL..
    while vsota < 101:
            število = število + 1 #število = število + 1
            vsota = vsota + število
            count = count + 1


#ker števec v  zanki sešteje še eno vsoto, ji moramo obvezno v printu eno odšteti!
            # ?ali lahko to storimo že v kodi?
    print("Lahko seštejemo",count - 1,"zaporednih števil",".")
    #daš indent pod while, da izpiše samo na koncu!

# !!!!!!!!!!!!!!!!!!!!!!NIZ (ang. string)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def pošta():
    kraj = "Maribor "# damo presledek
    #kraj[0] = "M" #spremeni črko (velikost)-->LIST ne dovoli sprememb
    # zbirka/seznam dovoli spremembe
    print(kraj[:]) #printa od 0
    print(kraj[0])
    print(kraj[-1])
    print(kraj[-2])
    print(kraj[:6])
    print(kraj[:])

    print(type(kraj)) #preveri tip spremenljivke
    print("3000 " + kraj)


    # !!!!!!!!!!!!!!!!operator za preverjanje IN --> pripadnost nizu
    # to je koda za search v GUI vmesniku
    print("a" in kraj)
    print("m" in kraj) #pazi navednice + velika začetnica
    print("l" in kraj)

def poljubno_za_IN():
    print("Mes" in "Novo Mesto")

# DOLŽINA NIZA --> LENGHT --> LEN
# MIN
# MAX

def dolžina_niza():
    kraj = "Koper"
    print(len(kraj))
    print(len("Paradižnik"))

def vgrajena_funkcija_min_in_max():
    kraj = "Koper"
    print(min(kraj)) # min = prva črka po abecedni vrsti. Velike črke imajo prednost
    # najprej velike in nato majhne.
    # prva bi bila e, vendar imajo velike črke prednost --> Velike in male črke
    print(max(kraj)) # max = zadnja črka po abecedi
    print("a" in "Alabama") # in je z malo
    #?? Kako najti koliko črk je v nizu..find?

#REZINE = PODNIZI
# !!! TUKAJ JE POTRBNO PAZITI NA KONEC DOLOČITVE, KJER JE EDEN ZNAK MANJ !!!
# Znak se ustavi pred navedeno številko !!!!
def rezine_podnizi():
    živilo = "Kruh"
    print(živilo[0:3:2]) # niz[začetek niza, konec niza, inteval/preskok]
    print("Banana"[2:4]) # interval je poljuben
    print("Banana"[0::2])# vsak drugi znak
    print("Banana"[::-1]) # obrnjen niz
    #obrnjen niz
    print("Banana"[-6:])
    #ali
    print("Banana"[0:7])
    #ali
    print("Banana"[0:])

def izpiši_prve_tri_znake():
    print("Mississippi"[0:3]) # prve tri so 0,1,2
        # ali
    print("Mississippi"[:3])

# Mississippi -->   0,  1, 2, 3, 4, 5, 6, 7, 8, 9,10
# ali
# Mississippi --> -11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1 (ena več, ker ni ničle)
def datum_izpis_realna_uporaba():
    datum = "06.12.2021"
    print("Leto je "+ datum[6:]+".")
    #ALI
    leto = datum[6:] # nova spremenljivka
    print(type(leto)) # tukaj je tip niz (string)
    leto = int(datum[6:])
    #odražem niz in oblečem v številko za nadaljnje upravljanje s številkami
    print(leto) # tukaj je tip cele številke (integer)
    print(type(leto))

    mesec = datum[3:5] #normal
    #ali
    mesec = datum[-7:-5] #nazaj
    #???????????ali obrnjen niz / REKURZIJA


    print(mesec)
    #ali
    print(datum[-4:])
    #ALI
    #obrnjen niz?

def timestamp():#časovni žig/znak
# ime funkcije ne more biti enako njeni spremenljivki
    ts = "06.12.2021 18:23:21"
    #sortiraj v sremenljivko datum in čas
    datum = ts[0:11]
    #ali
    datum = ts[-19:-9]
    čas = ts[-8:]
    print(datum)
    print(čas)


""" MIMI
import datetime

def live_date():
    print(datetime.date.today())

def kocka_avtomat():
    number = 0
    while number != 6:
        number = random.randint(1, 6)
        print(number)
def kocka_ročna():
    number = random.randint(1,1000000)
    print(number)

def random_choice():
    izbor = random.choice(["oh","oijiojoj","oijojoi"])
    print(izbor)

"""
def in_v_stavku_if():
    if "f" in "Alabama": # ali not if
        print("OK.")

    else:
        print("A ni v nizu.")

# DOMAČA NALOGA 1
#1.Izračun indeksa telesne mase
# (formulo za izračun; uporabnik poda vse potrebne vhodne podatke)
# ITM = telesna masa (kg) / višina2 (m2)

def DN1_izračun_indexa_telesne_mase():
    teža = float(input("Prosim vnesite vašo težo v kilogramih: "))
    višina = float(input("Prosim vnesite vašo višino v metrih: "))
    formula = teža/višina**2
    print("Index Vaše telesne mase je:",str(formula) + ".")

#2.Izračun in površina platonskih teles (tetraeder, ikozaeder, ...). Podatki na wikipediji.
# Program naj povpraša uporabnika po dolžini stranice, nato izračunate vse veličine in izpišete na zaslon.
import math
def DN1_2_površina_platonskih_teles():
    a = float(input("Kolikšna je dolžina stranice lika  v centimetrih? "))
    površina_tetraedra = a**2 * math.sqrt(3) # natančen zapis --> čista koda
    površina_heksaedra = a**3
    površina_oktaedra = 2 * a**2 * math.sqrt(3)
    površina_dodekaeder = 3 * math.sqrt(25 + 10 * math.sqrt(5)) * a**2
    površina_ikozaedre = 5 * a**2 * math.sqrt(3)

    print("Površina tetraedra z dolžino stranice",a,"cm je",str(površina_tetraedra) + " cm.")
    print("Površina heksaedra z dolžino stranice",a,"cm je",str(površina_heksaedra) + " cm.")
    print("Površina oktaedra z dolžimo stranice",a,"cm je",str(površina_oktaedra) + " cm.")
    print("Površina dodekaedra z dolžino stranuce",a,"cm je",str(površina_dodekaeder) + " cm.")
    print("Površina ikozaedra z dolžino stranice",a,"cm je",str(površina_ikozaedre) + " cm.")


