import pyautogui as pag
import cv2 as cv
import numpy as np
import time
from screeninfo import get_monitors
import PySimpleGUI as sg
import asyncio

# left, top, width, height
GAME_REGION = (442, 303, 996, 594)
FISHING_CIRCLE_REGION = (950, 421, 440, 301)

FISH_BAR_LOCATION = (788,849)
FISH_BAR_COLOR = (213, 211, 236)


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

FISHINGVIEW= (1151, 801)
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
# STAD_RACE_POS_XEND = 985
STAD_RACE_JUMP_COLOR = (155,168,163)
FINISH_BUSH_POS = (751,830)
FINISH_BUSH_POS_2 = (747,830)
FINISH_BUSH_COLOR = (255,255,255)


def main():
    if(pag.pixelMatchesColor(LOGIN_BUTTON[0],LOGIN_BUTTON[1],LOGIN_BUTTON_COLOR)):
        login()
        travelToFishing()
    while True:
        fishingLoop()
        sellFish()
        saveGame()
        restock()
        refresh()
        login()
        travelToFishing()

async def createWindow():
    layout = [[sg.Text("Created By RubberDucky#4318")], [sg.Button("Auto Race")], [sg.Button("Auto Fish")], [sg.Button("Exit")]]
    window = sg.Window(title='PetPals AFK Tool', layout=layout, keep_on_top=True, margins=(100, 50))
    isRacing = False
    isFishing = False
    currentTask = ''

    # Create an event loop
    while True:
        event, values = window.read()
        
        if(event == "Auto Race" and isRacing == False and isFishing == False):
            print("Start event: racing")
            currentTask = asyncio.create_task(racingLoop())

        if(event == "Auto Race" and isRacing == True):
            currentTask.cancel()

        if event == "Exit" or event == sg.WIN_CLOSED:
            currentTask.cancel()
            break



async def racingLoop():
    while True:
        enterStadium()
        waitStadiumRaceStart()
        stadiumRacing()
        

# Auto Statium
def enterStadium():
   click((720,420))
   time.sleep(0.5)
   click(CONFIRM_ENTER)
   time.sleep(1)

def waitStadiumRaceStart():
    while(pag.pixelMatchesColor(RETURN_HOME[0],RETURN_HOME[1],RETURN_HOME_COLOR)):
        time.sleep(0.2)
        print("Waiting for race to start")
    time.sleep(1)

def stadiumRacing():
    bushcount = 0
    # lastPixelRGB = (0,0,0)
    while(bushcount < 5):
        cPos = STAD_RACE_POS_XSTART
        # while(cPos < STAD_RACE_POS_XEND):
        if(pag.pixelMatchesColor(STAD_RACE_POS_XSTART, STAD_RACE_POS_Y, STAD_RACE_JUMP_COLOR)):
            click((950,600))
            #     break
            # else:
            #     cPos += 1
        # newPixel = pag.pixel(1010, 640)
        # if (lastPixelRGB == newPixel):
        #     bushcount += 1
        # else:
        #     lastPixelRGB = newPixel
        #     bushcount = 0
        if pag.pixelMatchesColor(FINISH_BUSH_POS[0],FINISH_BUSH_POS[1], FINISH_BUSH_COLOR) or pag.pixelMatchesColor(FINISH_BUSH_POS_2[0],FINISH_BUSH_POS_2[1], FINISH_BUSH_COLOR):
            bushcount += 1  
        else:
            bushcount = 0
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
    while(pag.pixelMatchesColor(BAIT_BORDER_LOC[0],BAIT_BORDER_LOC[1],BAIT_BORDER_COLOR,tolerance=3)):
        equipBait()
        clickCircle(FISHING_CIRCLE_REGION) # Start fishing
        time.sleep(0.1)
        clickCircle(FISHING_CIRCLE_REGION)
        time.sleep(0.1)
        clickCircle(FISHING_CIRCLE_REGION)
        catchFish()

def catchFish():
    # print("in catch fish")
    # Wait for fish to bite
    while(not pag.pixelMatchesColor(FISH_BAR_LOCATION[0],FISH_BAR_LOCATION[1],FISH_BAR_COLOR,tolerance=5)):
        time.sleep(0.2)
    # print("fish bite")
    # Now wait till we catch or lose the fish
    while(pag.pixelMatchesColor(FISH_BAR_LOCATION[0],FISH_BAR_LOCATION[1],FISH_BAR_COLOR,tolerance=5)):
        clickCircle(FISHING_CIRCLE_REGION)
        time.sleep(1)
    # print("caught or lost fish")

def equipBait():
    click((592, 864)) # change this to bait border, see if it still works

def click(posTuple):
    pag.moveTo(posTuple[0],posTuple[1])
    pag.click(posTuple[0],posTuple[1])

def clickCircle(region, debug=False):
    
    s = pag.screenshot("myimg.png", region=region)
    s = np.array(s)
    gray = cv.cvtColor(s, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows,
                               param1=10, param2=24,
                               minRadius=50, maxRadius=80)
    
    if circles is not None:
        pag.moveTo(circles[0][0][0] + region[0] ,circles[0][0][1] + region[1])
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
            cv.imshow("detected circles", s)
            cv.waitKey(0)
                
#main()
asyncio.run(createWindow())
