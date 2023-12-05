# convert input into 2d list
diagram = []
f = open('input.txt', 'r')
for line in f:
    diagram.append([c for c in line])

sum = 0

# loop through every character in diagram
for row_num, row in enumerate(diagram):
    for idx, char in enumerate(row):
        # check if char is *
        if(char == '*'):
            adjacent_symbols = []

            row_above = row_num -1
            row_below = row_num +1
            left = idx -1
            right = idx +1

            part_nums = []

            # check each character adjacent to the gear
            for i in range(row_above, row_below+1):
                for j in range(left, right +1):
                    if(0 <= i < len(diagram) and 0 <= j < len(row)): 
                        # check if current char is a digit
                        if(47 < ord(diagram[i][j]) < 58):
                            num_string = ''
                            left_idx = j
                            right_idx = j

                            # move the left idx left and right idx right until there is no longer a digit character.  Then, all characters between those idx makes up the multi digit number
                            while(47 < ord(diagram[i][left_idx-1]) < 58):
                                left_idx -= 1
                            while(47 < ord(diagram[i][right_idx+1]) < 58):
                                right_idx += 1

                            
                            for k in range(left_idx, right_idx+1):
                                num_string += diagram[i][k]
                                diagram[i][k] = '.'

                            part_nums.append(num_string)
            
            # if the gear was adjacent to two part nums, multiply and add to the sum
            if(len(part_nums) == 2):
                ratio = int(part_nums[0]) * int(part_nums[1])
                sum += ratio
                
print(sum)
            
            