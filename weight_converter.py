weight = input('Enter weight: ')
unit = input('(L)bs or (K)gs: ')
unit = unit.upper()
if unit == 'L':
    w = 0.45 * int(weight)
    print(f"Weight in Kg's is {w}" )
elif unit == 'K':
    w = 2.2 * int(weight)
    print(f"Weight in Lbs is {w}")