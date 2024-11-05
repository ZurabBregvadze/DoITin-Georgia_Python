##################################
#Start of Task 1
##################################
print("შეიყვანეთ მთელი რიცხვი:")

Integer1 = int(input("რიცხვი="))

A = Integer1%2

if A==0:
    print( "რიცხვი ლუწია" )
else:
    print( "რიცხვი კენტია" )

#End of Task 1
##################################

##################################
#Start of Task 2
##################################
print("შეიყვანეთ ტექსტი:")

text = input()

text1 = "small"

text2 = "tall"

text3 = "middle"

if text1 in text:
    print (text1)
if text2 in text:
    print (text2)
if text3 in text:
    print (text3)
else:
    print("მოცემულ ტექსტში ეს სამი სიტყვა არ მოიძებნა")

#End of Task 2
##################################


##################################
#Start of Task 3
##################################
print("შეიყვანეთ პირველი მთელი რიცხვი:")

Integer1 = int(input("რიცხვი_1="))

print("შეიყვანეთ მეორე მთელი რიცხვი:")

Integer2 = int(input("რიცხვი_2="))

operator = operator (input("შეიყვანეთ ოპერატორი: ") )

# A = Integer1 operator Integer2

print( Integer1, operator, Integer2 )

#End of Task 3
##################################

