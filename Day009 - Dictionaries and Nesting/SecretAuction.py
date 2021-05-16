import os

clear = lambda: os.system("clear")
clear()

nameBid = {}
stop = False

while not stop:
    name = input("What name would you like to place on your bid?: ")
    bid = float(input("What is your bid?: $"))

    nameBid[name] = bid

    peopleNeedingToBid = input(
        "Thank you for your bid, Are there any others needing to bid? Yes or No "
    ).lower()

    if peopleNeedingToBid == "no":
        stop = True

    clear()

personWithHighestBid = ""
highestBid = 0

for name in nameBid:
    bid = nameBid[name]
    if bid > highestBid:
        personWithHighestBid = name
        highestBid = bid

print(f"{personWithHighestBid} is the winner with a bid of ${round(highestBid,2)}")
