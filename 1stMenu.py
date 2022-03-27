#1stMenu
with open("output1st.txt", "a") as f:
    print("Enter Octal Number: ")
    onum = input()

    bnum = int(onum, 8)
    bnum = bin(bnum)

    print("\nEquivalent Binary Value =", bnum, file=f)