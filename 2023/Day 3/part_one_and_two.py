import part_one,part_two
import time

time_start = time.time()

part_one.gear_ratios_part_one()
part_two.gear_ratios_part_two()

time_end = time.time()
print(f"Finished in {(time_end - time_start) * 10 ** 3:.02f} ms")