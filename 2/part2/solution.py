# minimum cubes to make game possible
bag = {
    'red': 0,
    'green': 0,
    'blue': 0
}

sum = 0

f = open("input.txt", "r")
for game in f:
    # get all sets from each game
    sets = game.split(':').pop(1).split(';')

    # split each set into cube color and the number of that color
    for set in sets:
        cubes = set.split(',')
        # get the number of each cube pulled. 
        for cube in cubes:
            color = cube.split()
            num_cubes = int(color[0])
            # place the highest number of cubes of each color per game in bag
            if(num_cubes > bag[color[1]]):
                bag[color[1]] = num_cubes

    power = 1
    for key, value in bag.items():
        power *= value
    sum += power

    bag = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    
print(sum)
    