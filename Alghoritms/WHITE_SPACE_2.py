import pprint

do_ukrycia = 'ad'
nosnik = 'ab ca bc cb bcacb cb ca da fafa fafa '

bin_alfa = {' ': '00000', 'a': '00001', 'b': '00010', 'c': '00011',
            'd': '00100', 'e': '00101', 'f': '00110', 'g': '00111',
            'h': '01000', 'i': '01001', 'j': '01010', 'k': '01011',
            'l': '01100', 'm': '01101', 'n': '01110', 'o': '01111',
            'p': '10000', 'q': '10001', 'r': '10010', 's': '10011',
            't': '10100', 'u': '10101', 'v': '10110', 'w': '10111',
            'x': '11000', 'y': '11001', 'z': '11010', '.': '11011',
            '\n': '11100', '?': '11101', '!': '11110', ',': '11111'}
alfa_bin = {}

# ODWRACANIE
for klucz, wartosc in bin_alfa.items():
    alfa_bin[wartosc] = klucz

# DZIELENIE SŁOW, DODAWANIE SPACJI W WIADOMOSCI DO UKYRCIA, LISTA
tab = nosnik.split()[:5 * len(do_ukrycia)]
for i in range(len(tab)):
    tab[i] += ' '

# ZAPISYWANIE DO DRUGIEJ TABLICY ZNAKOW BINARNYCH

tab2 = [[] for x in range(len(tab) // 5)]
for nr_listy, lista in enumerate(tab2):
    for elem in tab[nr_listy * 5:(nr_listy + 1) * 5]:
        for litera in elem:
            if litera in bin_alfa.keys():
                tab2[nr_listy].append(bin_alfa[litera])
print(tab2)
# UKRYWANIE WIADOMOSCI

while do_ukrycia:
    ukrywana_litera = do_ukrycia[0]
    do_ukrycia = do_ukrycia[1:]
    for indeks_tab2, lista in enumerate(tab2):
        if ukrywana_litera in bin_alfa:
            ukrywana_litera_bin = bin_alfa[ukrywana_litera]
            for indeks, bit in enumerate(ukrywana_litera_bin):
                if bit == '1':
                    licznik = 0
                    for indeks_tab, elem in enumerate(lista):
                        if elem == '00000':
                            licznik += 1
                        if licznik == indeks:
                            tab2[indeks_tab2].insert(indeks_tab, '00000')
print(tab2)

# ODSZYFROWANIE

# output_list = []
# for elem in tab2:
#     output_list.append(alfa_bin[elem])
# print(''.join(output_list))
