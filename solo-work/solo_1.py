#zadanie 1.9
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

liczba_n = 0
for student in studenci:
    nazwisko = student.split()[-1]
    if nazwisko.startswith('N'):
        liczba_n += 1

print("Liczba studentow na N wynosi:", liczba_n)

