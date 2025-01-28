# Scrivere il codice dell'esercizi qui dentro

#primo esercizio: replico la funzione incorporata sollevando l'eccezione e gestisco l'eccezione all'interno della funzione

def my_divmod (a, b):
    if b == 0:
        raise ZeroDivisionError ("divisione per zero non consentita")
    quoziente = a // b
    resto = a % b
    return quoziente, resto
try:
    risultato = my_divmod (15, 0)
    print (risultato)
except ZeroDivisionError as e:
    print (f"Attenzione: {e}")

#secondo esercizio
#Implementa una funzione che prende una lista e restituisce un'altra lista con ogni valore elevato alla potenza di 2
li = [1, 2, 3]
def pow_list(li):
    for el in li:
        return [el**2 for el in li]

risultato = pow_list(li)
print (risultato)

assert pow_list([1, 2, 3]) == [1, 4, 9]

#Implementa una funzione che conta il numero di parole nella stringa data
def count_words(stringa):
    parole = stringa.split(' ')  # Divide la stringa in parole
    return len(parole)
stringa = "hello world"
numero_parole = count_words(stringa)
print(f"Il numero di parole in '{stringa}' è: {numero_parole}")

assert count_words("hello world")

#Implementa una funzione che accetta una stringa e la restituisce invertita

def reverse_string (s):
    return s[::-1]

parola = "hello"
parola_invertita = reverse_string(parola)
print (parola_invertita)

assert reverse_string("hello") == "olleh"

#Implementa una funzione che calcola il fattoriale di un numero dato

def factorial(n):
    risultato = 1
    for i in range(1, n + 1):
        risultato *= i
    return risultato
n = 5
print(factorial(5))

assert factorial(5) == 120

#Implementa una funzione che controlla se una data stringa è un palindromo

def is_palindrome(s):
    return s == s[::-1]

stringa = "racecar"
if is_palindrome(stringa):
    print(f'"{stringa}" è un palindromo')

assert is_palindrome("racecar") == True

#Implementa una funzione che accetta una lista di numeri e restituisce la somma di tutti i numeri pari

def sum_even_numbers(li):
    sum = 0
    for number in li:
        if number % 2 == 0:
            sum += number
    return sum

li = [1, 2, 3, 4, 5]
result = sum_even_numbers(li)
print(result)

assert sum_even_numbers([1, 2, 3, 4, 5]) == 6

#Implementa una funzione che accetta una lista di numeri e restituisce il numero più grande nella lista

def find_max(li):
    return max(li)

li = [1, 2, 3, 4, 5]
print (find_max (li))

assert find_max([3, 1, 4, 1, 5]) == 5

#Implementa una funzione che accetta una stringa e restituisce il conteggio delle vocali in essa contenute

def count_vowels(s):
    vocali = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vocali:
            count += 1
    return count

print(count_vowels("Hello world"))

assert count_vowels("hello world") == 3
