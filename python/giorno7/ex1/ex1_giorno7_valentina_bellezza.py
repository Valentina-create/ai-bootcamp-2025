import random
import csv
import os
from datetime import datetime

# Nome del file dove salvare i record
HIGH_SCORE_FILE = "high_scores.csv"

# Funzione per leggere i punteggi dal file
def carica_punteggi():
    punteggi = []
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                nome, tentativi, data = row
                punteggi.append((nome, int(tentativi), data))
    return punteggi


# Funzione per salvare i punteggi sul file
def salva_punteggi(punteggi):
    with open(HIGH_SCORE_FILE, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(punteggi)


# Funzione principale del gioco
def indovina_il_numero():
    numero_da_indovinare = random.randint(1, 100)
    tentativi = 0

    print("Benvenuto nel game! Indovina il numero tra 1 e 100.")

    while True:
        try:
            tentativo = input("Qual è il numero? ")
            if not tentativo.isdigit():
                raise ValueError("Input errato. Riprova.")

            tentativo = int(tentativo)
            tentativi += 1

            if tentativo < numero_da_indovinare:
                print("Troppo basso")
            elif tentativo > numero_da_indovinare:
                print("Troppo alto")
            else:
                print(f"Hai indovinato in {tentativi} tentativi!")
                return tentativi  # Restituisce il numero di tentativi effettuati
        except ValueError:
            print("Inserisci un numero intero.")


# Funzione principale che gestisce il gioco e i punteggi
def main():
    punteggi = carica_punteggi()

    while True:
        tentativi = indovina_il_numero()

        # Controlla se il punteggio è il migliore o se è tra i migliori
        if not punteggi or tentativi < min(p[1] for p in punteggi):
            nome = input("Hai fatto il record! Inserisci il tuo nome: ")
            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            punteggi.append((nome, tentativi, data))

            # Ordina i punteggi in base al numero di tentativi (ascendente)
            punteggi.sort(key=lambda x: x[1])

            # Salva la nuova classifica
            salva_punteggi(punteggi)

        rigioca = input("Vuoi giocare ancora? (s/n): ").strip().lower()
        if rigioca != "s":
            break

    # Stampa la classifica finale
    print("Classifica dei migliori punteggi")
    for i, (nome, tentativi, data) in enumerate(punteggi[:5], start=1):
        print(f"{i}. {nome} - {tentativi} tentativi ({data})")

    print("Grazie per aver giocato!")

if __name__ == "__main__":
    main()
