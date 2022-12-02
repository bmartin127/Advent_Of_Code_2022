import numpy as np

# opening the file in read mode
readin = open("readin.txt", "r")
  
# reading the file
readin_list = readin.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = readin_list.split("\n")
 # print(data_into_list)
readin.close()
first = ("")
first_value = int()
second = ("")
second_value = int()
added = int()
win_lose_tie = int()
for i in data_into_list:
    split_match = i.split( )
    first = split_match[0]
    second = split_match[1]
 
    if first == "A":
        first_value = 1
    elif first == "B":
        first_value = 2
    elif first == "C":
        first_value = 3

    if second == "X":
        second_value = 1
    elif second == "Y":
        second_value = 2
    elif second == "Z":
        second_value = 3


    if (first_value == 1 and second_value == 2) or (first_value == 2 and second_value == 3) or (first_value == 3 and second_value == 1):
        win_lose_tie = 6
        # print("won")
        # print("------")
        # print(first_value)
        # print(second_value)
        # print(win_lose_tie)
        # print("------")
    elif first_value == second_value:
        win_lose_tie = 3
        # print("draw")
        # print("------")
        # print(first_value)
        # print(second_value)
        # print(win_lose_tie)
        # print("------")
    else:
        win_lose_tie = 0
        print("lose")
        print("------")
        print(first_value)
        print(second_value)
        print(win_lose_tie)
        print("------")
    
    added += second_value + win_lose_tie

print(added)


    


    


            
