import pyautogui as pag
import cv2 as cv
import numpy as np
import time
from screeninfo import get_monitors
import PySimpleGUI as sg
import multiprocessing

my_window = ''

# left, top, width, height
GAME_REGION = (442, 303, 996, 594)
FISHING_CIRCLE_REGION = (950, 421, 440, 301)

FISH_BAR_LOCATION = (788,849)
FISH_BAR_COLOR = (213, 211, 236)

FISH_BAIT_BORDER_COLOR = (22,44,60)
FISH_BAIT_BORDER_LOC = (566,860)


RETURN_HOME = (1366, 840)
RETURN_HOME_COLOR = (232,224,200)
FISHING_EXIT = (1390, 342)

BAIT_BORDER_LOC = (592, 850)
BAIT_BORDER_COLOR = (117, 142, 56)

CASH_REGISTER = (733, 841)
CASH_REGISTER_COLOR = (197, 239, 231)
FIRST_SELL_ITEM = (740, 578)
SELL_BUTTON = (1161, 754)
SELL_CONFIRM_BUTTON = (1006, 720)
SELL_DECLINE_BUTTON = (1014, 753)

SAVE_CONFIRM = (950, 718)

LEAVE_HOUSE = (510, 856)

CAMERA_RIGHT = (1369, 653)
CAMERA_LEFT = (533, 650)

ENTER_SNACK_SHOP = (764, 420)
CONFIRM_ENTER = (867, 681)
TOMATO_LOCATION = (1167, 539)
PLUS_BUTTON = (1012, 643)
SHOP_BUY_BUTTON = (948, 761)

FISHINGVIEW = (1151, 801)
FISHINGVIEWCOLOR = (170, 221, 227)
ENTER_FISHING = (1185, 531)
FISHING_ACCEPT_BUTTON = (956, 677)
FISHING_ACCEPT_COLOR = (91, 191, 76)

REFRESH_BUTTON = (86, 51)
LOGIN_BUTTON = (1021, 595)
LOGIN_BUTTON_COLOR = (192, 163, 54)
SIGN_IN_BUTTON = (974, 729)

STAD_RACE_POS_Y = 840
STAD_RACE_POS_XSTART = 975
STAD_RACE_JUMP_COLOR = (155,168,163)
FINISH_BUSH_POS = (751,830)
FINISH_BUSH_POS_2 = (747,830)
FINISH_BUSH_COLOR = (255,255,255)

TRADE_DECLINE_BUTTON = (1144,637)
LEVEL_UP_ACCEPT_BUTTON = (950, 770)
CLOSE_PROFILE_BUTTON = (1207, 478)


# def main():
#     if(pag.pixelMatchesColor(LOGIN_BUTTON[0],LOGIN_BUTTON[1],LOGIN_BUTTON_COLOR)):
#         login()
#         travelToFishing()
#     while True:
#         fishingLoop()
#         sellFish()
#         saveGame()
#         restock()
#         refresh()
#         login()
#         travelToFishing()

def stopInturruptions(declineTrades):
    while True:

        if(declineTrades):
            declineTrade()

        acceptLevelup()
        closeProfile()

def declineTrade():
    if pag.locateOnScreen("trade_request.PNG"):
        print("DECLINING TRADE")
        click(TRADE_DECLINE_BUTTON)
def acceptLevelup():
    if pag.locateOnScreen("level_up.PNG"):
        print("ACCEPT LEVEL UP")
        click(LEVEL_UP_ACCEPT_BUTTON)
def closeProfile():
    if pag.locateOnScreen("profile_open.PNG"):
        print("CLOSING PROFILE")
        click(CLOSE_PROFILE_BUTTON)

def racingLoop():
    while True:
        time.sleep(1.5) # Added delay, to close level up etc
        ui_update_status("ENTER STATIUM")
        enterStadium()
        ui_update_status("WAITING RACE START")
        waitStadiumRaceStart()
        ui_update_status("RACING")
        stadiumRacing()
        

# Auto Statium
def enterStadium():
   while(not pag.locateOnScreen("stadium_lobby.PNG",confidence=0.8)):
    click((720,420))
    time.sleep(0.5)
    click(CONFIRM_ENTER)
    time.sleep(1.5)

def waitStadiumRaceStart():
    while(pag.pixelMatchesColor(RETURN_HOME[0],RETURN_HOME[1],RETURN_HOME_COLOR)):
        time.sleep(0.2)
        print("Waiting for race to start")
    time.sleep(2)

def stadiumRacing():
    bushcount = 0
    while(bushcount < 5):
        # Jump over obstacle
        if(pag.pixelMatchesColor(STAD_RACE_POS_XSTART, STAD_RACE_POS_Y, STAD_RACE_JUMP_COLOR)):
            click((950,600))

        elif pag.pixelMatchesColor(FINISH_BUSH_POS[0],FINISH_BUSH_POS[1], FINISH_BUSH_COLOR) or pag.pixelMatchesColor(FINISH_BUSH_POS_2[0],FINISH_BUSH_POS_2[1], FINISH_BUSH_COLOR):
            bushcount += 1
            time.sleep(0.2)
            
        else:
            bushcount = 0
    print("STOPPED RACING")
    time.sleep(3)
    click(FISHING_EXIT)
    time.sleep(2)



    # BROKEN, FIX THIS LATER, THEN CONVERT ALL COORDS TO LOCAL COORDS
# def findGameWindow():
#     mon0 = get_monitors()[0]
#     center = (mon0.width / 2, mon0.height / 2)
#     cPos = center

#     # Find left bound
#     while(not pag.pixelMatchesColor(cPos[0], cPos[1], (255,255,255))):
#         cPos[0] -= 1
#     cPos[0] += 1 # re-add one, so we're back within the play space

#     # Find top bound
#     while(not pag.pixelMatchesColor(cPos[0], cPos[1],(255,255,255))):
#         cPos[1] -= 1
#     cPos[1] += 1

#     topLeftBound = cPos

#     # Calculate half the width and height of the area
#     halfAreaX = center[0] - cPos[0]
#     halfAreaY = center[1] - cPos[1]

#     bottomRightBound = (cPos[0] + (halfAreaX * 2), cPos[1] + (halfAreaY * 2))
#     print("Found game area at: " + topLeftBound + ", " + bottomRightBound)
#     return (topLeftBound, bottomRightBound)

def refresh():
    click(REFRESH_BUTTON)
    
def login():
    while(not pag.pixelMatchesColor(LOGIN_BUTTON[0],LOGIN_BUTTON[1],LOGIN_BUTTON_COLOR)):
        time.sleep(0.5)
    click(LOGIN_BUTTON)
    time.sleep(0.5)
    click(SIGN_IN_BUTTON)
    while(not pag.pixelMatchesColor(CASH_REGISTER[0],CASH_REGISTER[1],CASH_REGISTER_COLOR)):
        time.sleep(0.5)
    click(LEAVE_HOUSE)

def travelToFishing():
    while(not pag.pixelMatchesColor(RETURN_HOME[0],RETURN_HOME[1],RETURN_HOME_COLOR)):
        time.sleep(0.2)
    moveCamRight(5)
    while(not pag.pixelMatchesColor(FISHINGVIEW[0],FISHINGVIEW[1],FISHINGVIEWCOLOR)):
        moveCamRight(5)
        time.sleep(0.5)
    click(ENTER_FISHING)
    time.sleep(0.5)
    click(CONFIRM_ENTER)
    while(not pag.pixelMatchesColor(FISHING_ACCEPT_BUTTON[0],FISHING_ACCEPT_BUTTON[1],FISHING_ACCEPT_COLOR)):
        time.sleep(0.2)
    click(FISHING_ACCEPT_BUTTON)

def restock():
    click(LEAVE_HOUSE)
    while(not pag.pixelMatchesColor(RETURN_HOME[0],RETURN_HOME[1],RETURN_HOME_COLOR)):
        time.sleep(0.2)
    moveCamRight(4)
    moveCamLeft(0.25)
    click(ENTER_SNACK_SHOP)
    time.sleep(0.2)
    click(CONFIRM_ENTER)
    time.sleep(0.2)
    while(not pag.pixelMatchesColor(RETURN_HOME[0],RETURN_HOME[1],RETURN_HOME_COLOR)):
        time.sleep(0.2)
    moveCamRight(5)
    click(TOMATO_LOCATION)
    time.sleep(0.2)
    for i in range(50):
        click(PLUS_BUTTON)
    time.sleep(0.1)
    click(SHOP_BUY_BUTTON)
    time.sleep(0.4)
    click(RETURN_HOME)
    pag.moveTo(500,500)

    # go fish again
    while(not pag.pixelMatchesColor(RETURN_HOME[0],RETURN_HOME[1],RETURN_HOME_COLOR)):
        time.sleep(0.2)
    moveCamRight(1)
    while(not pag.pixelMatchesColor(FISHINGVIEW[0],FISHINGVIEW[1],FISHINGVIEWCOLOR)):
        moveCamRight(1)
    click(ENTER_FISHING)
    time.sleep(0.2)
    click(CONFIRM_ENTER)
    while(not pag.pixelMatchesColor(FISHING_ACCEPT_BUTTON[0],FISHING_ACCEPT_BUTTON[1],FISHING_ACCEPT_COLOR)):
        time.sleep(0.2)
    click(FISHING_ACCEPT_BUTTON)
    
def moveCamRight(waitTime:float):
    click(CAMERA_RIGHT)
    pag.mouseDown(button='left')
    time.sleep(waitTime)
    pag.mouseUp(button='left')
    pag.click()

def moveCamLeft(waitTime:float):
    click(CAMERA_LEFT)
    pag.mouseDown(button='left')
    time.sleep(waitTime)
    pag.mouseUp(button='left')
    pag.click()

def sellFish():
    click(FISHING_EXIT)
    while(not pag.pixelMatchesColor(RETURN_HOME[0],RETURN_HOME[1],RETURN_HOME_COLOR)):
        time.sleep(0.2)
    click(RETURN_HOME)
    while(not pag.pixelMatchesColor(CASH_REGISTER[0],CASH_REGISTER[1],CASH_REGISTER_COLOR)):
        time.sleep(0.2)
    for i in range(4):
        sellInv()
    click(SELL_DECLINE_BUTTON)
    time.sleep(0.3)

def saveGame():
    time.sleep(1)
    click(FISHING_EXIT)
    time.sleep(0.8)
    click(SAVE_CONFIRM)
    time.sleep(0.4)

def sellInv():
        click(CASH_REGISTER)
        time.sleep(0.2)
        for i in range(15):
            click(FIRST_SELL_ITEM)
        time.sleep(0.1)
        click(SELL_BUTTON)
        time.sleep(0.3)
        click(SELL_CONFIRM_BUTTON)
        time.sleep(0.1)

def fishingLoop():
    while(True):
        equipBait()
        ui_update_status("EQUIPED BAIT")
        time.sleep(1)
        
        clickCircle(FISHING_CIRCLE_REGION) # Start fishing
        while(pag.pixelMatchesColor(FISH_BAIT_BORDER_LOC[0],FISH_BAIT_BORDER_LOC[1],FISH_BAIT_BORDER_COLOR,tolerance=5)):
            equipBait()
            clickCircle(FISHING_CIRCLE_REGION) # If first click was a miss, try again.

        ui_update_status("START FISHING")

        catchFish()
        ui_update_status("CAUGHT FISH")
        time.sleep(1)

def catchFish():
    # Wait for fish to bite
    while(not pag.pixelMatchesColor(FISH_BAR_LOCATION[0],FISH_BAR_LOCATION[1],FISH_BAR_COLOR,tolerance=5)):
        time.sleep(0.1)
    # Now wait till we catch or lose the fish
    while(pag.pixelMatchesColor(FISH_BAR_LOCATION[0],FISH_BAR_LOCATION[1],FISH_BAR_COLOR,tolerance=5)):
        clickCircle(FISHING_CIRCLE_REGION)
    # print("caught or lost fish")
    time.sleep(1) # wait a little, lost animation takes some time...

def equipBait():
    click((592, 864)) # change this to bait border, see if it still works

def click(posTuple):
    pag.moveTo(posTuple[0], posTuple[1])
    pag.click(posTuple[0], posTuple[1])

def clickCircle(region, debug=False):
    
    img = pag.screenshot("myimg.png", region=region)
    img = np.array(img)
    # Convert the image from BGR to HSV color space
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Split the HSV channels
    h, s, v = cv.split(hsv)

    # Increase the saturation of the image
    saturation_factor = 2
    s = np.clip(s * saturation_factor, 0, 255).astype(np.uint8)

    # Merge the channels back together
    hsv = cv.merge([h, s, v])


    gray = cv.cvtColor(hsv, cv.COLOR_BGR2GRAY)
    alpha = 1.5 # Contrast control (1.0-3.0)
    beta = 0    # Brightness control (0-100)
    gray = cv.convertScaleAbs(gray, alpha=alpha, beta=beta)
    gray = cv.blur(gray, (5,5))
    rows = gray.shape[0]
    circles = cv.HoughCircles(
        gray, 
        cv.HOUGH_GRADIENT, 
        1, 
        rows,
        param1=10, 
        param2=20,
        minRadius=60,
        maxRadius=70
        )
    
    if circles is not None:
        pag.moveTo(circles[0][0][0] + region[0] ,circles[0][0][1] + region[1])
        if not debug:
            click((circles[0][0][0] + region[0] ,circles[0][0][1] + region[1]))
        if(debug):
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                # circle center
                cv.circle(s, center, 1, (0, 100, 100), 3)
                # circle outline
                radius = i[2]
                cv.circle(s, center, radius, (255, 0, 255), 3)
    if(debug):
        cv.imshow("detected circles", gray)
        cv.waitKey(0)

def ui_update_status(str):
    global my_window
    return
    print("UI update currently broken")
    # my_window['_status_'].update(text="Status: " + str)

def createWindow():
    global my_window
    sg.theme('DarkGrey10')
    titleFont = ('Courier New', 16, 'bold')
    descFont = ('Courier New', 10, 'italic')
    layout = [
        [sg.Text("PetPals AFK Tool", justification='center', font=titleFont)],
        [sg.Text("Created By RubberDucky#4318", font=descFont),], 
        [sg.Button("Auto Race",key='_race_')], 
        [sg.Button("Auto Fish",key='_fish_')],
        [sg.Checkbox("Auto Decline Trades",default=True, disabled=False, key='_trade_')],
        [sg.Text("Status: Idle",key='_status_')],
        [sg.Button("Exit",size=(30,1))]
        ]
    
    my_window = sg.Window(title='PetPals AF', icon="icon.ico", layout=layout, keep_on_top=True, margins=(20, 50))
    isRacing = False
    isFishing = False
    process = ''
    stopInturruptionsProcess = ''
    # Create an event loop
    while True:
        event, values = my_window.read()
        
        

        # Start Racing
        if(event == "_race_" and isRacing == False and isFishing == False):
            isRacing = True
            my_window["_race_"].update(text="Stop Racing")
            my_window["_trade_"].update(disabled=True)

            stopInturruptionsProcess = multiprocessing.Process(target=stopInturruptions, args=(values["_trade_"],))
            stopInturruptionsProcess.start()
            process = multiprocessing.Process(target=racingLoop)
            process.start()
        # Stop Racing
        elif(event == "_race_" and isRacing == True):
            isRacing = False
            my_window["_race_"].update(text="Auto Race")
            my_window["_trade_"].update(disabled=False)
            
            stopInturruptionsProcess.terminate()
            process.terminate()
        # Start Fishing
        elif(event == "_fish_" and isFishing == False and isRacing == False):
            isFishing = True
            my_window["_trade_"].update(disabled=True)
            my_window["_fish_"].update(text="Stop Fishing")
            
            stopInturruptionsProcess = multiprocessing.Process(target=stopInturruptions, args=(values["_trade_"],))
            stopInturruptionsProcess.start()
            process = multiprocessing.Process(target=fishingLoop)
            process.start()
        # Stop Fishing
        elif(event == "_fish_" and isFishing == True):
            my_window["_trade_"].update(disabled=False)
            isFishing = False
            my_window["_fish_"].update(text="Auto Fish")

            stopInturruptionsProcess.terminate()
            process.terminate()


        # Exit program
        if event == "Exit" or event == sg.WIN_CLOSED:
            if process != '':
                process.terminate()
            break

if __name__ == '__main__':
    createWindow()

# declineTrade()

# clickCircle(FISHING_CIRCLE_REGION, True)