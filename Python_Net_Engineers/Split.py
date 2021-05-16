my_ip_address = '192.168.1.25'
print ('Split Ip address on "."')
print(my_ip_address.split("."))
print()

# Split whitespace
print('Split WhiteSpace')
my_sentence = "This is my very long sentence with lots of words."
my_sentence_split = my_sentence.split()
print("Orginal String: ")
print("Split: ")
print(my_sentence.split())

print()
print()

# Split Lines
str_paragraph = "Same text over multiple lines \nSystem Version PJW 15.5.4 \nOS Magny-Cours \nDate: 10/12/2020 \nLast Reload: Never"
print("Orginal String: " + str_paragraph)
print("SplitLines: ")
print(str_paragraph.split("\n"))