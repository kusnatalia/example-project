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

