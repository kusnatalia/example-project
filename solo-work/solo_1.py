#zadanie 1.7
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort(key=lambda x: x.split()[0])
print("Alfabetyczna lista studentow wynosi:")
for student in studenci:
    print(student)

