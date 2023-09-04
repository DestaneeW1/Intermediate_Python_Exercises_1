#Take in 5 int inputs from the user and add them together. The catch is that you can no longer assume that what the user enters is a valid int. If the user enters an invalid input, print an error message and make the user input the int again until all 5 int values are entered correctly. Print the resulting sum.

#I used https://stackoverflow.com/questions/48738218/python-3-create-error-if-user-input-is-not-an-integer#:~:text=If%20you%20cast%20the%20input,was%20not%20a%20valid%20integer.) 
#This helped me with the error message

#I used https://www.geeksforgeeks.org/sum-function-python/
#This function helped me sum up all the int elements in list_1

list_1 = []
total = 0

for i in range (5):
    try: 
        input_1 = int(input('Enter int # ' + '' + str(i+1) + ': '))
        list_1.append(input_1)
    except ValueError:
        print("Invalid input. Please enter an int.")
        input_1 = int(input('Enter int # ' + '' + str(i+1) + ': '))
        list_1.append(input_1)
print('Your sum is', (sum(list_1)))




