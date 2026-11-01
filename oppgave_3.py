def doble_print(tall):
    print(tall * 2)

def double_return(tall):
    return tall * 2

def regn_areal(lengde, bredde):
    return lengde * bredde

def skriv_areal(lengde, bredde):
    resultat = regn_areal(lengde, bredde)
    print(f"Arealet av rektangelet er: {resultat}")

doble_print(6)
print(doble_print(3))
skriv_areal(5, 6)

# --- Refleksjon ---
# 1. Fordi at funksjonen kun returnerer en verdi, det er ingen print i bildet. 
# 2. a er ingenting i steg 3, det er fordi at verdien kaller til en prosedyre og ikke en funksjon.
# 3. Det sier noe om at return er slutten, at det under ikke er kjørbart.
# 4. Forskjellen på en prosedyre og funksjon er at en prosedyre ikke returnerer noe, det gjør en funksjon.