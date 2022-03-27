#2ndMenu
with open("output2nd.txt", "a") as f:
    print("Enter Decimal Number: ")
    dnum = input()

    bnum = int(dnum, 10)
    bnum = bin(bnum)

    print("\nEquivalent Binary Value =", bnum, file=f)