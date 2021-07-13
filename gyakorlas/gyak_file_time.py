import datetime

# ezeket kell importálni
from datetime import datetime, timezone, date, time

print(datetime.now(timezone.utc))

#  datum/idő -lekérdezése időzónával
now = datetime.now(timezone.utc)

print(now.date())

# beadott 0karakterekből dátumot csinál (év,hó,nap)
print(date(2000, 12, 1))

