# --- Del 1 ---

"""navn = str(input("Hva er ditt navn? "))
poeng = int(input("Skriv inn poeng (0-100): "))

def finn_karakter(poeng: int) -> str:
    if poeng >= 101:
        return "Ugyldig tall (0-100)"
    elif poeng >= 90:
        return "A"
    elif poeng >= 80:
        return "B"
    elif poeng >= 60:
        return "C"
    elif poeng >= 50:
        return "D"
    elif poeng >= 40:
        return "E"
    elif poeng <= -1:
        return "Ugyldig tall (0-100)"
    else:
        return "F"

def skriv_resultat(navn: str, karakter: str) -> None:
    print(f"Hei {navn}! Du fikk karakteren {karakter}.")

skriv_resultat(navn, finn_karakter(poeng))"""

# --- Del 2 ---

"""def doble(tall: int) -> int:
    return tall * 2

print(doble("5"))"""

# Jeg trodde det ville gi error, men det ble 55!

# --- Utvidelse ---
def regn_total(brus_antall: int, smørbrød_antall: int, banan_antall: int, regning_antall: int) -> None:
    total = brus_pris * brus_antall + smørbrød_pris * smørbrød_antall + banan_pris * banan_antall

    print(f"Totalsum: {total}")

    del_regning(legg_til_mva(total), regning_antall)

def legg_til_mva(total: float) -> float:
    totalsum_med_mva = total * mva
    print(f"Totalsum med 25% mva: {totalsum_med_mva}")
    return totalsum_med_mva

def del_regning(total: float, regning_antall: int) -> None:
    totalsum_delt = total / regning_antall
    print(f"Pris per person ({regning_antall} stk): {totalsum_delt}")


brus_pris = 24.90
smørbrød_pris = 45
banan_pris = 8.50

mva = 1.25

brus_antall = int(input("Hvor mange brus? "))
smørbrød_antall = int(input("Hvor mange smørbrød? "))
banan_antall = int(input("Hvor mange bananer? "))

regning_antall = int(input("Hvor mange skal dele regningen? "))

regn_total(brus_antall, smørbrød_antall, banan_antall, regning_antall)



# --- Refleksjon ---
# 1. Ved bruk av funksjoner så blir alt mye tydeligere synes jeg personlig
# 2. Fordi at den går gjennom alle if-statements uansett
# 3. Jeg tror det er der for klarheten, det viser mye tydligere hva du forventer og gjør det klart og tydelig