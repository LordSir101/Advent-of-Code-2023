f = open("input.txt", "r")
sum = 0
digits = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}

for line in f:
    i1 = 0
    i2 = 0
    d1 = ''
    d2 = ''
    # find first digit
    for idx, char in enumerate(line):
        if(47 < ord(char) < 58):
            i1 = idx
            d1 = char
            break
    # find second digit
    for idx, char in enumerate(reversed(line)):
        if(47 < ord(char) < 58):
            i2 = idx
            d2 = char
            break
    
    # find first digit written as word, check if it comes before first digit
    for key in list(digits.keys()):
        idx = line.find(key)
        if(idx < i1 and idx >=0):
            i1 = idx
            d1 = digits[key]
    
    # check last digit as word
    for key in list(digits.keys()):
        idx = line[::-1].find(key[::-1])
        if(idx < i2 and idx >=0):
            i2 = idx
            d2 = digits[key]

    num = d1 + d2
    sum += int(num)

print(sum)


