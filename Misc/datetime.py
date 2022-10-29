from datetime import datetime
import pytz

timeZ_Portland = pytz.timezone('US/Pacific')
portlandTime = datetime.now(timeZ_Portland)

timeZ_NYC = pytz.timezone('America/New_York')
nycTime = datetime.now(timeZ_NYC)

timeZ_London = pytz.timezone('Europe/London')
londonTime = datetime.now(timeZ_London)

isPortlandOpen = portlandTime.hour > 9 and portlandTime.hour < 17

if (isPortlandOpen):
    print("Portland office is open")
else:
    print("Portland office is closed")

isnycOpen = nycTime.hour > 9 and nycTime.hour < 17

if (isnycOpen):
    print("NYC office is open")
else:
    print("NYC office is closed")

isLondonOpen = londonTime.hour > 9 and londonTime.hour < 17

if (isnycOpen):
    print("London office is open")
else:
    print("London office is closed")
