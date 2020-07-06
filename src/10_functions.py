# Write a function is_even that will return true if the passed-in number is even.

def is_even(integer):
    if type(integer) == int and (integer % 2) == 0:
        return True
    elif  type(integer) == int and (integer % 2) != 0:
        return False
    else:
        return TypeError("Expected integer, received non-integer input.")


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if is_even(num) == True:
    print("Even!")
elif is_even(num) == False:
    print("Odd")
