"""
#...nadaljevanje ZAČETEK_1
# PREDAVANJE 3
# NALOGE ZA VAJE 2:

# 1.Vadba poštevanke: računalnik si naključno izmisli dve celi števili na intervalu od 1 do 10. Nato vas povpraša, koliko je rezultat. Vaš vnos nato preveri in vam odgovori, če ste pravilno odgovorili.
# 2.Program vas povpraša po višini in teži. Nato vam izračuna in izpiše indeks telesne mase (ITM) ter poda diagnozo. Napišite funkcijo za itm: itm(teza,visina).
# 3.Program vas povpraša za poljubno letnico in vi mu odgovorite ali je leto prestopno ali ne. Kriterij za prestopno leto je tukaj.
# 4.Ugotovite, do katere velikosti stranice je volumen oktaedra manjši od 500 cm3 (začnite pri stranici a = 1 in povečujte).
# 5.Program naj uporabnika povpraša po temperaturi vode in po enotah (celzij, fahrenheit, kelvin). Pri enotah uporabnik lahko vnese velike črke C, F, K. Nato program izpiše v kakšnem agregatnem stanju je voda.
# 6.Izračun zaslužka: program vas povpraša po številu opravljenih ur v mesecu, po številu delovnih dni v mesecu in po ceni ure. Nato vam izpiše, koliko je normativ delovnih ur v mesecu in kolikšno plačilo vam pripada. Upoštevajte, da se nadure plačajo 20% več kot običajne ure. Če ste prekoračili mejo 20 nadur, naj vas opozori, da ste prekoračili priporočeno mejo.
# 7.Uporabnik vnese EMŠO, vi pa izpišete njegov datum rojstva in spol. Napišite funkcije za izpis datuma rojstva, letnico in spol (se pravi 3 funkcije).
"""


def vaje2_1_dve_števili_ponovi():
    naključno = random.randint(1,10)
    naključno2 = random.randint(1,10)
    print(naključno)
    print(naključno2)
    vprašanje1 = float(input("Kolikšen je prvi rezultat? "))
    vprašanje2 = float(input("Kolikšen je drugi rezultat? "))
    if vprašanje1 == naključno and vprašanje2 == naključno2 : #pazi je enako = =
        print("Vaš odgovor je pravilen.") #pazi indent
    else:
        print("Vaš odgovor je žal nepravilen.")

        #ali z izračunom vsote

# izračunaj vsoto ali zmnožek(odvisno od natančnosti navodil)
def vaje2_1_dve_števili_izračunaj_vsoto():
    naključno = random.randint(1, 10)
    naključno2 = random.randint(1, 10)
    print("Imamo števili",naključno, "in", str(naključno2) + "?")
# lahko damo rezultat tudi sem--> rezultat_vsota = naključno + naključno2
    vprašanje = float(input("Kolikšna je vsota? "))
    rezultat_vsota = naključno + naključno2 #uporabniku neviden.Če zmnožek -> naključno * naključno2

    if vprašanje == rezultat_vsota:  # pazi je enako = =
        print("Vaš odgovor je pravilen.")  # pazi indent
    else:
        print("Vaš odgovor je žal nepravilen. Pravilen odgovor je " + str(rezultat_vsota) + ".")
        # vedno naredi presledek na koncu dodane besede

def vaje2_2_indeks_telesne_mase():
    teža = float(input("Kolikšna je Vaša telesna teža v kg? "))
    višina = float(input("Kolikšna je Vaša višina v m? "))
    indeks_telesne_mase = teža / višina ** 2
    print("Na podlagi vaših podatkov je indeks Vaše telesne mase",str(indeks_telesne_mase) + " kg/m**2")

def vaje2_3_prestopno_leto():
    letnica = random.randint(0000,2022)
    print(letnica)
    #Leto je prestopno, če je deljivo s 4, razen ...
    #... v primeru, da je leto deljivo s 100, leto ni prestopno, razen ...
    #... v primeru, da je leto deljivo s 400, leto je prestopno.

    if letnica%4==0  or letnica%400==0: # pazi na znak za ostanek, kjer ostanka ne sme biti!!!
        print("Leto je prestopno.")
    elif letnica%100==0 and letnica%400==0:
        print("Leto ni prestopno.")
    else:
        print("Leto ni prestopno.")

# 4.Ugotovite, do katere velikosti stranice je volumen oktaedra manjši od 500 cm3 (začnite pri stranici a = 1
def vaje2_4_oktaeder_manjši_od_500():
    a = int(range(1,100))
    volumen = int(a) ** 3 * math.sqrt(2) / 3
    for a in a:
        while volumen < 500:
            print(a)

# 5.Program naj uporabnika povpraša po temperaturi vode in po enotah (celzij, fahrenheit, kelvin).
# Pri enotah uporabnik lahko vnese velike črke C, F, K. Nato program izpiše v kakšnem agregatnem stanju
# je voda.
def vaja2_5_agregatno_stanje():
    vprašanje = float(input("Kolikšna je temperatura vode v stopinj Fahrenheit? "))
    celzij = round((vprašanje -32) * 5/9,2) #round zaokroži in ima 2 parametra(self in koliko decimalk)
    print(vprašanje, " Fahrenheitov je",celzij,"stopinj celzija.")
    if celzij>0 and celzij < 100\
            :
        print("Agregatno stanje je tekoče oziroma vodno.")
    elif celzij <= 0: #manjše ali enako
        print("Agregatno stanje je trdo oziroma ledeno.")
    else: #else ima dodatnih parametrov
        print("Agregatno stanje je plinasto oziroma vre.")

#VPRAŠANJE NA IZPITU__> INDENTACIJA IF, DEF,.... = SINTAKSA( namesto oklepajev je indentacija

#napiše narobe - else, ker razume kot string in ne številko. Zato odgovor oblečemo v številko.
#Za izračun ševilk, pa oblešemo v int --> VENDAR STR NE MOREMO OBLEČI V INT!

def if_vaja():
    odgovor = int(input("Vnesi številko od 1 do 5: "))
    if odgovor == 1:
        print("ena")

    elif odgovor == 2:
        print("dva")
    elif odgovor == 3:
        print("tri")
    elif odgovor == 4:
        print("štiri")
    elif odgovor == 5:
        print("pet")
    else:
        print("prevelika številka")

def vprašanje_drugače():
    #to je operacija seštevanja nizov(string), kjer morajp biti vsi enakega tipa
    vprašanje = "Koliko " + "je " + str(1) + "+" + str(8) + "? " # plus je posebej

# Lahko napišemo -> odgovor = int(input(vprašanje))
# in nato -> if odgovor == 9
    if int(input(vprašanje)) == 9:
        print("true")
    else:
        print("false")#!!!narekovaji!--> če ne ne registrira


#Če sta 2 možni poti, uporabimo le if in else. Za 3 pa uporabimo še elif (fi, elif, else).
# Niz je v programiranju beseda(Niz dobesedno pomeni v prevodu "majhni koščki", kar so tudi številke)


#import iz druge datoteke
# VSE->from ZAČETEK_1_PREDAVANJA_1_IN_2 import * -> kličeš samo ime funkcije (vendar nepregledno)
# KOS->import ZAČETEK_1_PREDAVANJA_1_IN_2 -> kličeš-> ZAČETEK_1_PREDAVANJA_1_IN_2.ime funkcije (pregledno)
import PYTHON_ZAPISKI_PREDAVANJI_1_IN_2 #brez končnice datoteke, le glavo knjižnice
#ali
from PYTHON_ZAPISKI_PREDAVANJI_1_IN_2 import * #vse funkcije
#ali pa našteješ

from PYTHON_ZAPISKI_PREDAVANJI_1_IN_2 import volumen_stožca

def indeks_telesne_mase_itm_ponovitev():
    višina = float(input("Kolikšna je vaša višina v metrih? "))
    teža = float(input("Kolikšna je vaša teža v kg? "))
    formula_itm = teža/višina**2
    print("Indeks Vaše telesne mase je " + str(formula_itm))

#??kako pogledati kodo poklicane funkcije?

#raje piši float kakor int, razen v primeru, ko želimo omejitve na celo število pri vnosu
def indeks_telesne_mase_ponovitev2():
    višina = float(input("Kolikšna je Vaša višina v metrih? "))
    teža = float(input("Kolikšna je vaša teža v kilogramih? "))
    formula_itm = round(teža/višina**2,2) #zaokroži na dve decimalki
    print("Indeks Vaše telesne mase je " + str(formula_itm) + " kg/m2.")
    #ali
    print("Indeks Vaše telesne mase je",formula_itm,"kg/m2.")
#delaj presledke na koncu ali začetku besed!

def indeks_telesne_mase_metri_v_centimetre():
    višina = float(input("Kolikšna je Vaša višina? "))
    višina_metri = višina/100 #pretvorili smo cm v m...ali v rezultatu damo deljeno 100
    teža = float(input("Kolikšna je vaša teža v kilogramih? "))
    formula_itm = round(teža/višina_metri**2,2) #zaokroži na dve decimalki
    print("Indeks Vaše telesne mase je " + str(formula_itm) + " kg/m2.")
    #ali
    print("Indeks Vaše telesne mase je",formula_itm,"kg/m2.")
#če se vnos višine v metrih ne spodobi, naredimo pretvorbo: ali z novo spremenljivko, ali v formuli

def indeks_telesne_mase_metri_v_centimetre_profesorjeva_izbira(): #sprotna sprememba v formuli
    višina = float(input("Kolikšna je Vaša višina? "))
    teža = float(input("Kolikšna je vaša teža? "))

    formula_itm = round(teža/(višina/100)**2,2) #zaokroži na dve decimalki

    print("Indeks Vaše telesne mase je " + str(formula_itm) + " kg/m2.")
    #ali
    print("Indeks Vaše telesne mase je",formula_itm,"kg/m2.")
#profesorjeva izbira je napačna, ker uorabnik ne ve v kateri enoti naj vnese podatke!

#RETURN IN POVEZAVA index(a,b) --> poljubno = index(asociacija za a, asociacija za b)
#???seveda je lažje obleči vse v def, ampak profesor je tako želel



def funkcija_v_funkciji(): #sem dal sam, ker bi moral zakomentirat
    def funkcija_za_index(t, v):
        return round(t / (v / 100) ** 2, 2)#tukaj smo zaokrožili in spremenili cm v m!!

    # katera python avtomatsko povezuje "hard link"
    teža = float(input("Kolikšna je Vaša teža v kilogramih? "))
    višina = float(input("Kolikšna je Vaša višina v centimetrih? "))
    moj_itm = funkcija_za_index(teža, višina)  # tukaj smo dali različni imeni za dva parametra,
    # prej definiramo seveda imena spremenljivk
    print("Vaš indeks telesne mase je ", moj_itm)

    #namesto else lahko damo diagnozo kot spremenljivko --> diagnoza = " Debelost tretje stopnje"
    #dodamo še diagnozo, po določitvah - http//ITM wikipedija
    if moj_itm <=16: #pazi na pravilen predznak!!!
        print("Ste hudo nedohranjeni.")
    elif moj_itm > 16 and moj_itm < 17: #lahko tudi samo --> moj_itm < 17, ker se sam zaustavi pri =16!!
        print("Zmerna nedohranjenost.")
    elif moj_itm >=17 and moj_itm < 18.5: #pazi na večje ali enako zaradi zajetja vseh števil,
        # saj se lahko zgodi, da bo sortacija 17 napisala pod else (debelost)!!!!!
        print("Blaga nedohranjenost.")
    elif moj_itm > 18.5 and moj_itm < 25:
        print("Imate normalno telesno maso.")
    elif moj_itm > 25 and moj_itm < 30:
        print("Imate zvečano telesno maso.")
    elif moj_itm > 30 and moj_itm < 35:
        print("Debelost prve stopnje.")
    elif moj_itm > 35 and moj_itm < 40:
        print("Debelost druge stopnje.")
    #else :# else nikoli nima parametrov!!!!
    # else raje ne damo, če želimo biti brez skrbi!!!!
    else:# ali natannčneje -> elif moj_itm >= 40:
        print("Imate debelost tretje stopnje.")

#Lahko bi tudi dali diagnoza kot spremenljivko in jo nato klicali.....print(diagnoza)
def funkcija_v_funkciji_diagnoza_v_spremenljivki(): #sem dal sam, ker bi moral zakomentirat
    def funkcija_za_index(t, v):
        return round(t / (v / 100) ** 2, 2)#tukaj smo zaokrožili in spremenili cm v m!!

    # katera python avtomatsko povezuje "hard link"
    teža = float(input("Kolikšna je Vaša teža v kilogramih? "))
    višina = float(input("Kolikšna je Vaša višina v centimetrih? "))
    moj_itm = funkcija_za_index(teža, višina)  # tukaj smo dali različni imeni za dva parametra,
    # prej definiramo seveda imena spremenljivk
    print("Vaš indeks telesne mase je ", moj_itm)
    #dodamo še diagnozo, po določitvah - http//ITM wikipedija
    if moj_itm <=16: #pazi na pravilen predznak!!!
        diagnoza = "ste hudo nedohranjeni."
    elif moj_itm > 16 and moj_itm < 17:
        diagnoza = "zmerna nedohranjenost."
    elif moj_itm >=17 and moj_itm < 18.5: #pazi na večje ali enako zaradi zajetja vseh števil,
        # saj se lahko zgodi, da bo sortacija 17 napisala pod else (debelost)!!!!!
        diagnoza = "blaga nedohranjenost."
    elif moj_itm > 18.5 and moj_itm < 25:
        diagnoza = "imate normalno telesno maso."
    elif moj_itm > 25 and moj_itm < 30:
        diagnoza = "imate povečano telesno maso."
    elif moj_itm > 30 and moj_itm < 35:
        diagnoza = "debelost prve stopnje."
    elif moj_itm > 35 and moj_itm < 40:
        diagnoza = "debelost druge stopnje."

    #else :# else nikoli nima parametrov!!!!
    # else raje ne damo, če želimo biti brez skrbi!!!!
    else:# ali natannčneje -> elif moj_itm >= 40:
        diagnoza = "debelost tretje stopnje."
    print("Vaša diagnoza je",diagnoza) #print za celoten if stavek podaš/indentiraš v vrstico definicije,
    # ker je poglaviten print

def vaja_3_prestopna_letnica():# nekaj ni v redu, ker leto 500 se ne ujema s šolsko verzijo!
    poljubna_letnica = int(input("Vnesite poljubno letnico: "))
    # wiki :Leto je prestopno, če je deljivo s 4, razen ...
    # ... v primeru, da je leto deljivo s 100,leto ni prestopno, razen ...
    # ... v primeru, da je leto deljivo s 400, leto je prestopno.
    if poljubna_letnica%4 == 0 and poljubna_letnica %100 != 0 or poljubna_letnica%400 == 0 :
        print("Leto je prestopno.")

 #ker upošteva pogoj v prvem izrau, ne zazna drugega, zato moramo narediti po šolsko!!!!
#vsi pogoji v enem izrazu!!!
        # narobe....elif poljubna_letnica%100 == 0 and poljubna_letnica%400 != 0:
        # narobe....print("Leto ni prestopno.")
# primerjalnim operatorjem smo dodali še logične operatorje
    else: #obvezno else za enako letnico
        print("Leto ni prestopno.")
#dodelitev je =, primerjava je = =

def vaja_3_šolska_prestopno_leto_vsi_pogoji_v_enem_izrazu():
#Logical operators have operator precedence the same as other operators (relational, arithmetic, etc.).
# highest precedence belongs to not , followed by and , and finally by or .
#!!!!IZPIT!!!LOGIČNI OPERATORJI: not, and, or!!!!!
    # wiki :Leto je prestopno, če je deljivo s 4, razen ...
    # ... v primeru, da je leto deljivo s 100,leto ni prestopno, razen ...
    # ... v primeru, da je leto deljivo s 400, leto je prestopno.
    poljubna_letnica = int(input("Vnesite poljubno letnico: "))
    prestopno = ((poljubna_letnica % 4 == 0) and (poljubna_letnica % 100 != 0)) or (poljubna_letnica % 400 == 0)

    if prestopno:
        print("Leto je prestopno.")
    else:
        print("Leto ni prestopno.")

from math import *
def oktaeder_moja():
    # pri kateri stranici je volumen oktaedra manjši od 500? Začni pri 1, cela števila in izpiši volumen.
    # V=a**3 * sqrt(2)/3

    #1. najprej določimo neznanke...a,V
    #2. nato napišemo način izračunavanja...while
    #3. nato povečujemo spremenljivko(neznanko)
    #4. na koncu ponudimo izpis za uporabnika

    a = 1 #1.
    V = 0


    while V < 500: #2.
        V = a ** 3 * sqrt(2) / 3 #3.
        a = a + 1 #4.
        if V < 500: #zaradi zaustavitve pred 500 smo dodali pogojni stavek pred printom
            print("Za stranico", a, " je volumen kvadra", str(round(V,2)) + ".") # 5.
#!!!!!!!!!!STRING JE SAMO; KO SE Z INPUTOM JEMLJE!!!!!!!!!!!
def oktaeder_šolska(): # zaustavitev brez if stavka
    a = 1  # 1.
    V = a ** 3 * sqrt(2) / 3

    while V < 500:
        #zaradi zaustavitve pred 500 smo dal print po while in za printom povečanja
        print("Za stranico", a, " je volumen kvadra", str(round(V, 2)) + ".")
        a = a + 1  # 4.
        V = a ** 3 * sqrt(2) / 3


def oktaeder_šolska_z_importirano_funkcijo_in_returnom():
    def formula_volumen_oktaedra(a):
        return a ** 3 * sqrt(2) / 3
    a = 1
    volumen = formula_volumen_oktaedra(a)
    while volumen < 500:
        print(a,round(volumen,1
                    ))
        a = a + 1
        volumen = formula_volumen_oktaedra(a)

        #RETURN NAREDI FUNKCIJO ŽIVO IN ZAHTEVA SPREMENLJIVKO!!!!!!!!
#return se ne vidi, ker return ni funkcija, kot print. Return je vrednost!
def živa_funkcija_return(x):
    return x + 2 #variabla dobi vrednost od funkcije
#print(živa_funkcija_return(1))

#ali

def funkcija_samo_print():
    #ali x = int(input())
    # print(x+2)
    print(int(input())+2)

#oziroma

def funkcija_print_z_x():
    print(1 + "") #pokliče iz oklepaja prazen znak
                 #funkcija ima print funkcijo v njej

def vaja_7_EMŠO():#DDMMYYYRRSCCC(datum,mesec,leto,regija,spol,kontrolne številke)

    #NAVODILA: Uporabnik vnese EMŠO, vi pa izpišete njegov datum rojstva in spol.
    # Napišite tri funkcije za izpis datuma rojstva, letnico in spol
    EMŠO = input("Vnesite Vaš EMŠO: ") #1311979500970 mesto 9 --> 0 = moški, 5 = ženska
    def tisočletje(): #funkcija v funkciji, kadar ne želimo, da se takoj vidi, ampak nekje drugje
        tisočletje = EMŠO[4]
        if tisočletje in ("7", "8", "9"):#!!!raje daš pod else, ker zajame vse ostale
            return "1"
        elif tisočletje == "0":
            return "2"

    print("Vaš datum rojstva je: ", EMŠO[0:2], ".", EMŠO[2:4], ".", str(tisočletje()) + EMŠO[4:7])
#[0:2] ali [:2]
    #??????if EMŠO[9] == ["0","1","2","3","4"]: kako narediti list
    if EMŠO[9] in ("0","1","2","3","4"): #tako se izognemo ponavljanju logičnega operatorja or
        #LAHKO KOT LIST ALI KOT INDEX () ali [] ali OR
    #if EMŠO[9] == "0" or EMŠO[9] == "1" or EMŠO[9] == "2" or EMŠO[9] =="3" or EMŠO[9] == "4":#obvezno daš kot string, saj je input vedno string in ne registrira
        #ali pa zrihtaš prej v int
        print("Ste moškega spola.")
    #DOLOČIMO ZA VSE MOŽNOSTI POGOJA.KER JE STRING NE MOREMO DATI RANGE

    elif EMŠO[9] in ("5","6","7","8","9"):
    #elif EMŠO[9] == "5" or EMŠO[9] == "6" or EMŠO[9] == "7" or EMŠO[9] == "8" or EMŠO[9] == "9":
        print("Ste ženskega spola.")
    else:
        print("Vaš spol je nedoločen.")
#pozabil si kriterij za letnico-->tisočico (1000 ali 2000), saj nekateri so rojeni v 2000!!!!
#emšo je seveda kot string
"INDEX/SEZNAM IMA DVOPIČJE"
def prvi_simboli():
    x = "12345"
    print(x[1:3])

def vaja_7_EMŠO_s_funkcijo():
    def datum_rojstva(x):
        return x[0:2]
def seštevamo_index():
    print("avto"[0+2])
def INDEX_VEDNO_KOT_STRING():
    print("1234"[2])
#rezine

def vaja_7_EMŠO_ŠOLSKA():
    def datum_rojstva(EMŠO):
        if EMŠO[4] == "0":
            return EMŠO[0:2] + "." + EMŠO[2:4] + "." + "2" + EMŠO[4:7]
        else:
            return EMŠO[0:2] + "." + EMŠO[2:4] + "." + "1" + EMŠO[4:2]
    #načrt: DDMMYYYRRSCCC -->13 števk
    #index začne z 0 1 2 3 4 5 6 7 8 9 10 11 12
    EMŠO = input("Vpišite svoj EMŠO: ")
    dan = EMŠO[0:2]#ali [:2]
    mesec = EMŠO[2:4]
    leto = EMŠO[4:7]

    if EMŠO[4]== "0": #!!ne pozabi indexa!!!
        leto = "2" + leto
    else:#kar else za vsa ostala števila
        leto = "1" + leto
#spotoma smo spremenili-->pogojevali leto!!
    datum = dan + "." + mesec + "." + leto
    """
    def tisočletje_šolska():
        tisočletje = EMŠO[4]
        if tisočletje in ("7","8","9"):
            return 1
        elif tisočletje == "0":
            return 2

    leto = str(tisočletje_šolska()) + EMŠO[4:7]
    """
    print(datum)

    #pojdimo za spol
    #s pripadnostjo množici iz niza
    if EMŠO[9] in "01234":
        spol = "Moški"
    else:
        spol = "Ženski"
    print(spol)

    #še funkcija
    def datum_rojstva(EMŠO):
        if EMŠO[4] == "0":
            return EMŠO[0:2] + "." + EMŠO[2:4] + "." + "2" + EMŠO[4:7]
        else:
            return EMŠO[0:2] + "." + EMŠO[2:4] + "." + "1" + EMŠO[4:2]



    #ali s primerjalnim operatorjem
    if int(EMŠO[9]) <5: #string lahko pretvorimo v int in obratno, le računati (razen plusa) ne moremo
        spol = "Moški"

    else:
        spol = "Ženski"
    print(spol)

    # ali s primerjalnim operatorjem
    if int(EMŠO[9]) < 5:  # string lahko pretvorimo v int in obratno, le računati (razen plusa) ne moremo!!
        spol = "Moški"

    else:
        spol = "Ženski"
    print(spol)


# 1 možnost je = , dve možnosti je if, else in tri ali več možnosti je if, elif, else!!!
#def gaga():#TUKAJ JE PRIKAZ RETURNA, LE KO GA POKLIČEMO S PRINT
    #return

#namesto inputa damo v oklepaj definicije()
"""
def datum_rojstva(EMŠO):
    if EMŠO[4] == "0":
        return EMŠO[0:2] + "." + EMŠO[2:4] + "." + "2" + EMŠO[4:7]
    else:
        return EMŠO[0:2] + "." + EMŠO[2:4] + "." + "1" + EMŠO[4:7]

print(datum_rojstva("1311979500970"))
"""
"""
def datum_rojstva(EMŠO):
    if EMŠO[4] == "0":
        return EMŠO[0:2] + "." + EMŠO[2:4] + "." + "2" + EMŠO[4:7]
    else:
        return EMŠO[0:2] + "." + EMŠO[2:4] + "." + "1" + EMŠO[4:7]

EMŠO = input("Vnesi svoj EMŠO: ") #pri funkciji je lahko spremenljivka tudi kasneje!!!
#print(datum_rojstva(EMŠO)) #to je klic funkcije!!

def spol(EMŠO):
    if EMŠO[9] in "01234": #ali if int(EMŠO[9]) < 5:
        return "Moški spol"
    else:
        return "Ženski spol"


EMŠO = input("Vnesi svoj EMŠO: ")  # pri funkciji je lahko spremenljivka tudi kasneje!!!
print(spol(EMŠO))  # to je klic funkcije!!
"""