import csv
import sqlite3

# Apertura del file CSV
with open("students.csv", newline='', encoding='utf-8') as fd:
    reader = csv.reader(fd, delimiter=';') # per far riconoscere come delimiter ';'
    saved_data = list(reader)

# Verifica che ci siano dati e rimuove l'intestazione
if saved_data:
    header = saved_data[0]
    data = saved_data[1:]
else:
    data = []


# Connessione al database SQLite
conn = sqlite3.connect("students.db")
cur = conn.cursor()


# Creazione della tabella con email come identificatore univoco: se un record con la stessa email esiste già, l'ID rimane invariato .
# se un record nuovo viene inserito, SQLite assegna un nuovo ID progressivo
cur.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        year_of_birth INTEGER,
        gender TEXT,
        email TEXT UNIQUE,
        assignments INTEGER DEFAULT 0
    )
''')
conn.commit()


# inserimento  o aggiornamento dei dati senza cambiare ID: estrazione dei valori dalla riga, assegnandoli a variabili
# corrispondenti alle colonne della tabella. I valori year_of_birth assignments vengono convertiti in interi con int()
for row in data:
    first_name, last_name, year_of_birth, gender, email, assignments = row[1], row[2], int(row[3]), row[4], row[5], int(
        row[6])

    cur.execute('''
        INSERT INTO students (first_name, last_name, year_of_birth, gender, email, assignments)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(email) DO UPDATE SET
            first_name = excluded.first_name,
            last_name = excluded.last_name,
            year_of_birth = excluded.year_of_birth,
            gender = excluded.gender,
            assignments = excluded.assignments
    ''', (first_name, last_name, year_of_birth, gender, email, assignments))

conn.commit()
# Inserimento di un nuovo studente nel database: se l' email esiste già ( ON CONFLICT(email)), aggiorna i dati

print("Dati inseriti o aggiornati senza cambiare gli ID.")

# Stampare il contenuto della tabella
cur.execute("SELECT * FROM students")
rows = cur.fetchall()

print("\nContenuto della tabella students:")
for row in rows:
    print(row)

# Stampare gli studenti nati nell'anno 2000
cur.execute("SELECT * FROM students WHERE year_of_birth = 2000")
students_2000 = cur.fetchall()

print("\nStudenti nati nel 2000:")
for student in students_2000:
    print(student)

# Stampare la persona che ha consegnato il maggior numero di assignments
cur.execute("SELECT * FROM students WHERE assignments = (SELECT MAX(assignments) FROM students)")
top_student = cur.fetchall()

print("\nPersona con il maggior numero di assignments:")
for student in top_student:
    print(student)

# Stampare il cognome delle studentesse di nome 'Jane'
cur.execute("SELECT last_name FROM students WHERE first_name = 'Jane' AND gender = 'F'")
janes_last_names = cur.fetchall()

print("\nCognome delle studentesse di nome 'Jane':")
for last_name in janes_last_names:
    print(last_name[0])  # Stampa solo il cognome

# Graduatoria degli studenti ordinati in base al numero di assignments
cur.execute("SELECT * FROM students ORDER BY assignments DESC")  # La query ordina gli studenti in ordine decrescente in base al numero di assignments
ranking = cur.fetchall()

print("\nGraduatoria degli studenti (ordinata per numero di assignments):")
for student in ranking:
    print(student)


# Chiudere la connessione
conn.close()
