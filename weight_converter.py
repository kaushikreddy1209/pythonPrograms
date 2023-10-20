weight = input('Enter weight: ')
unit = input('(L)bs or (K)gs: ')
if unit == 'L' or 'l':
    w = 0.45 * int(weight)
    print(f"Weight in Kg's is {w}" )
elif unit == 'K' or 'k':
    w = 2.2 * int(weight)
    print(f"Weight in Lbs is {w}")