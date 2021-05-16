import time
print("-" * 15)
print("Basic If")
print("-" * 15,"\n")

var1 = int(input("Set Number:"))

if var1 == 5:
    print("My favourite number too.")
elif var1 == 44:
    print("Lewis Hamilton's car number")
else:
    print("meh, number " + str(var1) + " means nothing to me.")

time.sleep(2)
print("\nThank You and Goodnight...")
time.sleep(2)
print("\n" * 1)
