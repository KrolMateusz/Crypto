import copy

do_ukrycia = 'a'
nosnik = 'ab ca bc cb bcacb cb ca'
bin_alfa = {' ': '00000', 'a': '00001', 'b': '00010', 'c': '00011'}
alfa_bin = {}

# ODWRACANIE
for klucz, wartosc in bin_alfa.items():
    alfa_bin[wartosc] = klucz
print(alfa_bin)
# DZIELENIE SŁOW, DODAWANIE SPACJI W WIADOMOSCI DO UKYRCIA, LISTA
tab = nosnik.split()[:5 * (len(do_ukrycia) + 1)]
for i in range(len(tab) - 1):
    tab[i] += ' '

# ZAPISYWANIE DO DRUGIEJ TABLICY ZNAKOW BINARNYCH
tab2 = []
for elem in tab:
    for letter in elem:
        if letter in bin_alfa.keys():
            tab2.append(bin_alfa[letter])
print(tab2)

# UKRYWANIE WIADOMOSCI
tab_wyj = []
while do_ukrycia:
    ukrywana_litera = do_ukrycia[0]
    do_ukrycia = do_ukrycia[1:]
    if ukrywana_litera in bin_alfa:
        ukrywana_litera_bin = bin_alfa[ukrywana_litera]
        for indeks, bit in enumerate(ukrywana_litera_bin):
            if bit == '1':
                licznik = -1
                for indeks_tab, elem in enumerate(tab2):
                    if elem == '00000':
                        licznik += 1
                    if licznik == indeks:
                        tab2.insert(indeks_tab, '00000')
print(tab2)

# ODSZYFROWANIE
output_list = []
for elem in tab2:
    output_list.append(alfa_bin[elem])
print(''.join(output_list))
