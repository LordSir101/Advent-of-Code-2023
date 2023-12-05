# convert input into 2d list
diagram = []
f = open('input.txt', 'r')
for line in f:
    diagram.append([c for c in line])

sum = 0

# loop through every character in diagram
for row_num, row in enumerate(diagram):
    for idx, char in enumerate(row):
        # check if char is num
        if(47 < ord(char) < 58):

            adjacent_symbols = []

            row_above = row_num -1
            row_below = row_num +1
            left = idx -1
            right = idx +1

            # find all adjacent characters
            if(row_above >= 0):
                adjacent_symbols.append(diagram[row_above][idx])
                if(left >= 0):
                    adjacent_symbols.append(diagram[row_above][left])
                if(right < len(row)):
                    adjacent_symbols.append(diagram[row_above][right])

            if(left >= 0):
                adjacent_symbols.append(diagram[row_num][left])
            if(right < len(row)):
                adjacent_symbols.append(diagram[row_num][right])

            if(row_below < len(diagram)):
                adjacent_symbols.append(diagram[row_below][idx])
                if(left >= 0):
                    adjacent_symbols.append(diagram[row_below][left])
                if(right < len(row)):
                    adjacent_symbols.append(diagram[row_below][right])

            #check if it is near a symbol
            adjacent_to_symbol = False
            for symbol in adjacent_symbols:
                if((32 < ord(symbol) < 48 or 59 < ord(symbol) < 65) and ord(symbol) != 46):
                    adjacent_to_symbol = True
                    break
            
            # get the whole number that is near the symbol
            if(adjacent_to_symbol):
                num_string = ''
                left_idx = idx
                right_idx = idx

                # move the left idx left and right idx right until there is no longer a digit character.  Then, all characters between those idx makes up the multi digit number
                while(47 < ord(diagram[row_num][left_idx-1]) < 58):
                    left_idx -= 1
                while(47 < ord(diagram[row_num][right_idx+1]) < 58):
                    right_idx += 1
                
                for i in range(left_idx, right_idx+1):
                    num_string += diagram[row_num][i]
                    diagram[row_num][i] = '.'

                sum += int(num_string)

print(sum)
            
            