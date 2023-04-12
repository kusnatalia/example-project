#zadanie 1.8
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
nazwiska = [student.split()[-1] for student in studenci]
studenci_sorted = [s for _, s in sorted(zip(nazwiska, studenci))]
print("Alfabetyczna lista studentów wynosi:")
for student in studenci_sorted:
    print(student)

