from thisapidoesnotexist import get_person
import requests
import time

n  = int(input("Number of photos:"))

for x in range(1, n + 1):
    person = get_person()
    person.save_image(f"{x}.jpeg")
    print(x)
    time.sleep(3)
