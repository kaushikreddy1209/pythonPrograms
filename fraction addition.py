n=int(input("Enter the value of n: " ))
i=1
sum=0
while i<=n:
    sum+=1/i
    sum = round(sum,2)
    i+=1
print(f'The sum of all the fractions is: {sum}')