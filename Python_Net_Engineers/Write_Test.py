print("-" * 20)
print("Write To Files")
print("-" * 20,"\n")

f = open("F:\_PythonFiles\My-FirstPythonTextFile222.txt","w")

line1 = input("Line1:")
line2 = input("Line2:")
line3 = input("line3")

f.write("My Text File Pre-Amble")
f.write(line1)
f.write(line2)
f.write(line3)
# Flush File
p = input("Press Enter To Flush File")
f.flush()
p = input("Press Enter To Close File")
# F.Close
