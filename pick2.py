import time
from random import shuffle, randint
import pyfiglet

# this script takes output.txt and picks a random winner. Duplicate tags do
# not count

f = open("input.txt", "r", encoding="utf8")

text = f.read()
lines = text.splitlines()
# print(lines)

drawfrom = []

for line in lines:
    drawfrom.append(line)

# print(drawfrom)
shuffle(drawfrom)

def stall():
    print("Gathering Entries")
    time.sleep(1)
    print("Gathering Entries.")
    time.sleep(1)
    print("Gathering Entries..")
    time.sleep(1)
    print("Gathering Entries...")
    time.sleep(1)
    print("Gathering Valid Entries....")

# stall()

for entry in drawfrom:
    print(entry)
    # time.sleep(.0025)

length = len(drawfrom)

print("Total Entries:", length)
time.sleep(1)

def confirm_choice():
    while True:
        confirm = input('Would you like to redraw? [y]Yes or [n]No: ')
        if confirm in ('y', 'n'):
            if confirm is 'y':
                picker()
                return confirm
            else:
                print("\nCONGRATS.")
                return confirm
        else:
            print("\n[y]Yes or [n]No: ")

def picker():
    print("Generating a random number from 1 to", length)
    time.sleep(1)

    x = 0
    for z in range(200):
        x = randint(1, length-1)
        print(x, "    ",  end="\r")
        time.sleep(.015)

    time.sleep(2)
    print(x)

    strin = "Finding that person..."
    for z in range(5):
        print(strin,  end="\r")
        strin += "."
        time.sleep(1)

    ascii_banner = pyfiglet.figlet_format(drawfrom[x])
    print(ascii_banner)
    confirm_choice()

picker()
