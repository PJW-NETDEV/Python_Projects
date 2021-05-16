print("-" * 20)
print("Read File Line By Test")
print("-" * 20,"\n")

f = open("F:\_PythonFiles\PJWCSW1.txt")

for x in range(5):
  my_text_file_contents = f.readline()
  print(my_text_file_contents)
  Prompt = input("Next...")

f.close()