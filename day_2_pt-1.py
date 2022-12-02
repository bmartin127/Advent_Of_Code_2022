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

    elif first == "X":
        first_value = 1

    elif first == "Y":
        first_value = 2

    elif first == "Z":
        first_value = 3

    if second == "A":
        second_value = 1

    elif second == "B":
        second_value = 2

    elif second == "C":
        second_value = 3

    elif second == "X":
        second_value = 1

    elif second == "Y":
        second_value = 2

    elif second == "Z":
        second_value = 3

  
    if first_value < second_value:
        win_lose_tie = 6
        print("------")
        print(second_value)
        print(win_lose_tie)
        print("------")
        print("won")

    elif first_value == second_value:
        win_lose_tie = 3
        print("------")
        print(second_value)
        print(win_lose_tie)
        print("------")
        print("draw")

    elif first_value > second_value:
        win_lose_tie = 0
        print("------")
        print(second_value)
        print(win_lose_tie)
        print("------")
        print("lose")
    
    added = (added + second_value + win_lose_tie)

    print(added)


    


    


            
