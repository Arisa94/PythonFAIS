x = 2 ; y = 3 ;
if (x > y):
	result = x;
else:
	result = y;


#Poprawnie, aczkolwiek nawiasy w warunku nie sa konieczne

for i in "qwerty":
	if ord(i) < 100: print i

#Niepoprawnie, w Pythonie wazne sa biale znaki, konieczna jest
#nowa linia i wciecie po petli

for i in "axby":
		print ord(i)
		if ord(i) < 100:
			pass
		else:
			i

#Niepoprawnie, jw. + po if'ie nie moze byc po prostu else'a, w if'ie musi sie
#cos znajdowac
