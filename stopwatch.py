#! python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions.
print('Press Enter to begin. Afterwards, press Enter to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

# TODO: Start tracking the lap times.
