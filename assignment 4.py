#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      singh
#
# Created:     19-07-2023
# Copyright:   (c) singh 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------


marks =["maths" , "95" , "chemistry" , "98"]
marks.append("physics")
marks.append(97)
print(marks)
marks.insert(0 , "english")
marks.insert(1 , "99")
print(marks)
print("maths" in marks)
print(len(marks)/2)
marks.clear()
print(marks)
i=0
while i < len(marks):
    print(marks[i])
    print(marks[i+1])
    i=i+2