Write the script that extract letters from the 26 text files and put the letters in a list.(Pervious example continues) eg: ['a','b',.....'z']

import glob
letters3 =[]
file_list = glob.glob("letters3/*.txt")
print(file_list)
for file_name in file_list:
    with open(file_name, "r")as file:
        letters3.append(file.read().strip("\n"))
        
        
print(letters3)
        
