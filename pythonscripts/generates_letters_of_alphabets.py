Create a Scripts that generates a file where all letters of the alphabets are listed three in each line.

ex. abc
    def
    ghi 

import string
letters1 = string.ascii_lowercase + " "
slice1 = letters1[0::3]
slice2 = letters1[1::3]
slice3 = letters1[2::3]
with open("letters1.txt","w") as file:
    for s1,s2,s3 in zip(slice1,slice2,slice3):
        file.write(s1 + s2 + s3 + "\n")


