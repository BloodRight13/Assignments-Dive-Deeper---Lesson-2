#Task 1: Identify the Greatest
a = float(input("Enter a random number: "))
b = float(input("Enter another random number: "))
c = float(input("Enter the last random number: "))

largest_number = max(a,b,c)
print("The largest number is ", largest_number)

#Task 2:Identify the Smallest
smallest_number = min(a,b,c)
print("The smallest number is ", smallest_number)
#Task 3: Equality Check
if a == b:
    print("These two numbers are equal ", a, b)
elif b == c:
    print("These two numbers are equal ", b, c)
elif a == c:
    print("These two numbers are equal ", a, c)
else:
    print()