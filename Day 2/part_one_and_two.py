import re

fdin = open("input.txt")

MAXRED = 12
MAXBLUE = 14
MAXGREEN = 13

def cube(fdin):
    global MAXRED, MAXBLUE, MAXGREEN
    colors = {"red" : 1, "blue": 2, "green": 3}
    sum_minimum_cubes = 0
    id_sum = 0

    for line in fdin:
        
        line = re.sub(r"[\n]", '', line)
        game_id, game_info = line.split(':')
        game_id = int(game_id.split(' ')[1])
        game_info = game_info.split(';')

        current_bag_index = 0

        min_red = 0
        min_blue = 0
        min_green = 0
        
        for bag in game_info:

            current_red_cube = 0
            current_blue_cube = 0
            current_green_cube = 0

            cubes = bag.split(',')

            for cube in cubes:

                cube = cube.split(' ')

                match colors[cube[2]]:
                    case 1:
                        min_red = max(int(cube[1]), min_red)
                        current_red_cube = int(cube[1])
                    
                    case 2:
                        min_blue = max(int(cube[1]), min_blue)
                        current_blue_cube = int(cube[1])

                    case 3:
                        min_green = max(int(cube[1]), min_green)
                        current_green_cube = int(cube[1])

            if current_red_cube <= MAXRED and current_blue_cube <= MAXBLUE and current_green_cube <= MAXGREEN:
                current_bag_index += 1

        
        if current_bag_index == len(game_info):
            id_sum += game_id

        sum_minimum_cubes += (min_red * min_blue * min_green)
        
    
    return id_sum, sum_minimum_cubes

part_one, part_two = cube(fdin)
print(f"Part One Result: {part_one}; Part Two Result: {part_two}")