import datetime

# ezeket kell importálni
from datetime import datetime, timezone, date, time
from time import ctime, sleep, strptime

# várakozás

sleep(2)

print(datetime.now(timezone.utc))

#  datum/idő -lekérdezése időzónával
now = datetime.now(timezone.utc)

print(now.date())



# beadott 0karakterekből dátumot csinál (év,hó,nap)
print(date(2000, 12, 1))

# az epocha-tól eltelt idő (induló dátumtól eltelt secundumokat alakítja át)
print(ctime())
print(strptime("2022-03-25"))
