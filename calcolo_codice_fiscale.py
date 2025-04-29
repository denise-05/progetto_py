import datetime

# Calcola le 3 lettere del cognome
def codice_cognome(cognome):
    consonanti = ''.join([c for c in cognome.upper() if c.isalpha() and c not in 'AEIOU'])
    vocali = ''.join([c for c in cognome.upper() if c.isalpha() and c in 'AEIOU'])
    return (consonanti + vocali + 'XXX')[:3]

# Calcola le 3 lettere del nome
def codice_nome(nome):
    consonanti = ''.join([c for c in nome.upper() if c.isalpha() and c not in 'AEIOU'])
    vocali = ''.join([c for c in nome.upper() if c.isalpha() and c in 'AEIOU'])
    if len(consonanti) >= 4:
        return consonanti[0] + consonanti[2] + consonanti[3]
    else:
        return (consonanti + vocali + 'XXX')[:3]

# Calcola anno, mese e giorno (aggiunge 40 se femmina)
def codice_data_nascita(data, sesso):
    mesi = "ABCDEHLMPRST"
    data = datetime.datetime.strptime(data, "%d/%m/%Y")
    anno = str(data.year)[-2:]
    mese = mesi[data.month - 1]
    giorno = data.day + 40 if sesso.upper() == 'F' else data.day
    return anno + mese + f"{giorno:02d}"

# Codici catastali (solo alcuni per semplicità)
comuni = {
    'ROMA': 'H501',
    'MILANO': 'F205',
    'NAPOLI': 'F839',
    'TORINO': 'L219',
    'APRILIA': 'A341',
    'PALERMO': 'G273'
}

# Codice comune
def codice_comune(comune):
    return comuni.get(comune.upper(), "XXXX")

# Funzione principale
def main():
    print("== Generatore di Codice Fiscale ==")
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    data_nascita = input("Data di nascita (gg/mm/aaaa): ")
    sesso = input("Sesso (M/F): ")
    comune = input("Comune di nascita: ")

    cf = (
        codice_cognome(cognome) +
        codice_nome(nome) +
        codice_data_nascita(data_nascita, sesso) +
        codice_comune(comune) +
        "X"  # Carattere di controllo semplificato
    )

    print("Codice fiscale (semplificato):", cf)

# Avvia il programma
main()