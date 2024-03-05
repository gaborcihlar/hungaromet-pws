# Készítette: Cihlár Gábor
# Verziószám: 1.01
# Frissítve: 2024.03.05-én

# betölti a szükséges bővítményeket
import requests
import time
import schedule
import arrow
import json

# az idézőjelek közé írd be a MET-ÉSZ Beállítások alatt található PWS azonosítót
pws = ""
# az idézőjelek közé írd be a MET-ÉSZ jelszavad
jelszo = ""
# írd be az egyenlőségjel után 123 helyére a tengerszint feletti magasságot, ahol a műszered található
tszfm = 123
# írd be másodperccel számolva, hogy milyen gyakran szeretnél adatot küldeni (javasolt 300 az 5 perchez, vagy 600 a 10 perchez)
kuldes = 300   
# az IP modul léghőmérséklet, páratartalom és légnyomásmérő érzékelőjének JSON linkje
szenzor = requests.get("http://192.168.0.111/sensors.json")
# az IP modul szélmérőjének JSON linkje
szelmero = requests.get("http://192.168.0.111/wind.json")
    
def feladat():
    try:
        # az érzékelő adatainak beolvasása
        idokep1 = json.loads(szenzor.text)
        # az érzékelő válasza
        oke1 = (szenzor.status_code)
        # a léghőmérséklet értéke
        tempc = (idokep1['hom'])
        # a műszerszinti légnyomás értéke
        pressure = (idokep1['p'])
        # a páratartalom értéke
        humidity = (idokep1['rh'])
        # a műszerszinti légnyomás értéke
        legnyomas = (idokep1['ap'])
        # a tengerszinti légnyomás kiszámítása, csak ha van léghőmérséklet adat
        baromhpa = (legnyomas*(1-((0.0065*tszfm)/(tempc+(0.0065*tszfm)+273.15)))**-5.257)
        # a szélmérő adatainak beolvasása
        idokep2 = json.loads(szelmero.text)
        # a szélmérő válasza
        oke2 = (szenzor.status_code)
        # a szélirány értéke
        winddir = (idokep2['dir'])
        # a szélerősségmérő értéke és kilométe per órás sebesség kiszámítása
        windspeedkmph = (idokep2['speed']*3.6)
        # ha az érzékelő és a szélmérő válasza megfelelő
        if oke1 == 200 and oke2 == 200:
            # akkor kiírja a kapott JSON válaszokat és az OK üzenetet
            print (oke1, oke2, '- OK!')
            # a pontos dátum és idő lekérdezése a számítőgépről
            utc = time.time()
            # a dátum és idő átalakítása UTC-ra megfelelő formátumban
            datum = arrow.utcnow().format('YYYY-MM-DD HH:mm:ss')
            # előkészíti az API-hoz szükséges formátumot a betöltött és létrehozott adatokkal 
            eszlel = {"PWS": pws, "FIX": jelszo, "dateutc": datum, "pressure": legnyomas, "baromhpa": baromhpa, "tempc": tempc, "humidity": humidity, "winddir": winddir, "windspeedkmph": windspeedkmph}
            # elkészíti a beküldéshez szükséges linket az előbb betöltött adatokkal
            bead = requests.post("https://sandman.met.hu/metesz/pws", params=eszlel)
            # kiírja az elkészített linket
            print (bead.url)
        else:
            feladat()
    except json.decoder.JSONDecodeError:
        print ('HIBA! Az oldal nem tartalmaz JSON adatot!')
schedule.every(1).seconds.do(feladat)

while True:
    schedule.run_pending()
    time.sleep(kuldes-1)
