print("-" * 15)
print("Read File Test")
print("-" * 15,"\n")

f = open("F:\_PythonFiles\PJWCSW1.txt")
my_text_file_contents = f.read()
f.close()

print(my_text_file_contents)
