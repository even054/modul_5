def hilsen(navn, alder, by="Oslo"):
    print(f"Hei, {navn}! Du er {alder} år og bor i {by}.")

navn = input("Hva er navnet ditt? ")
alder = input("Hvor gammel er du? ")
by = input("Hvilken by er du fra? ")
hilsen(navn, alder, by)

# --- Utvidelse ---
# Hvis man kaller prosedyren med en by så kommer det man skriver inn, hvis man ikke har by i prosedyre kallet så kommer standardverdien Oslo. Det som skjer hvis man flytter et parameter med default forran en som ikke har det er at man får syntaxerror. Parametere med standardverdi skal alltid være bakerst.

# --- Refleksjon ---
# 1. Forskjellen på parameter og argument er at parameterer er det som er i prosedyren/funksjonen og argumentet er i kallet.
# 2. Det gir ikke en feilmelding, det ga "Hei, 31! Du er Michael år."
# 3. Det sier at rekkefølgen har noe å si, ikke hva variabelen heter.
# 4. Det fungerte fordi at man ga variablene riktige verdier selvom rekkefølgen var snudd. Jeg tror de er nyttige når man ikke får hatt de i riktig rekkefølge.