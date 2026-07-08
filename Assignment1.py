#Q1
a=5
b=10
res=a+b
print("The sum of a and b is:", res)

#Q2

a=20
b=20
res=a<=b
print("The value of a is less than or equal to b:", res)

result = a and b
print("Using and operator:", result)

or_result = a or b
print("Using or operator:", or_result)

if a and b:
    print("Both a and b have values.")
else:
    print("One of the values is false or empty.")

if a or b:
    print("At least one of a or b has a value.")
else:
    print("Both a and b are false or empty.")


#Q3

a=20
b=4
lol=a//b
print("The value of a divided by b is:", lol)

#Q4

num = "4578"
print("The number is:",num[0])
       

#Q5

num = "4578"
print("The number is:",num[3])
       

#Q6

a=200
b=13
res=a+b
res1=a%b
print("The sum of a and b is:", res)
print("The remainder of a and b is:", res1)


#Q7

a=200
b=13
res=a*b
print("The product of a and b is:", res)

#Q8

A = int(input("Enter marks in subject A: "))
B = int(input("Enter marks in subject B: "))
C = int(input("Enter marks in subject C: "))

total_marks = A + B + C
average = total_marks / 3

print("Total marks:", total_marks)
print("Average marks:", average)

