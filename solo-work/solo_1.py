
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