#Take in a string from the user and pass it as input to a function. Have the function return a dict which keeps count of each letter (in lowercase) in the string, excluding spaces. Print out this dict.

#I copied the code from https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/ 
#Specifically the code under Method #1

input1 = input("Enter a string: ")
counter = {}

for i in input1:
    #We iterate through the string and add elements from input_1 into the dictionary named counter, if the element is already in the dictionary, we increase the value of that element in the dictionary 
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
        
print(counter)
        
