from datetime import datetime, timedelta
import time


def send_email():
    for i in range(10000):
        pass


start = time.time()
send_email()
end = time.time()
duration = start - end
print(duration)

# Working with datetimes


dt1 = datetime(2020, 4, 12)
dt2 = datetime.now()
dt = datetime.strptime("2020/12/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))
print(dt1 > dt2)

# working with timedeltas
dt1_1 = datetime(2020, 4, 12) + timedelta(days=1, seconds=1000)
print(dt1_1)
dt2_2 = datetime.now()
duration_1 = dt2_2 - dt1_1
print(duration_1)
print("days", duration_1.days)
print("seconds", duration_1.seconds)
print("total_seconds", duration_1.total_seconds())