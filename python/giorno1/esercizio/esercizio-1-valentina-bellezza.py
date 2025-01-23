print("Inizio programma")

# Assegno la variabile foo
foo = False

# Questi controlli assert devono passare tutti
assert not bool(0)
assert False != True
assert not True is False
assert True != False
assert None is not False

# Faccio alcune operazioni aritmetiche sui numeri interi
bar = 1
baz = 1
result = baz / bar

# Incremento il risultato di uno

result + 1

# Decremento il risultato di uno

result -= 1

# Controllo che il valore non sia negativo
assert not result < 0

# Concateno le stringhe
str = "hello"
byte = b"world"
#si tratta di 2 tipi distinti, quindi converto la stringa in bytes
str_in_bytes = str.encode ("utf-8")
message = str_in_bytes + byte

# Creo una lista e la estendo
li1 = [1, 2]
li1 += [3]

# Non mi ricordo come si "prepende" un valore...
li1 = [0] + li1

# Verifico che il risultato sia quello che mi aspetto
assert li1 == [0, 1, 2, 3]

# Creo una tupla e la estendo (convertendo in lista, estendendo questa e riconverto in tupla)
tu1 = (1, 2)
li2 = list(tu1)
li2 += [3]
tu1 = tuple(li2)

assert tu1 == (1, 2, 3)

# Creo un dict

d1 = {}
d2 = {}
d2["a"] = 1
d1["a"] = 1
d1["b"] = 2
assert d2["a"] == 1
assert d1 == {"a": 1, "b": 2}

# Cancello la chiave "b"
del d1["b"]

# Controllo che il dict non contenga ancora la chiave "b"
assert "b" not in d1

# Potrei anche controllarlo in questo modo
# e verificare anche la presenza di "a"
if "b" not in d1:
    assert True
elif "a" in d1:
    assert True
else:
    assert True

# Stampo la scritta "Ciao" tre volte poi esco
# Conto le volte che l'ho stampata
count = 0
for idx in [0, 1, 2]:
    count += 1
    print("Ciao")

# Controllo che l'abbia stampata tre volte
assert count == 3

# Stampo di nuovo la scritta "Ciao" tre volte poi esco
num = 3
while num > 0:
    print("Ciao")
    num -= 1

print("Fine programma")

# Bonus: verifico la seguente operazione sui float
#assert 0.1 + 0.2 == 0.3