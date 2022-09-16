def oktaeder_šolska(): # zaustavitev brez if stavka
# pri kateri stranici je volumen oktaedra manjši od 500? Začni pri 1, cela števila in izpiši volumen.
    # V=a**3 * sqrt(2)/3
#!!!!!!!!!!STRING JE SAMO; KO SE Z INPUTOM JEMLJE!!!!!!!!!!!

    a = 1  # 1.
    V = a ** 3 * sqrt(2) / 3  # 3.

    while V < 500:
        # zaradi zaustavitve pred 500 smo dal print po while in za printom povečanja
        print("Za stranico", a, "je volumen kvadra", str(round(V, 2)) + ".")
        a = a + 1  # 4.
        V = a ** 3 * sqrt(2) / 3

#WHILE ZANKO UPORABIMO; KO NE VEMO KOLIKO BO PONOVITEV



def vaja_7_EMŠO():#DDMMYYYRRSCCC(datum,mesec,leto,regija,spol,kontrolne številke)

    #NAVODILA: Uporabnik vnese EMŠO, vi pa izpišete njegov datum rojstva in spol.
    # Napišite tri funkcije za izpis datuma rojstva, letnico in spol
    EMŠO = input("Vnesite Vaš EMŠO: ") #1311979500970 mesto 9 --> 0 = moški, 5 = ženska
    def tisočletje(): #funkcija v funkciji, kadar ne želimo, da se takoj vidi, ampak nekje drugje
        tisočletje = EMŠO[4]
        if tisočletje in ("7", "8", "9"):
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

# import druge datoteke
from PYTHON_ZAPISKI_PREDAVANJE_3 import *

def vaja_7_EMŠO_ŠOLSKA():
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

    print(datum)

print(datum)

    #pojdimo za spol
    #s pripadnostjo množici iz niza
    if EMŠO[9] in "01234":
        spol = "Moški"
    else:
        spol = "Ženski"
    print(spol)

    #ali s primerjalnim operatorjem
    if int(EMŠO[9]) <5: #string lahko pretvorimo v int in obratno, le računati (razen plusa) ne moremo!!
        spol = "Moški"

    else:
        spol = "Ženski"
    print(spol)


def datum_rojstva(EMŠO):
    if EMŠO[4] == "0":
        return EMŠO[0:2] + "." + EMŠO[2:4] + "." + "2" + EMŠO[4:7]
    else:
        return EMŠO[0:2] + "." + EMŠO[2:4] + "." + "1" + EMŠO[4:7]

EMŠO = input("Vnesi svoj EMŠO: ") #pri funkciji je lahko spremenljivka tudi kasneje!!!

print(datum_rojstva(EMŠO)) #to je klic funkcije!!
#print(datum_rojstva("1311979500970"))
#dve returna, vendar ena pot

def spol(EMŠO):
    if EMŠO[9] in "01234": #ali if int(EMŠO[9]) < 5:
        return "Moški spol"
    else:
        return "Ženski spol"


EMŠO = input("Vnesi svoj EMŠO: ")  # pri funkciji je lahko spremenljivka tudi kasneje!!!
print(spol(EMŠO))  # to je klic funkcije!!