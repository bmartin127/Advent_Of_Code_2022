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
length = len(data_into_list)
i = 0
while i < length:
    sack_1 = set(list(data_into_list[i]))
    sack_2 = set(list(data_into_list[i+1]))
    sack_3 = set(list(data_into_list[i+2]))

    i = i + 3
    matching.append(sack_1.intersection(sack_2, sack_3))
    print((sack_1.intersection(sack_2, sack_3)))
    aphabet = "1abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters = [*aphabet]
    
matching = list(matching)
for t in matching:
    #print (letters.index(t))
    added = added + letters.index((list(t))[0])
print("answer", added)
