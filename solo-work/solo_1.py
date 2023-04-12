
# zadanie 1.1
komunikat = "{} {}"
hello = "Hello"
student = "Natalia"

pelny_komunikat = komunikat.format(hello, student)
print("Hello Natalia")

# zadanie 1.2

student = input("Natalia")

print("Hello Natalia")

# zadanie 1.3
studenci = ["Ania", "Kuba", "Piotr", "Jan"]

liczba_studentow = len(studenci)
print("Liczba studentow wynosi:", liczba_studentow)

#zadanie 1.4
studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

for student in studenci:
    print("Hello", student)

#zadanie 1.5
liczba = 3
potega = 4

wynik = liczba ** potega

print("Wynik wynosi:", wynik)
#zadanie 1.6
ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")

print("Liczba nawiasow otwierajacych wynosi:", liczba_nawiasow_otwierajacych)

#zadanie 1.7
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]


studenci.sort(key=lambda x: x.split()[0])

print("Alfabetyczna lista studentow wynosi:")
for student in studenci:
    print(student)
#zadanie 1.8
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]


nazwiska = [student.split()[-1] for student in studenci]
studenci_sorted = [s for _, s in sorted(zip(nazwiska, studenci))]


print("Alfabetyczna lista studentów wynosi:")
for student in studenci_sorted:
    print(student)
#zadanie 1.9
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

liczba_n = 0
for student in studenci:
    nazwisko = student.split()[-1]
    if nazwisko.startswith('N'):
        liczba_n += 1

print("Liczba studentow na N wynosi:", liczba_n)
#zadanie 1.10
wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]



wykres_1_funkcja_liniowa = (wykres_1[1][1] - wykres_1[0][1]) == (wykres_1[2][1] - wykres_1[1][1])
wykres_2_funkcja_liniowa = (wykres_2[1][1] - wykres_2[0][1]) == (wykres_2[2][1] - wykres_2[1][1])
wykres_3_funkcja_liniowa = (wykres_3[1][1] - wykres_3[0][1]) == (wykres_3[2][1] - wykres_3[1][1])

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")