import numpy as np

# opening the file in read mode
readin = open("readin.txt", "r")
  
# reading the file
readin_list = readin.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = readin_list.split("\n")
# 
# print(data_into_list)
readin.close()


readin_array = np.genfromtxt("readin.txt", dtype=str,
                     encoding=None, delimiter="")
# print(readin_array)
added = int(0)
answer = int(0)
calories = []
for i in data_into_list:
    if i == (""):
        calories.append(added)


        if added > (answer ):
            answer = added
        added = 0
    else:
        added = added + int(i)
print("answer is")
calories.sort()
finanswer = calories[len(calories) - 1] + calories[len(calories) - 2] + calories[len(calories) - 3]
print (finanswer)



