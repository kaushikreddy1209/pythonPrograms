def consecutive_repetitions_string(short_s,long_s):
    if len(long_s)<len(short_s) or len(short_s)==0 or len(long_s)==0:
        print("0")
    max_count=0
    current_count=0
    index=0
    while index in range(len(long_s)):
        if long_s[index:].startswith(short_s):
            current_count+=1
            max_count=max(current_count,max_count)
            index+=len(short_s)
        else:
            current_count=0
            index+=1
    return max_count

short_string=input("Enter short string: ")
long_string=input("Enter long string: ")
result = consecutive_repetitions_string(short_string,long_string)
print(result)