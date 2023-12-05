# possible cubes to pull
bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

sum = 0

f = open("input.txt", "r")
for game in f:
    possible = True
    game_num = int(game.split(':')[0].split()[1])
    # get all sets from each game
    sets = game.split(':').pop(1).split(';')

    # split each set into cube color and the number of that color
    for set in sets:
        if(possible):
            cubes = set.split(',')
            # get the number of each cube pulled. If the number of cubes pulled is more than in the bag, the game is not possible 
            for cube in cubes:
                color = cube.split()
                num_cubes = int(color[0])
                if(num_cubes > bag[color[1]]):
                    possible = False
                    break
    if(possible):
        sum += game_num

print(sum)
    