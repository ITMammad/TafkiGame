import pygame
import random
import tkinter
import pygame.locals
from PIL import Image, ImageTk
import tkinter.ttk as modernTKinter

garbage_one_comsDown_status = True
garbage_two_comsDown_status = True
clock = pygame.time.Clock()
godPowerGiftStatus = False
godPowerGiftSpeed = 0
garbage_one_pos = [0, 0]
garbage_two_pos = [0, 0]
gameOverStatus = False
garbage_one_speed = 0
garbage_two_speed = 0
binTMoveState = False
binKMoveState = False
godPowerPos = [0, 0]
monitor_height = 0
monitor_width = 0
screen_height = 0
screen_width = 0
garbage_one = []
garbage_two = []
start_ticks = 0
binsSpeed = 12.5
running = True
leftTime = 0
score = 0
power = 3
galb = None
time = 0
fps = 30
speeds = [0.40, 0.45, 0.50, 0.55, 0.60]
garbagesT = []
garbagesK = []
color_of_score = [ 10, 10, 10 ]
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
    y = (screen_height / 2) - (700 / 2)
    garbageInfoWindow.geometry('%dx%d+%d+%d' % (800, 700, x, y))
    garbageInfoFrame = modernTKinter.Frame(garbageInfoWindow, padding=10)
    garbageInfoFrame.pack()
    img = ImageTk.PhotoImage(Image.open(r"assets/img/garbageInfo.png").resize((780, 680)))
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

    def checkHardShip():
        file = open("hardShip.txt", "r")
        txt = file.read()
        return int(txt)

    topHardShip = checkHardShip();

    var = tkinter.IntVar()
    R1 = modernTKinter.Radiobutton(mainFrame, text="آسان", variable=var, value=1)
    R1.grid(row=1, column=1)
    R2 = modernTKinter.Radiobutton(mainFrame, text="متوسط", variable=var, value=2)
    R2.grid(row=2, column=1)
    R3 = modernTKinter.Radiobutton(mainFrame, text="سخت", variable=var, value=3)
    R3.grid(row=3, column=1)

    if topHardShip < 1:
        R2.configure(state = tkinter.DISABLED)
        R3.configure(state = tkinter.DISABLED)
    elif topHardShip == 1:
        R3.configure(state = tkinter.DISABLED)

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
    global godPowerGiftStatus
    global godPowerGiftSpeed
    global garbage_one_speed
    global garbage_two_speed
    global garbage_one_pos
    global garbage_two_pos
    global gameOverStatus
    global monitor_height
    global binTMoveState
    global binKMoveState
    global monitor_width
    global screen_height
    global garbage_types
    global screen_width
    global start_ticks
    global binsSpeed
    global garbagesT
    global garbagesK
    global leftTime
    global running
    global score
    global power
    global time
    global galb
    global binTPos
    global binKPos

    power = ((hardShip * 2) + 1)
    screen_height = monitor_height / 2 + 150
    screen_width = monitor_width / 2 + 250
    binTPos = [0, screen_height - 150]
    binKPos = [screen_width - 100, screen_height - 75]
    binsSpeed = ((screen_width / 100) * 2.25)
    godPowerGiftSpeed = ((screen_width / 100) * 0.85)

    pygame.init()
    gameScreen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('TafkiGame')
    Icon = pygame.image.load('assets/img/logo.png')
    pygame.display.set_icon(Icon)
    emojiFont = pygame.font.Font("assets/font/Emoji.ttf", 50)
    galb = emojiFont.render("♥", True, (255, 0, 0))
    mainFont = pygame.font.Font("assets/font/IRANSans.ttf", 25)
    smallEmojiFont = pygame.font.Font("assets/font/Emoji.ttf", 25)
    correctMusic = pygame.mixer.Sound("assets/music/Correct_Bin.wav")
    inCorrectMusic = pygame.mixer.Sound("assets/music/InCorrect_Bin.wav")
    bgPic = pygame.image.load("assets/img/backGround.jpg")
    bgIMG = pygame.transform.scale(bgPic, (screen_width, screen_height))
    gameScreen.blit(bgIMG, (0, 0))

    garbagesT = [
        pygame.transform.scale(pygame.image.load("assets/garbages/T/1.png"), (75, 30)),
        pygame.transform.scale(pygame.image.load("assets/garbages/T/2.png"), (75, 30)),
        pygame.transform.scale(pygame.image.load("assets/garbages/T/3.png"), (75, 32)),
        pygame.transform.scale(pygame.image.load("assets/garbages/T/4.png"), (61, 50)),
        pygame.transform.scale(pygame.image.load("assets/garbages/T/5.png"), (51, 50)),
        pygame.transform.scale(pygame.image.load("assets/garbages/T/6.png"), (79, 50)),
        pygame.transform.scale(pygame.image.load("assets/garbages/T/7.png"), (30, 50)),
        pygame.transform.scale(pygame.image.load("assets/garbages/T/8.png"), (43, 50)),
        pygame.transform.scale(pygame.image.load("assets/garbages/T/9.png"), (65, 41)),
        pygame.transform.scale(pygame.image.load("assets/garbages/T/10.png"), (26, 50)),
    ]

    garbagesK = [
        pygame.transform.scale(pygame.image.load("assets/garbages/K/1.png"), (41, 50)),
        pygame.transform.scale(pygame.image.load("assets/garbages/K/2.png"), (51, 50)),
        pygame.transform.scale(pygame.image.load("assets/garbages/K/3.png"), (47, 50)),
        pygame.transform.scale(pygame.image.load("assets/garbages/K/4.png"), (49, 50)),
        pygame.transform.scale(pygame.image.load("assets/garbages/K/5.png"), (31, 50)),
        pygame.transform.scale(pygame.image.load("assets/garbages/K/6.png"), (48, 50)),
        pygame.transform.scale(pygame.image.load("assets/garbages/K/7.png"), (57, 50)),
        pygame.transform.scale(pygame.image.load("assets/garbages/K/8.png"), (65, 37)),
        pygame.transform.scale(pygame.image.load("assets/garbages/K/9.png"), (27, 50)),
        pygame.transform.scale(pygame.image.load("assets/garbages/K/10.png"), (65, 44)),
    ]

    def setHardShip():
        file = open("hardShip.txt", "w+")
        fr = open("hardShip.txt", "r").read()
        if fr < str(hardShip):
            file.write(str(hardShip))
        file.close()
        return True

    def makeScreenClear():
        gameScreen.blit(bgIMG, (0, 0))

    def update_information():
        global power

        score_text = mainFont.render('Score: ' + str(score), True, (25, 205, 25))
        power_text = smallEmojiFont.render("♥: " + str(power - 0.0), True, (255,0, 0))
        level_text = mainFont.render('HardShip: ' + str(hardShip), True, (25, 25, 205))
        gameScreen.blit(score_text, (20, 5))
        gameScreen.blit(power_text, power_text.get_rect(center=(screen_width // 2, 25)))
        gameScreen.blit(level_text, (screen_width - 150, 5))

    def playMusic():
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(f"assets/music/BG_{hardShip}.wav"), -1)

    def playCorrectMusic():
        pygame.mixer.Channel(1).play(correctMusic)

    def playInCorrectMusic():
        pygame.mixer.Channel(1).play(inCorrectMusic)

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
        pygame.time.delay(750)
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
        global power

        if garbage_one_comsDown_status:
            garbage_one = garbagesT[random.randint(0, 9)]
            garbage_one_pos = [random.randint(0, screen_width - garbage_one.get_size()[0]), 0]
            garbage_one_speed = speeds[random.randint(0, 4)]
            gameScreen.blit(garbage_one, (garbage_one_pos[0], garbage_one_pos[1]))
            garbage_one_comsDown_status = False
        elif check_collision(1):
            garbage_one_comsDown_status = True
        elif garbage_one_pos[1] + garbage_one.get_size()[1] >= screen_height:
            power -= 0.5
            garbage_one_comsDown_status = True
        else:
            garbage_one_pos[1] += int((screen_width / 100) * garbage_one_speed - 0.0)
            gameScreen.blit(garbage_one, (garbage_one_pos[0], garbage_one_pos[1]))

        if garbage_two_comsDown_status:
            garbage_two = garbagesK[random.randint(0, 9)]
            garbage_two_pos = [random.randint(0, screen_width - garbage_two.get_size()[0]), 0]
            collision = garbage_one_pos[0] + garbage_one.get_width() < garbage_two_pos[0] and garbage_two_pos[0] > garbage_two_pos[0] + garbage_two.get_width()
            while collision:
                garbage_two_pos = [random.randint(0, screen_width - garbage_one[1][0]), 0]
            garbage_two_speed = speeds[random.randint(0, 4)]
            while garbage_two_speed == garbage_one_speed:
                garbage_two_speed = speeds[random.randint(0, 4)]
            gameScreen.blit(garbage_two, (garbage_two_pos[0], garbage_two_pos[1]))
            garbage_two_comsDown_status = False
        elif check_collision(2):
            garbage_two_comsDown_status = True
        elif garbage_two_pos[1] + garbage_two.get_size()[1] >= screen_height:
            power -= 0.5
            garbage_two_comsDown_status = True
        else:
            garbage_two_pos[1] += int((screen_width / 100) * garbage_two_speed - 0.0)
            gameScreen.blit(garbage_two, (garbage_two_pos[0], garbage_two_pos[1]))

    def move_bins():
        global binTPos
        global binKPos

        move_binsT()
        move_binsK()

        binTPic = pygame.image.load("assets/bins/T.png")
        binTIMG = pygame.transform.scale(binTPic, (100, 75))
        gameScreen.blit(binTIMG, (binTPos[0], binTPos[1]))
        binKPic = pygame.image.load("assets/bins/K.png")
        binKIMG = pygame.transform.scale(binKPic, (100, 75))
        gameScreen.blit(binKIMG, (binKPos[0], binKPos[1]))

    def check_collision(t):
        global godPowerGiftStatus
        global score
        global power

        if t == 1:
            if binTPos[0] < garbage_one_pos[0] < binTPos[0] + 100 and binTPos[1] < garbage_one_pos[1] < binTPos[1] + 75:
                score += 1
                playCorrectMusic()
                return True
            elif binKPos[0] < garbage_one_pos[0] < binKPos[0] + 100 and binKPos[1] < garbage_one_pos[1] < binKPos[1] + 75:
                power -= 1
                playInCorrectMusic()
                return True
            else:
                return False
        elif t == 2:
            if binKPos[0] < garbage_two_pos[0] < binKPos[0] + 100 and binKPos[1] < garbage_two_pos[1] < binKPos[1] + 75:
                score += 1
                playCorrectMusic()
                return True
            elif binTPos[0] < garbage_two_pos[0] < binTPos[0] + 100 and binTPos[1] < garbage_two_pos[1] < binTPos[1] + 75:
                power -= 1
                playInCorrectMusic()
                return True
            else:
                return False
        else:
            if godPowerGiftStatus:
                power += 1
            else:
                return False

    def move_binsT():
        global binTPos
        global binsSpeed
        global binTMoveState

        if not binTMoveState == False:
            if binTMoveState == "r":
                if not binTPos[0] + 100 >= screen_width:
                    binTPos[0] += int((((hardShip + 1) / 2) * binsSpeed) - 0.0)
            elif binTMoveState == "l":
                if not binTPos[0] - int((((hardShip + 1) / 2) * binsSpeed) - 0.0) < 0:
                    binTPos[0] -= int((((hardShip + 1) / 2) * binsSpeed) - 0.0)

    def move_binsK():
        global binKPos
        global binsSpeed
        global binKMoveState

        if not binKMoveState == False:
            if binKMoveState == "r":
                if not binKPos[0] + 100 >= screen_width:
                    binKPos[0] += int((((hardShip + 1) / 2) * binsSpeed) - 0.0)
            elif binKMoveState == "l":
                if not binKPos[0] - int((((hardShip + 1) / 2) * binsSpeed) - 0.0) < 0:
                    binKPos[0] -= int((((hardShip + 1) / 2) * binsSpeed) - 0.0)

    def gameOver():
        global gameOverStatus
        global score

        gameOverStatus = True
        pygame.mixer.Channel(0).stop()
        pygame.mixer.music.load("assets/music/GameOver.wav")
        pygame.mixer.music.play()
        font = pygame.font.Font("assets/font/IRANSans.ttf", 35)

        bgPic = pygame.image.load("assets/img/GameOver.jpg")
        bgIMG = pygame.transform.scale(bgPic, (screen_width, screen_height))
        gameScreen.fill((255, 255, 255))
        gameScreen.blit(bgIMG, (0, 0))

        GOver = font.render("...!GameOver!...", True, (color_of_score[0], color_of_score[1], color_of_score[2]))
        gameScreen.blit(GOver, GOver.get_rect(center=(screen_width // 2, screen_height / 100 * 40)))
        TGScore = font.render("Your Score: " + str(score), True, (color_of_score[0], color_of_score[1], color_of_score[2]))
        gameScreen.blit(TGScore, TGScore.get_rect(center=(screen_width // 2, screen_height / 100 * 50)))
        BGScore = font.render("HardShip: " + str(hardShip), True, (color_of_score[0], color_of_score[1], color_of_score[2]))
        gameScreen.blit(BGScore, BGScore.get_rect(center=(screen_width // 2, screen_height / 100 * 60)))

    def gameWin():
        global gameOverStatus
        global score

        gameOverStatus = True
        pygame.mixer.Channel(0).stop()
        pygame.mixer.music.load("assets/music/GameWin.wav")
        pygame.mixer.music.play()
        setHardShip()
        font = pygame.font.Font("assets/font/IRANSans.ttf", 35)

        bgPic = pygame.image.load("assets/img/gameWin.jpg")
        bgIMG = pygame.transform.scale(bgPic, (screen_width, screen_height))
        gameScreen.fill((255, 255, 255))
        gameScreen.blit(bgIMG, (0, 0))

        if int(hardShip) == 3:
            cupPic = pygame.image.load(f"assets/keys/key{hardShip}.png")
            cupIMG = pygame.transform.scale(cupPic, ((screen_width / 100) * 10, (screen_width / 100) * 12.6))
            gameScreen.blit(cupIMG, cupIMG.get_rect(center=(screen_width // 2, screen_height / 100 * 20)))
        else:
            keyPic = pygame.image.load(f"assets/keys/key{hardShip}.png")
            keyIMG = pygame.transform.scale(keyPic, ((screen_width / 100) * 19.93, (screen_width / 100) * 10))
            gameScreen.blit(keyIMG, keyIMG.get_rect(center=(screen_width // 2, screen_height / 100 * 20)))

        GOver = font.render("...!You Win This HardShip!...", True, (25, 200, 0))
        gameScreen.blit(GOver, GOver.get_rect(center=(screen_width // 2, screen_height / 100 * 40)))
        TGScore = font.render("Your Score: " + str(score), True, (0, 25, 200))
        gameScreen.blit(TGScore, TGScore.get_rect(center=(screen_width // 2, screen_height / 100 * 50)))
        BGScore = font.render("HardShip: " + str(hardShip), True, (200, 0, 25))
        gameScreen.blit(BGScore, BGScore.get_rect(center=(screen_width // 2, screen_height / 100 * 60)))

    def godPowerGift():
        global godPowerGiftStatus

        if random.randint(0, 1) == 1:
            godPowerGiftStatus = True
        else:
            godPowerGiftStatus = False

    def moveGodPowerGift():
        global godPowerGiftStatus
        global godPowerGiftSpeed
        global godPowerPos
        global power
        global galb

        collisionT = binTPos[0] < godPowerPos[0] < binTPos[0] + 100 and binTPos[1] < godPowerPos[1] < binTPos[1] + 75
        collisionK = binKPos[0] < godPowerPos[0] < binKPos[0] + 100 and binKPos[1] < godPowerPos[1] < binKPos[1] + 75

        if godPowerPos[1] == 0:
            font = emojiFont
            godPowerPos = [random.randint(0, screen_width), godPowerGiftSpeed]
            gameScreen.blit(galb, (godPowerPos[0], godPowerPos[1]))
        elif collisionT or collisionK:
            power += 1.0
            playCorrectMusic()
            godPowerGiftStatus = False
            godPowerPos = [0, 0]
        else:
            font = emojiFont
            galb = font.render("♥", True, (255, 0, 0))
            godPowerPos[1] += godPowerGiftSpeed
            gameScreen.blit(galb, (godPowerPos[0], godPowerPos[1]))
            return True

    playMusic()
    startCountDown()
    start_ticks = pygame.time.get_ticks()

    while running:
        if not gameOverStatus:
            makeScreenClear()
            update_information()
            move_garbages()
            move_bins()
            if godPowerGiftStatus:
                moveGodPowerGift()

            clock.tick(fps)
            pygame.display.update()

            if score >= 20 + [0, 15, 30][hardShip - 1]:
                gameWin()

            if int(power) <= 0:
                gameOver()

            if int(power) > ((hardShip * 2) + 1):
                power = ((hardShip * 2) + 1)

            if int(power - 0.0) % 1 == 0 and int(power) != ((hardShip * 2) + 1):
                godPowerGift()

            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.locals.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.locals.K_LEFT]:
                        binKMoveState = "l"
                    elif pygame.key.get_pressed()[pygame.locals.K_RIGHT]:
                        binKMoveState = "r"
                    if pygame.key.get_pressed()[pygame.locals.K_a]:
                        binTMoveState = "l"
                    elif pygame.key.get_pressed()[pygame.locals.K_d]:
                        binTMoveState = "r"
                if event.type == pygame.locals.KEYUP:
                    binTMoveState = False
                    binKMoveState = False
        else:
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    running = False
                    pygame.quit()
            if running:
                pygame.display.update()

showMainWindow()