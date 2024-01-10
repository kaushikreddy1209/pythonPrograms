x=input("Enter your email: ")
a=x.find('@') #Find position of '@' in the string
b=x.rfind(".") #Find the position of '.' in the string and find it from the right end
print(f"Your email service is:", x[a+1:b].capitalize()) #capitalize the first letter of the result
