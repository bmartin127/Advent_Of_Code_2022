import string
# opening the file in read mode
readin = open("readin.txt", "r")
  
# reading the file
readin_list = readin.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = readin_list.split("\n")
# print(data_into_list)
first_compartment = ""
second_compartment = ""
matching = []
added = 0
for i in data_into_list:
    first_compartment, second_compartment = i[:len(i)//2], i[len(i)//2:]
    second_compartment_range = list(second_compartment)
    first_compartment_range = list(first_compartment)
    matching = [element for element in first_compartment_range if element in second_compartment_range]
    matching = [*set(matching)]
    matching_values = []
    aphabet = "1abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = [*aphabet]
    for t in matching:
        print (letters.index(t))
        matching_values.append(letters.index(t))
        added = (added + letters.index(t))
print("answer", added)


