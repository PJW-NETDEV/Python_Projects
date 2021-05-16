import sys

print("-" * 15)
print("ArgV Test")
print("-" * 15,"\n")

my_arg_list = sys.argv

print("Arguments Passed Into", my_arg_list[0])
# Print arguments in list except first (filename)
for x in my_arg_list[1:]:
    print(x)

print("\nThank You and Goodnight...")
print("\n" * 2)
