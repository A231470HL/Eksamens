## Funkcionalitāte

- **Preču pārlūkošana** - Apskatīt visas pieejamās preces vai filtrēt pēc kategorijas
- **Preču filtrēšana** - Filtrēt preces pēc cenas, izmēra vai krāsas
- **Iepirkumu grozs** - Pievienot un noņemt preces no groza
- **Piegādes opcijas** - Izvēlēties starp dažādiem piegādes veidiem (standarta, ātrā, bezmaksas)
- **Atlaižu sistēma** - Piemērot atlaides (jaunā klienta, lojalitātes, akcijas)
- **Krāsaina saskarne** - Pateicoties Colorama bibliotēkai, programma izmanto krāsas, lai uzlabotu lietotāja pieredzi

## Programmas struktūra

- **main.py** - Programmas galvenais fails, kas inicializē veikalu
- **shop.py** - Satur Shop klasi, kas pārvalda veikala funkcionalitāti un lietotāja saskarni
- **product.py** - Satur Product un ProductCollection klases, kas pārvalda preces un preču kolekcijas
- **cart.py** - Satur Cart klasi, kas implementē iepirkumu groza funkcionalitāti
- **products.csv** - CSV fails ar preču datiem (nosaukums, cena, kategorija, izmēri, krāsas)

### Galvenā izvēlne

Programmā pieejamas šādas opcijas:
1. Apskatīt visas pieejamās preces
2. Apskatīt grozu
3. Pievienot preci grozam pēc kategorijas
4. Noņemt preci no groza
5. Filtrēt preces
6. Piegādes un atlaižu iestatījumi
7. Veikt pirkumu
8. Iziet

### Preču filtrēšana

Preces var filtrēt pēc:
- Cenas diapazona (minimālā un maksimālā cena)
- Izmēra (izvēle no pieejamiem izmēriem)
- Krāsas (izvēle no pieejamajām krāsām)

### Piegādes un atlaižu iestatījumi

Pieejamie piegādes veidi:
- Standarta piegāde: 2.99€
- Ātrā piegāde: 5.99€
- Bezmaksas piegāde: 0.00€

Pieejamās atlaides:
- Bez atlaides: 0%
- Jaunā klienta atlaide: 10%
- Lojalitātes atlaide: 15%
- Akcijas atlaide: 20%

## Preču sortiments

Veikalā pieejamas preces šādās kategorijās:
- Krekli
- Šorti
- Džemperi
- Bikses
- Aksesuāri

Katrai precei ir noteikti izmēri (S, M, L vai OneSize) un krāsu varianti.


## Izstrādātāji

© 2025 Ralfs Konrads Haralds Labalaikis DP2-2