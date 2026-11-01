# Del 1 - Forutsi

"""
Snutt 1:
Jeg tror at det vil bli printet Hei! også kommer det en error om at melding ikke finnes fra siste linje.

def lag_hilsen():
    melding = "Hei!"
    print(melding)

lag_hilsen()
print(melding)
"""

"""
Snutt 2:
Jeg tror at det vil bli printet: Jeg bor i Oslo.

by = "Oslo"

def skriv_by():
    print(f"Jeg bor i {by}.")

skriv_by()
"""

"""
Snutt 3:
Jeg tror først at 10 blir printet, så 5.

def doble(tall):
    tall = tall * 2
    print(f"Inne: {tall}")

tall = 5
doble(tall)
print(f"Ute: {tall}")
"""

# Del 2 - Poengtelleren igjen
# Trodde egentlig at det skulle fungere, men innså at scope ikke tilater det. Begge løsningene gir mening, B er nok best.

def legg_til_poeng(poeng: int, antall: int) -> int:
    return poeng + antall

# --- Utvidelse ---
def trekk_fra_poeng(poeng: int, antall: int) -> int:
    return poeng - antall

poeng = 0
poeng = legg_til_poeng(poeng, 10)
poeng = legg_til_poeng(poeng, 25)
poeng = trekk_fra_poeng(poeng, 5)
print(poeng)

# --- Refleksjon ---
# 1. Det som skjer i første snutt er at prosedyren printer ut den lokale variabelen, så prøver den rett etter på globalt nivå å printe en lokal variabel noe som ikke går og det gir error. I tredje så sendes det inn et tall i en prosedyre så ganges det med to. Den endrer ikke variabelen på globalt nivå, kun lokalt.
# 2. Jeg tror at forskjellen er at prosedyrer/funksjoner kan lese variabler på globalt nivå, men ikke endre de. De kan selvfølgelig endres, men da gjør man det på andre måter som vises i Del 2.
# 3. Tror personlig at jeg hadde valgt løsning B, A fungerer selvfølgelig også men det er mye mer klart hva som skjer med løsning B. Eksempelet som blir oppgitt er et bra et, det er vanskelig å tracke hva som skjer når man bruker global.