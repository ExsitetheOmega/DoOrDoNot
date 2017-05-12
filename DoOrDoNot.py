import random
def DrawBoard(x):
    print("=" * 12)
    print("=" + " " * 10 + "=")
    print("=" + " " * 10 + "=")
    print("=" + " " * 3 + str(x) + " " * 3 + "=")
    print("=" + " " * 10 + "=")
    print("=" + " " * 10 + "=")
    print("=" * 12)

while True:
    diffc = input("What chances?(1/10) on true ")
    randomnum = random.randint(1,10)
    if diffc == "Stop" or diffc == "stop" or diffc == "quit":
        break
    else:
        if randomnum >= int(diffc):
            wn = "Wel "
        else:
            wn = "Niet"
    DrawBoard(wn)
print("Programm Shutting down..")
exit()


