cards = []
f = open('input.txt', 'r')
for line in f:
    cards.append(line)

# fancy memoization
results = {

}

def getCopies(idx, cards):
    # calculate the number of winning numbers we have
    card = cards[idx] # current card
    winning_nums = 0
    numbers = card.split(':')[1].split('|')
    for num in numbers[1].split():
        if num in numbers[0].split():
            winning_nums += 1
    
    if winning_nums == 0:
        return 0
    
    # each winning number gets a copy of the next n cards
    for i in range(1, winning_nums+1):
        # check if we have calculated the copies for this card already
        if(idx+i in results.keys()):
            num_copies = results[idx+i]
        else:
            # save the results in the table
            num_copies = getCopies(idx+i,cards)
            results[idx+i] = num_copies

        winning_nums += num_copies
    return winning_nums

copies = 0
for idx, card in enumerate(cards):
    if(idx in results.keys()):
        copies += results[idx] + 1 # add one extra since the original card counts as a copy
    else:
        num_copies = getCopies(idx,cards)
        results[idx] = num_copies
        copies += num_copies + 1 

print(copies)
    

