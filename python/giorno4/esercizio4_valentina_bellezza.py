# creo una classe generica per i contatti:
# che ha un costruttore (__init__) che accetta
# un nome e un numero di telefono (quest'ultimo opzionale, impostato a None di default)

class Contact:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone if self.phone else 'N/A'}"

# implemento il dunder method __str__ che serve a restituire una rappresentazione testuale
# del contatto indicando il numero se presente, altrimenti "N/A"



# creo una classe Person che eredita dalla classe Contact;
# un metodo costruttore che accetta nome, cognome e numero do telefono;
# uso super().__init__ per inizializzare la classe base (Contact), ossia per creare
# una classe derivata, concatenando name e surname per ottenere il nome completo

class Person(Contact):
    def __init__(self, name, surname, phone=None):
        super().__init__(name + " " + surname, phone)



#creo un'altra classe Business derivata da Contact,
# ma accetta solo un name e un numero di telefono
# anche qui inizializzo per ereditare dalla superclasse Contact;

class Business(Contact):
    def __init__(self, name, phone=None):
        super().__init__(name, phone)



#Creo la classe Directory che rappresenta la rubrica telefonica
#inserisco un attributo contacts, che è una lista vuota in cui memorizzare i contatti

class Directory:
    def __init__(self):
        self.contacts = []

    def add(self, contact):
        self.contacts.append(contact)

    def __len__(self):
        return len(self.contacts)

    def query(self, name):
        result = []
        for contact in self.contacts:
            if contact.name.startswith(name):
                result.append(contact)
        return result

    def find(self, keyword):
        result = []
        for contact in self.contacts:
            if keyword in contact.name or (contact.phone and keyword in contact.phone):
                result.append(contact)
        return result


# definisco i metodi:
# add: che aggiunge un oggetto contact alla lista contacts;
# il dunder method __len__: che permette di usare len(directory), restituendo il numero di contatti presenti;
# il metodo query: utilizzato per eseguire interrogazioni su dati,
# in questo caso cerca i contatti che iniziano con la stringa nome
# (utile per cercare sia persone che aziende) restituendo una lista con i contatti trovati;
# il metodo find: restituisce i contatti
# che contengono la keyword nel nome o nel numero di telefono



# Creo una rubrica vuota, un'istanza della rubrica
directory = Directory()

# Verifico che la lunghezza della mia rubrica sia uguale a zero (controllo quindi che sia vuota)
assert len(directory) == 0


# Aggiungo tre contatti alla mia rubrica:
#Una Person con nome completo e telefono;
#Un Business con nome e telefono;
#Una Person con nome ma senza telefono.


directory.add(Person(name="Margaret", surname="Hamilton", phone="01-234-567"))
directory.add(Business(name="Vedrai", phone="+39-333-333333"))
directory.add(Person(name="Linda", surname="Hamilton"))


# Verifico che la lunghezza della rubrica sia uguale a tre
#quindi controllo con assert che la rubrica contenga adesso tre contatti

assert len(directory) == 3


# eseguo due ricerche per nome, ottenendo i contatti corrispondenti
# e stampo con la funzione print i risultati per verificarne il contenuto

query_result = directory.query(name="Vedrai")
print([str(el) for el in query_result])

query_result = directory.query(name="Margaret")
print([str(el) for el in query_result])



# Verifico con assert che la query per "Vedrai" restituisca il numero "+39-333-333333"
# Verifico con assert che la query per "Margaret" restituisca il numero "01-234-567"

assert [el.phone for el in directory.query(name="Vedrai")] == ["+39-333-333333"]
assert [el.phone for el in directory.query(name="Margaret")] == ["01-234-567"]



# poi grazie alla funzione find implemento una funzione che mi permette di fare una ricerca completa
# su tutti i contatti.
# Per ciascun contatto, verifica se la parola chiave (keyword)
# è contenuta nel nome del contatto (contact.name)
# o nel suo numero di telefono (contact.phone).
# Restituisce una lista di contatti che soddisfano questa condizione.

# Risultato per la ricerca della parola "Hamilton"

hamilton_results = directory.find("Hamilton")
print("Risultati per 'Hamilton':")
for contact in hamilton_results:
    print(f"Nome: {contact.name}, Telefono: {contact.phone if contact.phone else 'N/A'}")


# Risultato per la ricerca della parola "333"

three_three_three_results = directory.find("333")
print("\nRisultati per '333':")
for contact in three_three_three_results:
    print(f"Nome: {contact.name}, Telefono: {contact.phone if contact.phone else 'N/A'}")



# Verifico con assert che i risultati per le ricerche per nome
# restituiscano  i nomi e i numeri di telefono corrispondenti se presenti


assert [el.phone for el in directory.find("Hamilton")] == ["01-234-567", None]
# 'Hamilton' appare in Margaret e Linda



# Verifico con assert che il risultato per la ricerca per la stringa "333"
# corrisponda al numero di telefono e al nome in rubrica

assert [el.name for el in directory.find("333")] == ["Vedrai"]
# "333" appare nel numero di telefono di Vedrai


