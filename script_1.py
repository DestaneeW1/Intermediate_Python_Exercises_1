#Write a function that takes in a list data structure as input. The function should create a new list and only include unique elements of the inputted list. Under the function, write code that calls the function with a test list like so and print out the result. Remember that your code should work for all lists of integers, not just the sample test here.

#I used https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/ 
# I used https://www.geeksforgeeks.org/python-get-unique-values-list/ 
#I received help from Tutoring Center 

my_list = [1, 2, 3, 2, 1, 4]

def unique_list(list1):
   #In the inside parentheses, we turn the list into a set. This allows us to get the unique elements in the list. Then we turn the set back into a list
   return list(set(list1))

#Finally, we print the list with the unique elements
print(unique_list(my_list))
