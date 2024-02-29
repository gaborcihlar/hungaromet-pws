# Készítette: Cihlár Gábor
# Verziószám: 1.0

import requests
import time
import schedule
import arrow
import json

pws = ""
# az idézőjelek közé írd be a MET-ÉSZ Beállítások alatt található PWS azonosítót
jelszo = ""
# az idézőjelek közé írd be a MET-ÉSZ jelszavad
tszfm = 123
# írd be az egyenlőségjel után 123 helyére a tengerszint feletti magasságot, ahol a műszered található
kuldes = 300   
# írd be másodperccel számolva, hogy milyen gyakran szeretnél adatot küldeni (javasolt 300 az 5 perchez, vagy 600 a 10 perchez)
szenzor = requests.get("http://192.168.0.111/sensors.json")
# az IP modul léghőmérséklet, páratartalom és légnyomásmérő érzékelőjének JSON linkje
szelmero = requests.get("http://192.168.0.111/wind.json")
# az IP modul szélmérőjének JSON linkje
    
def feladat():
    try:
        idokep1 = json.loads(szenzor.text)
        # az érzékelő adatainak beolvasása
        oke1 = (szenzor.status_code)
        # az érzékelő válasza
        tempc = (idokep1['hom'])
        # a léghőmérséklet értéke
        pressure = (idokep1['p'])
        # a műszerszinti légnyomás értéke
        humidity = (idokep1['rh'])
        # a páratartalom értéke
        legnyomas = (idokep1['ap'])
        # a műszerszinti légnyomás értéke
        baromhpa = (legnyomas*(1-((0.0065*tszfm)/(tempc+(0.0065*tszfm)+273.15)))**-5.257)
        # a tengerszinti légnyomás kiszámítása
        idokep2 = json.loads(szelmero.text)
        # a szélmérő adatainak beolvasása
        oke2 = (szenzor.status_code)
        # a szélmérő válasza
        winddir = (idokep2['dir'])
        # a szélirány értéke
        windspeedkmph = (idokep2['speed']*3.6)
        # a szélerősségmérő értéke és kilométe per órás sebesség kiszámítása
        if oke1 == 200 and oke2 == 200:
        # ha az érzékelő és a szélmérő válasza megfelelő
            print (oke1, oke2, '- OK!')
            # akkor írja ki a kapott válaszokat és írja ki, hogy OK!
            utc = time.time()
            # a pontos dátum és idő lekérdezése a számítőgépről
            datum = arrow.utcnow().format('YYYY-MM-DD HH:mm:ss')
            # a dátum és idő átalakítása megfelelő formátumra UTC-ben
            eszlel = {"PWS": pws, "FIX": jelszo, "dateutc": datum, "pressure": legnyomas, "baromhpa": baromhpa, "tempc": tempc, "humidity": humidity, "winddir": winddir, "windspeedkmph": windspeedkmph}
            #előkészíti az API-hoz szükséges formátumot a betöltött és létrehozott adatokkal 
            bead = requests.post("https://sandman.met.hu/metesz/pws", params=eszlel)
            #elkészíti a beküldéshez szükséges linket az előbb betöltött adatokkal
            print (bead.url)
            #kiírja az elkészített linket
        else:
            feladat()
    except json.decoder.JSONDecodeError:
        print ('HIBA! Az oldal nem tartalmaz JSON adatot!')
schedule.every(1).seconds.do(feladat)

while True:
    schedule.run_pending()
    time.sleep(kuldes-1)
