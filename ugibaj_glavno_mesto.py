from random import randint, seed

def preveri(drzava, ugibano, slovar_mest):
    pravi_odgovor = slovar_mest[drzava]

    if pravi_odgovor == ugibano:
        print("BRAVO")
        return True
    else:
        print("NAROBE")
        return False

def main():
    slovar_mest = {"Slovenija": "ljubljana", "Avstrija": "vienna", "Hrvaska": "zagreb"}    

    brisi = raw_input("ali naj brisem ze ugotovljene (da/ne)").lower()

    if brisi == "da":
        brisi = True
    else:
        brisi = False

    ponovi = raw_input("ali naj ponavljam ne ugotovljene (da/ne)").lower()

    if ponovi == "da":
        ponovi = True
    else:
        ponovi = False

    zadnji_odgovor = True

    while len(slovar_mest) > 0:

        if zadnji_odgovor or not ponovi:    
            st_drzave = randint(0,len(slovar_mest)-1)

        drzava = slovar_mest.keys()[st_drzave]

        ugibano = raw_input("Katero je glavno mesto: " + drzava + " ?")

        ugibano = ugibano.lower()

        zadnji_odgovor = preveri(drzava, ugibano, slovar_mest)

        if brisi and zadnji_odgovor:
            del slovar_mest[drzava]
    
if __name__ == "__main__":
    main()
