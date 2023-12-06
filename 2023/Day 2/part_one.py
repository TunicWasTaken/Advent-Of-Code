import re
import time

time_start = time.time()

fdin = open("input.txt")

MAXRED = 12
MAXBLUE = 14
MAXGREEN = 13

def cube_conumdrum(fdin):
    global MAXRED, MAXBLUE, MAXGREEN
    colors = {"red" : 1, "blue": 2, "green": 3}
    id_sum = 0

    for line in fdin:
        
        line = re.sub(r"[\n]", '', line)
        game_id, game_info = line.split(':')
        game_id = int(game_id.split(' ')[1])
        game_info = game_info.split(';')
        
        current_bag_index = 0

        for bag in game_info:

            current_red_cube = 0
            current_blue_cube = 0
            current_green_cube = 0

            cubes = bag.split(',')

            for cube in cubes:

                cube = cube.split(' ')

                match colors[cube[2]]:
                    case 1:
                        current_red_cube = int(cube[1])
                    
                    case 2:
                        current_blue_cube = int(cube[1])

                    case 3:
                        current_green_cube = int(cube[1])
            
            if current_red_cube <= MAXRED and current_blue_cube <= MAXBLUE and current_green_cube <= MAXGREEN:
                current_bag_index += 1

        
        if current_bag_index == len(game_info):
            id_sum += game_id

    return id_sum


result = cube_conumdrum(fdin)
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")