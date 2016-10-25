L = L.sort()

#L nie jest zainicjalizowane, wiec nie mozna na nim uzyc metody sort

x, y = 1, 2, 3

#Nie mozna przypisac wartosci krotki trzyelementowej do krotki z dwuelementowej

X = 1, 2, 3 ; X[1] = 4

#Nie mozna odwolac sie do krotki jak do tablicy (po indeksie)

X = [1, 2, 3] ; X[3] = 4

#Indeks wychodzi poza zakres

X = "abc" ; X.append("d")

#Na obiekcie X nie mozna uzyc metody append, gdyz nie jest lista

print map(pow, range(8))

#W funkcji map brakuje jednego argumentu, gdyz funkcja pow na ktora mapujemy wymaga 2 argumentow