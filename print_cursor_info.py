import pyautogui, sys
print('Press Ctrl-C to quit.')
game_region = [473, 303, 1432, 897]
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        if(x >= game_region[0] and x <= game_region[2] and y >= game_region[1] and y <= game_region[3]):
            gameX = x - game_region[0]
            gameY = y - game_region[1]
            positionStr += ' |  GameX: ' + str(gameX).ljust(4) + ' GameY: ' + str(gameY).ljust(4)
        positionStr += '\n' + str(pyautogui.pixel(x,y))
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')