Create a Scripts that generates a 26 text files named a.txt,b.txt and so on up to z.txt.each file contains a letter reflections its filename. So, a.txt will contain letter a,b.txt will contain letter b and so on.

import string,os
if not os.path.exists("letters3"):
    os.makedirs("letters3")
for letter in string.ascii_lowercase:
    with open("letters3/"+letter+ ".txt","w")as file:
        file.write(letter+'\n')