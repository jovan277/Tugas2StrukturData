#3rdMenu
with open("output3rd.txt", "a") as f:
    print("Enter Hexadecimal Number: ")
    hdnum = input()

    bnum = int(hdnum, 16)
    bnum = bin(bnum)

    print("\nEquivalent Binary Value =", bnum, file=f)