<h1 align="left">HungaroMet PWS</h1>

###

<h3 align="left">A HungaroMet MET-ÉSZ oldalán tehetjük közzé az Időképes IP modul adatait.</h3>

###

<p align="left">WINDOWS alatt: töltsük le és telepítsük a Python környezetet a www.python.org oldalról, majd Parancssorban ellenőrizzük működését:</p>

```bash
python
```

###

<p align="left">Amennyiben sikeres volt a telepítés, az alábbi üzenetet fogjuk kapni: </p>

```bash
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36)...
```

<p align="left">Parancssorban lépjünk a Python telepítési mappájába, ami alapértelmezetten a következő helyen található: </p>

```bash
cd C:\Users\felhasználónév\AppData\Local\Programs\Python\Python312
```

<p align="left">Frissítsük a pip csomagtelepítőt: </p>

```bash
python -m pip install --upgrade pip
```

<p align="left">Telepítsük fel az alábbi kiegészítőket:</p>

```bash
python -m pip install requests
python -m pip install math
python -m pip install time
python -m pip install schedule
python -m pip install arrow
```

###

<p align="left">Írjuk át a program kódját a Python beépített szereksztőjével (jobb egérgomb, Edit with IDLE) vagy egy szövegszerkesztővel, például:</p>

[Notepad++](https://notepad-plus-plus.org/downloads/v8.6.4/)

<p align="left">Az alábbi részekre nagyon figyeljünk:</p>

```bash
pws = ""
# az idézőjelek közé írd be a MET-ÉSZ Beállítások alatt található PWS azonosítót
jelszo = ""
# az idézőjelek közé írd be a MET-ÉSZ jelszavad
tszfm = 123
# írd be az egyenlőségjel után 123 helyére a tengerszint feletti magasságot, ahol a műszered található
kuldes = 300   
# írd be másodperccel számolva, hogy milyen gyakran szeretnél adatot küldeni (javasolt 300 az 5 perchez, vagy 600 a 10 perchez)
```

<p align="left">Paranccsorban lépjünk abba a mappába, ahol a pws.py található, majd indítsuk el a programot:</p>

```bash
cd A:\letöltési\mappa\helye
```

```bash
python pws.py
```

###

<p align="left">Amennyiben mindent helyesen csináltunk, meg fognak jelenni a szenzoradatok a MET-ÉSZ oldalon.</p>
