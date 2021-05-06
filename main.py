# first program

# ask for user's name
print("What is your first and last name?")
# user enter first and last Name
n= str(input())
#print user's first and last name in reverse order
print(n[::-1])


# second program

# allow user to input number
n= int(input())
# detrmine if number is even, odd or zero
if n == 0:
  # notify number is a zero
  print("This number is a zero.")
elif n %2 == 0:
  #notify number is even
  print("This number is even.")
else:
 # notify number is odd
  print("This number is odd.")


# third program

#take day number, convert to actual date

d= int(input())

m= int(d/12)
n= int(d%31)

if m == 1:
  print("Jan", n)

elif m == 2:
  print("Feb",n)

elif m == 3:
  print("Mar",n)

elif m == 4:
  print("Apr",n)

elif m == 5:
  print("May",n)

elif m == 6:
  print("Jun",n)

elif m == 7:
  print("July",n)

elif m == 8:
  print("Aug",n)

elif m == 9:
  print("Sept",n)

elif m == 10:
  print("Oct",n)

elif m == 11:
  print("Nov",n)

elif m == 12:
  print("Dec",n)


# fourth program

# take 5,4,3,2,1, print new row subratcing last number from each until only 5 remains
for i in range (5,0,-1):
  for j in range (i,0,-1):
    print(j, end=" ")
  print()


# fifth program

# same as fourth, but let user print max number

n= int(input())

for i in range (n,0,-1):
  for j in range (i,0,-1):
    print(j, end=" ")
  print()