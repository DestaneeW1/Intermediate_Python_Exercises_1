#Write a function that takes in two dict data structures as input. Both dicts map str->int (the keys are strings and the values are integers). The function should compute a new dict which combines the two dicts by summing the values for the common keys. Keys that are not common should be left out. Use the following code to test your function, but remember that your function should for all str->int dict inputs, not just the test here.

#I used https://www.geeksforgeeks.org/python-combine-two-dictionary-adding-values-for-common-keys/ 
#I received help from the Tutoring Center 

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
dict_3 = {}

#We iterate through the second dictionary, then we iterate through the first one by comparing the two dictionaries
#If both dictionaries have the same letter, we add the numbers together and put the results inside an empyt dictionary named dict_3
#Finally we print dict_3 
for i in my_dict_2:
    if i in my_dict_1:
        dict_3[i] = my_dict_2[i] + my_dict_1[i]

print(dict_3)

