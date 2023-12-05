f = open("input.txt", "r")
sum = 0
for line in f:
    d1 = ''
    d2 = ''
    # find first digit
    for char in line:
        #print(ord(char))
        if(47 < ord(char) < 58):
            d1 = char
            break
    # find second digit
    for char in reversed(line):
        if(47 < ord(char) < 58):
            d2 = char
            break
    num = d1 + d2
    print(num)
    sum += int(num)

print(sum)
