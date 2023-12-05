sum = 0

f = open('input.txt', 'r')
for line in f:
    score = 0
    winning_nums = 0
    numbers = line.split(':')[1].split('|')
    for num in numbers[1].split():
        if num in numbers[0].split():
            winning_nums += 1

    score = 0 if winning_nums == 0 else 2 ** (winning_nums -1)
    sum += score

print(sum)
    

