def regn_pris(antall, pris_per_stk):
    return antall * pris_per_stk

def skriv_kvittering(navn, total):
    print(f"Kvittering for {navn}")
    print(f"Totalt: {total} kr")

def avslutt():
    print("Takk for handelen!")

pris = regn_pris(3, 49.90)
skriv_kvittering("Michael", pris)
print(f"Du betalte {pris} kr.")
avslutt
print(avslutt)

# --- Refleksjon ---
# 1. Manglet semikolon i prosedyren regn_pris, manglet innrykk på print på linje 5, oppgitt feil variabel i print linje 13 (skal være pris og ikke total), regn_pris mangler return og en variabel trenger ikke å bli deklarert i funksjonen
# 2. avslutt er ikke python-syntaks, det gir ikke feil men er ikke riktig, regn_pris funksjonen ga aldri noe tilbake (det er jo det som er poenget)
# 3. Jeg løste det ved at jeg endret {total} til {pris} og at regn_pris returnerer noe (det er det som er poenget). Det fungerte ikke fordi at {total} var en variabel på globalt nivå og regn_pris ikke returnerte noe
# 4. Fikk function avslutt at ***, det er nok fordi at python-syntaksen registrerer avslutt som en prosedyre (?)