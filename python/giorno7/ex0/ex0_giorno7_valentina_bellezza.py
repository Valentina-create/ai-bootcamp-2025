import csv

# Lista in cui memorizzare i dati
data = []

# Apertura del file CSV
with open("data.csv", mode="r") as fd:
    reader = csv.reader(fd)

    # Salto dell'intestazione, se presente
    header = next(reader, None)

    # Caricamento dei dati nelle variabili col metodo append
    for line in reader:
        data.append(line)

# Ordinamento dei dati in base alla seconda colonna (indice 1)
data_sorted = sorted(data, key=lambda x: x[1])

# Stampa dei dati ordinati con il numero sequenziale
for index, row in enumerate(data_sorted, start=1):
    print(f"{index}: {row}")

# creazione del secondo file

with open("data2.csv", mode="w", newline='') as fd2:
    writer = csv.writer(fd2)

    # Scrittura dell'intestazione nel nuovo file se presente
    if header:
        writer.writerow(header)

    # Scrittura delle righe ordinate senza indice
    writer.writerows(data_sorted)

# Stampa del contenuto del nuovo file CSV
with open("data2.csv", mode="r") as fd2:
    reader = csv.reader(fd2)
    for row in reader:
        print(row)
