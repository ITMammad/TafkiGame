import pygame
import random
import tkinter
import pygame.locals
from PIL import Image, ImageTk
import tkinter.ttk as modernTKinter

ashghal_one_comsDown_status = True
ashghal_two_comsDown_status = True
clock = pygame.time.Clock()
ashghal_one_pos = [0, 0]
ashghal_two_pos = [0, 0]
ashghal_one_speed = 0
ashghal_two_speed = 0
monitor_height = 0
monitor_width = 0
screen_height = 0
screen_width = 0
ashghal_one = []
ashghal_two = []
satlsSpeed = 25
running = True
timer = 0
score = 0
fps = 40
speeds = [
    [
        0.25,
        0.50,
        0.75,
        1.00,
        1.25
    ],
    [
        0.75,
        1.00,
        1.25,
        1.50,
        1.75
    ],
    [
        1.25,
        1.50,
        1.75,
        2.00,
        2.25
    ]
]
ashghalsT = [
    ["assets/ashghals/T/1.png", [50, 120]],
    ["assets/ashghals/T/2.png", [50, 127]],
    ["assets/ashghals/T/3.png", [50, 114]],
    ["assets/ashghals/T/4.png", [50, 61]],
    ["assets/ashghals/T/5.png", [50, 51]],
    ["assets/ashghals/T/6.png", [50, 79]],
    ["assets/ashghals/T/7.png", [50, 30]],
    ["assets/ashghals/T/8.png", [50, 43]],
    ["assets/ashghals/T/9.png", [50, 79]],
    ["assets/ashghals/T/10.png", [50, 26]],
]
ashghalsK = [
    ["assets/ashghals/K/1.png", [50, 41]],
    ["assets/ashghals/K/2.png", [50, 51]],
    ["assets/ashghals/K/3.png", [50, 47]],
    ["assets/ashghals/K/4.png", [50, 49]],
    ["assets/ashghals/K/5.png", [50, 31]],
    ["assets/ashghals/K/6.png", [50, 48]],
    ["assets/ashghals/K/7.png", [50, 57]],
    ["assets/ashghals/K/8.png", [50, 87]],
    ["assets/ashghals/K/9.png", [50, 27]],
    ["assets/ashghals/K/10.png", [50, 73]],
]
ashghal_types = [ashghalsT, ashghalsK]
satlTPos = [0, screen_height - 200]
satlKPos = [screen_width - 100, screen_height - 100]

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
    y = (screen_height / 2) - (500 / 2)
    howToWindow.geometry('%dx%d+%d+%d' % (500, 500, x, y))
    howToFrame = modernTKinter.Frame(howToWindow, padding=10)
    howToFrame.pack()
    img = ImageTk.PhotoImage(Image.open(r"assets/img/howTo.png").resize((480, 480)))
    panel = modernTKinter.Label(howToFrame, image=img)
    panel.pack()
    howToWindow.resizable(False, False)
    howToWindow.mainloop()

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
    global ashghal_one_comsDown_status
    global ashghal_two_comsDown_status
    global ashghal_one_speed
    global ashghal_two_speed
    global ashghal_one_pos
    global ashghal_two_pos
    global monitor_height
    global monitor_width
    global screen_height
    global ashghal_types
    global screen_width
    global ashghalsT
    global ashghalsK
    global running
    global timer
    global score

    global satlTPos
    global satlKPos

    timer = hardShip * 15

    screen_height = monitor_height / 2 + 150
    screen_width = monitor_width / 2 + 250

    satlTPos = [0, screen_height - 150]
    satlKPos = [screen_width - 100, screen_height - 75]

    pygame.init()
    gameScreen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('TafkiGame')
    Icon = pygame.image.load('assets/img/logo.png')
    pygame.display.set_icon(Icon)
    bgPic = pygame.image.load("assets/img/bg.jpg")
    bgIMG = pygame.transform.scale(bgPic, (screen_width, screen_height))
    gameScreen.blit(bgIMG, (0, 0))

    def makeScreenClear():
        gameScreen.fill((255, 255, 255))
        gameScreen.blit(bgIMG, (0, 0))

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

    # def move_ashghals():
    #     global ashghal_one_comsDown_status
    #     global ashghal_two_comsDown_status
    #     global ashghal_one_speed
    #     global ashghal_two_speed
    #     global ashghal_one_pos
    #     global ashghal_two_pos
    #     global screen_height
    #     global ashghal_types
    #     global screen_width
    #     global ashghal_one
    #     global ashghal_two
    #     global speeds
    #     global score

    #     if ashghal_one_comsDown_status:
    #         ashghal_type = ashghal_types[0]
    #         ashghal = ashghal_type[random.randint(0, 9)]
    #         ashghal_one = ashghal
    #         ashghalPic = pygame.image.load(ashghal[0])
    #         ashghalIMG = pygame.transform.scale(ashghalPic, (ashghal[1][1], ashghal[1][0]))
    #         ashghal_one_pos = [random.randint(0, screen_width - ashghal[1][0]), 0]
    #         ashghal_one_speed = speeds[hardShip - 1][random.randint(0, 4)]
    #         gameScreen.blit(ashghalIMG, (ashghal_one_pos[0], ashghal_one_pos[1]))
    #         ashghal_one_comsDown_status = False
    #     else:
    #         if check_collision(1):
    #             score += 1
    #             ashghal_one_comsDown_status = True
    #         elif not ashghal_one_pos[1] + ashghal_one[1][1] >= screen_height:
    #             makeScreenClear()
    #             ashghal_one_pos[1] += ashghal_one_speed
    #             gameScreen.blit(ashghalIMG, (ashghal_one_pos[0], ashghal_one_pos[1]))
    #         elif ashghal_one_pos[1] + ashghal_one[1][1] >= screen_height:
    #             makeScreenClear()
    #             print("Finished!...")
    #             score -= 1
    #             ashghal_one_comsDown_status = True
    #         else:
    #             print("An Other Thing...")

    #     if ashghal_two_comsDown_status:
    #         ashghal_type = ashghal_types[1]
    #         ashghal = ashghal_type[random.randint(0, 9)]
    #         ashghal_two = ashghal
    #         ashghalPic = pygame.image.load(ashghal[0])
    #         ashghalIMG = pygame.transform.scale(ashghalPic, (ashghal[1][1], ashghal[1][0]))
    #         ashghal_two_pos = [random.randint(0, screen_width - ashghal[1][0]), 0]
    #         while ashghal_two_pos == ashghal_one_pos:
    #             ashghal_two_pos = [random.randint(0, screen_width - ashghal[1][0]), 0]
    #         ashghal_two_speed = speeds[hardShip - 1][random.randint(0, 4)]
    #         gameScreen.blit(ashghalIMG, (ashghal_two_pos[0], ashghal_two_pos[1]))
    #         ashghal_two_comsDown_status = False
    #     else:
    #         if check_collision(1):
    #             score += 1
    #             ashghal_two_comsDown_status = True
    #         elif not ashghal_two_pos[1] + ashghal_two[1][1] >= screen_height:
    #             makeScreenClear()
    #             ashghal_two_pos[1] += ashghal_two_speed
    #             gameScreen.blit(ashghalIMG, (ashghal_two_pos[0], ashghal_two_pos[1]))
    #         elif ashghal_two_pos[1] + ashghal_two[1][1] >= screen_height:
    #             makeScreenClear()
    #             print("Finished!...")
    #             score -= 1
    #             ashghal_two_comsDown_status = True
    #         else:
    #             print("An Other Thing...")

    #     print("Score: " + str(score))

    def move_ashghals():
        global ashghal_one_comsDown_status
        global ashghal_two_comsDown_status
        global ashghal_one_speed
        global ashghal_two_speed
        global ashghal_one_pos
        global ashghal_two_pos
        global ashghal_types
        global screen_height
        global screen_width
        global ashghal_one
        global ashghal_two
        global speeds
        global score

        makeScreenClear()

        if ashghal_one_comsDown_status:
            ashghal_one = ashghal_types[0][random.randint(0, 9)]
            ashghalPic = pygame.image.load(ashghal_one[0])
            ashghalIMG = pygame.transform.scale(ashghalPic, (ashghal_one[1][1], ashghal_one[1][0]))
            ashghal_one_pos = [random.randint(0, screen_width - ashghal_one[1][0]), 0]
            ashghal_one_speed = speeds[hardShip - 1][random.randint(0, 4)]
            gameScreen.blit(ashghalIMG, (ashghal_one_pos[0], ashghal_one_pos[1]))
            ashghal_one_comsDown_status = False
            print("Blited!...")
        elif check_collision(1):
            score += 1
            ashghal_one_comsDown_status = True
        elif ashghal_one_pos[1] + ashghal_one[1][1] >= screen_height:
            score -= 1
            ashghal_one_comsDown_status = True
            print("Finished!...")
        else:
            ashghal_one_pos[1] += ashghal_one_speed
            ashghalPic = pygame.image.load(ashghal_one[0])
            ashghalIMG = pygame.transform.scale(ashghalPic, (ashghal_one[1][1], ashghal_one[1][0]))
            gameScreen.blit(ashghalIMG, (ashghal_one_pos[0], ashghal_one_pos[1]))
            print("Goes Downer!...")

    def move_satls():
        global satlTPos
        global satlKPos

        makeScreenClear()

        satlTPic = pygame.image.load("assets/bins/T.png")
        satlTIMG = pygame.transform.scale(satlTPic, (100, 75))
        gameScreen.blit(satlTIMG, (satlTPos[0], satlTPos[1]))
        satlKPic = pygame.image.load("assets/bins/K.png")
        satlKIMG = pygame.transform.scale(satlKPic, (100, 75))
        gameScreen.blit(satlKIMG, (satlKPos[0], satlKPos[1]))

    def check_collision(t):
        return False

    def move_satlsT(wh):
        global satlTPos
        global satlsSpeed

        if wh == "r":
            if not satlTPos[0] + 100 >= screen_width:
                satlTPos[0] += satlsSpeed
        elif wh == "l":
            if not satlTPos[0] - satlsSpeed < 0:
                satlTPos[0] -= satlsSpeed

    def move_satlsK(wh):
        global satlKPos
        global satlsSpeed

        if wh == "r":
            if not satlKPos[0] + 100 >= screen_width:
                satlKPos[0] += satlsSpeed
        elif wh == "l":
            if not satlKPos[0] - satlsSpeed < 0:
                satlKPos[0] -= satlsSpeed

    # playMusic()
    # startCountDown()

    while running:
            move_ashghals()
            move_satls()

            clock.tick(fps)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.locals.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.locals.K_LEFT]:
                        move_satlsK("l")
                    elif pygame.key.get_pressed()[pygame.locals.K_RIGHT]:
                        move_satlsK("r")
                    if pygame.key.get_pressed()[pygame.locals.K_a]:
                        move_satlsT("l")
                    elif pygame.key.get_pressed()[pygame.locals.K_d]:
                        move_satlsT("r")

    pygame.quit()

showMainWindow()