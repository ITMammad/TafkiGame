import pygame
import random
import tkinter
import pygame.locals
from PIL import Image, ImageTk
import tkinter.ttk as modernTKinter

garbage_one_comsDown_status = True
garbage_two_comsDown_status = True
clock = pygame.time.Clock()
garbage_one_pos = [0, 0]
garbage_two_pos = [0, 0]
gameOverStatus = False
garbage_one_speed = 0
garbage_two_speed = 0
monitor_height = 0
monitor_width = 0
screen_height = 0
screen_width = 0
garbage_one = []
garbage_two = []
start_ticks = 0
binsSpeed = 25
running = True
leftTime = 0
score = 0
time = 0
fps = 40
speeds = [
    [
        1,
        2,
        3,
        4,
        5
    ],
    [
        3,
        4,
        5,
        6,
        7
    ],
    [
        5,
        6,
        7,
        8,
        9
    ]
]
garbagesT = [
    ["assets/garbages/T/1.png", [50, 120]],
    ["assets/garbages/T/2.png", [50, 127]],
    ["assets/garbages/T/3.png", [50, 114]],
    ["assets/garbages/T/4.png", [50, 61]],
    ["assets/garbages/T/5.png", [50, 51]],
    ["assets/garbages/T/6.png", [50, 79]],
    ["assets/garbages/T/7.png", [50, 30]],
    ["assets/garbages/T/8.png", [50, 43]],
    ["assets/garbages/T/9.png", [50, 79]],
    ["assets/garbages/T/10.png", [50, 26]],
]
garbagesK = [
    ["assets/garbages/K/1.png", [50, 41]],
    ["assets/garbages/K/2.png", [50, 51]],
    ["assets/garbages/K/3.png", [50, 47]],
    ["assets/garbages/K/4.png", [50, 49]],
    ["assets/garbages/K/5.png", [50, 31]],
    ["assets/garbages/K/6.png", [50, 48]],
    ["assets/garbages/K/7.png", [50, 57]],
    ["assets/garbages/K/8.png", [50, 87]],
    ["assets/garbages/K/9.png", [50, 27]],
    ["assets/garbages/K/10.png", [50, 73]],
]
color_of_score = [
    10,
    10,
    10
]
garbage_types = [garbagesT, garbagesK]
binTPos = [0, screen_height - 200]
binKPos = [screen_width - 100, screen_height - 100]

def showAboutWindow():
    aboutWindow = tkinter.Tk()
    aboutWindow.title("WhileTrue About")
    screen_width = aboutWindow.winfo_screenwidth()
    screen_height = aboutWindow.winfo_screenheight()
    x = (screen_width / 2) - (250 / 2)
    y = (screen_height / 2) - (80 / 2)
    aboutWindow.geometry('%dx%d+%d+%d' % (250, 80, x, y))
    aboutFrame = modernTKinter.Frame(aboutWindow, padding=5)
    aboutFrame.pack()
    whileTrueText = modernTKinter.Label(aboutFrame, text="WhileTrue", foreground="#00F")
    whileTrueAboutText = modernTKinter.Label(aboutFrame, text="The TafkiGame Game Developed By \n ❤️ From WhileTrue Programming \n Team...", justify=tkinter.CENTER, foreground="#F00")
    whileTrueText.pack()
    whileTrueAboutText.pack()
    aboutWindow.resizable(False, False)
    aboutWindow.mainloop()

def showHowToWindow():
    howToWindow = tkinter.Toplevel()
    howToWindow.title("TafkiGame HowTo")
    screen_width = howToWindow.winfo_screenwidth()
    screen_height = howToWindow.winfo_screenheight()
    x = (screen_width / 2) - (500 / 2)
    y = (screen_height / 2) - (540 / 2)
    howToWindow.geometry('%dx%d+%d+%d' % (500, 540, x, y))
    howToFrame = modernTKinter.Frame(howToWindow, padding=10)
    howToFrame.pack()
    img = ImageTk.PhotoImage(Image.open(r"assets/img/howTo.png").resize((480, 480)))
    panel = modernTKinter.Label(howToFrame, image=img)
    panel.pack()
    showGarbageInfoWindowButton = modernTKinter.Button(howToFrame, text="درباره زباله ها", width=240, command=showGarbageInfoWindow)
    showGarbageInfoWindowButton.pack()
    howToWindow.resizable(False, False)
    howToWindow.mainloop()

def showGarbageInfoWindow():
    garbageInfoWindow = tkinter.Toplevel()
    garbageInfoWindow.title("TafkiGame HowTo")
    screen_width = garbageInfoWindow.winfo_screenwidth()
    screen_height = garbageInfoWindow.winfo_screenheight()
    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2) - (600 / 2)
    garbageInfoWindow.geometry('%dx%d+%d+%d' % (800, 600, x, y))
    garbageInfoFrame = modernTKinter.Frame(garbageInfoWindow, padding=10)
    garbageInfoFrame.pack()
    img = ImageTk.PhotoImage(Image.open(r"assets/img/garbageInfo.png").resize((780, 580)))
    panel = modernTKinter.Label(garbageInfoFrame, image=img)
    panel.pack()
    garbageInfoWindow.resizable(False, False)
    garbageInfoWindow.mainloop()

def showMainWindow():
    global monitor_height
    global monitor_width
    mainWindow = tkinter.Tk()
    mainWindow.title("TafkiGame")
    photo = tkinter.PhotoImage(file='assets/img/logo.png')
    mainWindow.iconphoto(True, photo)
    screen_width = mainWindow.winfo_screenwidth()
    screen_height = mainWindow.winfo_screenheight()
    monitor_height = mainWindow.winfo_screenheight()
    monitor_width = mainWindow.winfo_screenwidth()
    x = (screen_width / 2) - (350 / 2)
    y = (screen_height / 2) - (132.5 / 2)
    mainWindow.geometry('%dx%d+%d+%d' % (350, 132.5, x, y))
    mainFrame = modernTKinter.Frame(padding=10)
    mainFrame.pack()
    def sel():
        selectedOption = var.get()
        if selectedOption == 1 or selectedOption == 2 or selectedOption == 3:
            mainWindow.destroy()
            showGameWindow(selectedOption)

    var = tkinter.IntVar()
    R1 = modernTKinter.Radiobutton(mainFrame, text="آسان", variable=var, value=1)
    R1.grid(row=1, column=1)
    R2 = modernTKinter.Radiobutton(mainFrame, text="متوسط", variable=var, value=2)
    R2.grid(row=2, column=1)
    R3 = modernTKinter.Radiobutton(mainFrame, text="سخت", variable=var, value=3)
    R3.grid(row=3, column=1)
    button = modernTKinter.Button(mainFrame, text="شروع بازی", width=24, command=sel)
    button.grid(row=4, column=1)
    aboutButton = modernTKinter.Button(mainFrame, text="درباره ما", width=12, command=showAboutWindow)
    aboutButton.grid(row=5, column=0)
    howToButton = modernTKinter.Button(mainFrame, text="آموزش بازی", width=12, command=showHowToWindow)
    howToButton.grid(row=5, column=2)
    mainWindow.resizable(False, False)
    mainWindow.mainloop()

def showGameWindow(hardShip):
    global garbage_one_comsDown_status
    global garbage_two_comsDown_status
    global garbage_one_speed
    global garbage_two_speed
    global garbage_one_pos
    global garbage_two_pos
    global gameOverStatus
    global monitor_height
    global monitor_width
    global screen_height
    global garbage_types
    global screen_width
    global start_ticks
    global garbagesT
    global garbagesK
    global leftTime
    global running
    global score
    global time

    global binTPos
    global binKPos

    leftTime = time = hardShip * 15

    screen_height = monitor_height / 2 + 150
    screen_width = monitor_width / 2 + 250

    binTPos = [0, screen_height - 150]
    binKPos = [screen_width - 100, screen_height - 75]

    pygame.init()
    gameScreen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('TafkiGame')
    Icon = pygame.image.load('assets/img/logo.png')
    pygame.display.set_icon(Icon)
    bgPic = pygame.image.load("assets/img/bg.jpg")
    bgIMG = pygame.transform.scale(bgPic, (screen_width, screen_height))
    gameScreen.blit(bgIMG, (0, 0))

    def getBestScore():
        file = open("Best.txt", "r")
        txt = file.read()
        if txt == "":
            txt = "0"
        file.close()
        return int(txt)

    def setBestScore():
        global score

        file = open("Best.txt", "w+")
        file.write(str(score))
        file.close()

    def makeScreenClear():
        gameScreen.fill((255, 255, 255))
        gameScreen.blit(bgIMG, (0, 0))

    def update_information():
        font = pygame.font.Font("assets/font/IRANSans.ttf", 25)
        score_text = font.render('Score: ' + str(score), True, (color_of_score[0], color_of_score[1], color_of_score[2]))
        time = font.render("Time: " + str(int(leftTime)) + "s", True, (color_of_score[0], color_of_score[1], color_of_score[2]))
        level_text = font.render('HardShip: ' + str(hardShip), True, (color_of_score[0], color_of_score[1], color_of_score[2]))
        gameScreen.blit(score_text, (20, 5))
        gameScreen.blit(time, time.get_rect(center=(screen_width // 2, 25)))
        gameScreen.blit(level_text, (screen_width - 150, 5))

    def playMusic():
        pygame.mixer.music.load("assets/music/BG.wav")
        pygame.mixer.music.play(-1)

    def startCountDown():
        font = pygame.font.Font("assets/font/IRANSans.ttf", 125)
        count3 = font.render("3", True, (10, 10, 10))
        count2 = font.render("2", True, (10, 10, 10))
        count1 = font.render("1", True, (10, 10, 10))
        go = font.render("!GO!", True, (10, 10, 10))
        count3Rects = count3.get_rect(center = pygame.display.get_surface().get_rect().center)
        count2Rects = count2.get_rect(center = pygame.display.get_surface().get_rect().center)
        count1Rects = count1.get_rect(center = pygame.display.get_surface().get_rect().center)
        goRects = go.get_rect(center = pygame.display.get_surface().get_rect().center)
        gameScreen.blit(count3, count3Rects)
        pygame.display.update()
        pygame.time.delay(1000)
        makeScreenClear()
        gameScreen.blit(count2, count2Rects)
        pygame.display.update()
        pygame.time.delay(1000)
        makeScreenClear()
        gameScreen.blit(count1, count1Rects)
        pygame.display.update()
        pygame.time.delay(1000)
        makeScreenClear()
        gameScreen.blit(go, goRects)
        pygame.display.update()
        pygame.time.delay(2500)
        makeScreenClear()

    def move_garbages():
        global garbage_one_comsDown_status
        global garbage_two_comsDown_status
        global garbage_one_speed
        global garbage_two_speed
        global garbage_one_pos
        global garbage_two_pos
        global garbage_types
        global screen_height
        global screen_width
        global garbage_one
        global garbage_two
        global speeds
        global score

        if garbage_one_comsDown_status:
            garbage_one = garbage_types[0][random.randint(0, 9)]
            garbagePic = pygame.image.load(garbage_one[0])
            garbageIMG = pygame.transform.scale(garbagePic, (garbage_one[1][1], garbage_one[1][0]))
            garbage_one_pos = [random.randint(0, screen_width - garbage_one[1][0]), 0]
            garbage_one_speed = speeds[hardShip - 1][random.randint(0, 4)]
            gameScreen.blit(garbageIMG, (garbage_one_pos[0], garbage_one_pos[1]))
            garbage_one_comsDown_status = False
        elif check_collision(1):
            garbage_one_comsDown_status = True
        elif garbage_one_pos[1] + garbage_one[1][1] >= screen_height:
            score -= 1
            garbage_one_comsDown_status = True
        else:
            garbage_one_pos[1] += garbage_one_speed
            garbagePic = pygame.image.load(garbage_one[0])
            garbageIMG = pygame.transform.scale(garbagePic, (garbage_one[1][1], garbage_one[1][0]))
            gameScreen.blit(garbageIMG, (garbage_one_pos[0], garbage_one_pos[1]))

        if garbage_two_comsDown_status:
            garbage_two = garbage_types[1][random.randint(0, 9)]
            while garbage_two == garbage_one:
                garbage_two = garbage_types[0][random.randint(0, 9)]
            garbagePic = pygame.image.load(garbage_two[0])
            garbageIMG = pygame.transform.scale(garbagePic, (garbage_two[1][1], garbage_two[1][0]))
            garbage_two_pos = [random.randint(0, screen_width - garbage_one[1][0]), 0]
            while garbage_two_pos == garbage_one_pos:
                garbage_two_pos = [random.randint(0, screen_width - garbage_one[1][0]), 0]
            garbage_two_speed = speeds[hardShip - 1][random.randint(0, 4)]
            while garbage_two_speed == garbage_one_speed:
                garbage_two_speed = speeds[hardShip - 1][random.randint(0, 4)]
            gameScreen.blit(garbageIMG, (garbage_two_pos[0], garbage_two_pos[1]))
            garbage_two_comsDown_status = False
        elif check_collision(2):
            garbage_two_comsDown_status = True
        elif garbage_two_pos[1] + garbage_two[1][1] >= screen_height:
            score -= 1
            garbage_two_comsDown_status = True
        else:
            garbage_two_pos[1] += garbage_two_speed
            garbagePic = pygame.image.load(garbage_two[0])
            garbageIMG = pygame.transform.scale(garbagePic, (garbage_two[1][1], garbage_two[1][0]))
            gameScreen.blit(garbageIMG, (garbage_two_pos[0], garbage_two_pos[1]))

    def move_bins():
        global binTPos
        global binKPos

        binTPic = pygame.image.load("assets/bins/T.png")
        binTIMG = pygame.transform.scale(binTPic, (100, 75))
        gameScreen.blit(binTIMG, (binTPos[0], binTPos[1]))
        binKPic = pygame.image.load("assets/bins/K.png")
        binKIMG = pygame.transform.scale(binKPic, (100, 75))
        gameScreen.blit(binKIMG, (binKPos[0], binKPos[1]))

    def timer():
        global start_ticks
        global leftTime
        global time

        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        leftTime = time - seconds

    def check_collision(t):
        global score

        if t == 1:
            if binTPos[0] < garbage_one_pos[0] < binTPos[0] + 100 and binTPos[1] < garbage_one_pos[1] < binTPos[1] + 75:
                score += 1
                return True
            elif binKPos[0] < garbage_one_pos[0] < binKPos[0] + 100 and binKPos[1] < garbage_one_pos[1] < binKPos[1] + 75:
                score -= 1
                return True
            else:
                return False
        elif t == 2:
            if binKPos[0] < garbage_two_pos[0] < binKPos[0] + 100 and binKPos[1] < garbage_two_pos[1] < binKPos[1] + 75:
                score += 1
                return True
            elif binKPos[0] < garbage_two_pos[0] < binKPos[0] + 100 and binKPos[1] < garbage_two_pos[1] < binKPos[1] + 75:
                score -= 1
                return True
            else:
                return False
        else:
            return False

    def move_binsT(wh):
        global binTPos
        global binsSpeed

        if wh == "r":
            if not binTPos[0] + 100 >= screen_width:
                binTPos[0] += binsSpeed
        elif wh == "l":
            if not binTPos[0] - binsSpeed < 0:
                binTPos[0] -= binsSpeed

    def move_binsK(wh):
        global binKPos
        global binsSpeed

        if wh == "r":
            if not binKPos[0] + 100 >= screen_width:
                binKPos[0] += binsSpeed
        elif wh == "l":
            if not binKPos[0] - binsSpeed < 0:
                binKPos[0] -= binsSpeed

    def gameOver():
        global gameOverStatus
        global score

        gameOverStatus = True
        if score >= getBestScore():
            setBestScore()
        font = pygame.font.Font("assets/font/IRANSans.ttf", 35)

        makeScreenClear()
        GOver = font.render("...!GameOver!...", True, (color_of_score[0], color_of_score[1], color_of_score[2]))
        gameScreen.blit(GOver, GOver.get_rect(center=(screen_width // 2, screen_height / 100 * 40)))
        TGScore = font.render("Your Score: " + str(score), True, (color_of_score[0], color_of_score[1], color_of_score[2]))
        gameScreen.blit(TGScore, TGScore.get_rect(center=(screen_width // 2, screen_height / 100 * 50)))
        BGScore = font.render("Your Best Score: " + str(getBestScore()), True, (color_of_score[0], color_of_score[1], color_of_score[2]))
        gameScreen.blit(BGScore, BGScore.get_rect(center=(screen_width // 2, screen_height / 100 * 60)))

    playMusic()
    startCountDown()
    start_ticks = pygame.time.get_ticks()

    while running:
        if not gameOverStatus:
            makeScreenClear()
            update_information()
            move_garbages()
            move_bins()

            timer()
            clock.tick(fps)
            pygame.display.update()

            if leftTime // 1 <= 0:
                gameOver()

            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.locals.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.locals.K_LEFT]:
                        move_binsK("l")
                    elif pygame.key.get_pressed()[pygame.locals.K_RIGHT]:
                        move_binsK("r")
                    if pygame.key.get_pressed()[pygame.locals.K_a]:
                        move_binsT("l")
                    elif pygame.key.get_pressed()[pygame.locals.K_d]:
                        move_binsT("r")
        else:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    running = False
                    pygame.quit()
            if running:
                pygame.display.update()

showMainWindow()