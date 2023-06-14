#!/usr/bin/python3
from time import sleep

print("We are ready for launch...")
countdown = 11
while True:
    sleep(1)
    countdown -= 1
    print(countdown)

    if countdown == 0:
        print("And we have Liftoff! Singularity X IGHPV(Inter-Galactic Hyper Space Vehicle)!")
        break

print("...")
