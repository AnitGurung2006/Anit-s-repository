principle=0
rate=0
time=0

while True:
    principle=float(input("Enter the principle: "))
    if principle <= 0:
        print("Principle must be a positive number")
    else:
        break

while True:
    rate=float(input("Enter the rate: "))
    if rate <= 0:
        print("Rate must be a positive number")
    else:
        break
while True:
    time=float(input("Enter the time: "))
    if time <= 0:
        print("Time must be a positive number")
    else:
        break
total=principle*pow((1+rate/100),time)
print(f"Balance after {time} year/s: Rs.{total:.2f}")



