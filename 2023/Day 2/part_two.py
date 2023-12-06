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
    sum_minimum_set_cubes = 0

    for line in fdin:
        
        line = re.sub(r"[\n]", '', line)
        game_id, game_info = line.split(':')
        game_id = int(game_id.split(' ')[1])
        game_info = game_info.split(';')

        min_red = 0
        min_blue = 0
        min_green = 0
        
        for bag in game_info:

            cubes = bag.split(',')

            for cube in cubes:

                cube = cube.split(' ')

                match colors[cube[2]]:
                    case 1:
                        min_red = max(int(cube[1]), min_red)
                    
                    case 2:
                        min_blue = max(int(cube[1]), min_blue)

                    case 3:
                        min_green = max(int(cube[1]), min_green)

        
        sum_minimum_set_cubes += (min_red * min_blue * min_green)
        
    
    return sum_minimum_set_cubes

result = cube_conumdrum(fdin)
time_end = time.time()
print(f"Result: {result}, Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")