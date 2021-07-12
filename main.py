# print("hello")
# fullname = input("what is you full name? ")
# age = input("how old are you? ")
# favorite_act = input("what is your favorite activity? ")

# #Concatination 
# print("your name is " + fullname)
# print("Your are", age, "years old")
# print("Your favorite activity is " + favorite_act)
 
#--------------------------------------------------------
#data convertions 
# var1 = 1 #integer value
# var_string = str(var1)
# print(var1)
# print(var_string)

#---------------------------------------------------------
#get perimeter of a rectangle 
#User inputs length and width 
#console outputs perimeter 

# perimeter = input("enter a perimeter of a rectangle: ")
# l_w = input("enter the length and width of the rectangle from the primeter (l, w:)")
# print("the perimeter of the rectangle is " + perimeter)
# print("the length and width of the rectangle is " + l_w)

#string manipulation 
#concatination -> "hello" "world" -> "hello world"
#length -> "hello" -> len("hello") -> 5 
#upper -> cornvert all characters to uppercase "hello" -> "HELLO"
#lower ->converts all characters the lowercase "HELLO" -> "hello"

string1 = "hello"
string2 = "HELLO"

print(string1.upper())
print(string2.lower())
print(len(string1))
print(string1 + string2)

#string formating 
name = input ("Enter name: ")
number = int(input("Enter number: "))
print(f"Your name is {name} and your favorite number is {number}")
name2 = "Bella"
number2 = "13"
print("my name is {0}, I am {1}".format(name2,number2))


