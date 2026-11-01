def skriv_skillelinje():
    print("-" * 20)

def skriv_velkomst():
    print("Velkommen til sjappa!")
    print("Dette er menyen:")
    print("")

def skriv_meny():
    skriv_skillelinje()
    print("--- Meny ---")
    print("1. Pizza")
    print("2. Burger")
    print("3. Salat")
    skriv_skillelinje()

skriv_velkomst()
skriv_meny()

# --- Utvidelse ---
# Det som skjer er at det kommer tjue bindestrek før og etter menyen.

# --- Refleksjon ---
# 1. Det som skjer er ingenting, det er fordi at man må kalle på prosedyren/funksjonen for at noe skal skje.
# 2. Forskjellen er at når man definerer så skriver man i blokken hva som skal skje når man kaller på selve prosedyren.
# 3. Feilmeldingen sa at 'skriv_meny' ikke er definert, det er i teorien sant fordi at kallet må være under prosedyren/funksjonen.
# 4. Det er nyttig fordi at man fjerner redudant kode, noe som gjør koden kortere og enklere å lese.