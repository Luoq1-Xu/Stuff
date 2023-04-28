# Example file showing a circle moving on screen
import pygame
import pygame_gui
import random


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

manager = pygame_gui.UIManager((1280, 720))

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
strikezone = pygame.Rect((565, 400), (130, 165))
ball_pos = (0,0)
yes = True
fourseamballsize = 11
strikezonedrawn = True

menu_state = 0

pitchnumber = 0
currentballs = 0
currentstrikes = 0

currentouts = 0
currentstrikeouts = 0
currentwalks = 0

runners = 0

popsfx = pygame.mixer.Sound("popsfx.mp3")
strikecall = pygame.mixer.Sound("STRIKECALL.mp3")
ballcall = pygame.mixer.Sound("BALLCALL.mp3")



batterimg = pygame.image.load('better.png')
pitcherimg = pygame.image.load('small.png')
leftypitcher = pygame.image.load('lefty.png')
leftywindup = pygame.image.load('windup.png')
leftyfollowthrough = pygame.image.load('salemini.png')
leftyend = pygame.image.load('salefrontmini.png')


righty1 = pygame.image.load('righty1.png')
righty2 = pygame.image.load('righty2.png')
righty3 = pygame.image.load('righty3.png')
righty4 = pygame.image.load('righty4.png')
righty5 = pygame.image.load('righty5.png')
righty6 = pygame.image.load('righty6.png')
righty7 = pygame.image.load('righty7.png')


isstrike = 0




strikezonetoggle = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((540,0), (200,50)),
                                        text = 'strikezonetoggle',
                                        manager=manager)

salepitch = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (200,50,)),
                                            text= 'salepitch',
                                            manager=manager)

degrompitch = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1080, 0), (200,50,)),
                                            text= 'degrompitch',
                                            manager=manager)


swing = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((540, 80), (200,50,)),
                                            text= 'swing',
                                            manager=manager)


def check_menu():
    global currentouts
    global menu_state
    if currentouts == 3:
        menu_state = 1
    return

def inning_summary(summary):
    return pygame_gui.elements.UITextBox(summary,relative_rect=pygame.Rect((440, 160), (400,400,)),
                                        manager=manager)


def pitchresult(input):
    return pygame_gui.elements.UITextBox(input,relative_rect=pygame.Rect((980, 400), (200,100,)),
                                        manager=manager)


def drawscoreboard(results):
    return pygame_gui.elements.UITextBox(results,relative_rect=pygame.Rect((980, 200), (200,100,)),
                                        manager=manager)


def basesempty_graphic():
    pygame.draw.polygon(screen, "white", ((1000, 550), (1025, 575), (1000,600), (975,575)), 3)
    pygame.draw.polygon(screen, "white", ((1035, 585), (1060, 610), (1035,635), (1010,610)), 3)
    pygame.draw.polygon(screen, "white", ((965, 585), (990, 610), (965,635), (940,610)), 3)
    return

def runnerfirst_graphic():
    pygame.draw.polygon(screen, "white", ((1000, 550), (1025, 575), (1000,600), (975,575)), 3)
    pygame.draw.polygon(screen, "yellow", ((1035, 585), (1060, 610), (1035,635), (1010,610)),)
    pygame.draw.polygon(screen, "white", ((965, 585), (990, 610), (965,635), (940,610)), 3)
    return

def runnerfirstsecond_graphic():
    pygame.draw.polygon(screen, "yellow", ((1000, 550), (1025, 575), (1000,600), (975,575)),)
    pygame.draw.polygon(screen, "yellow", ((1035, 585), (1060, 610), (1035,635), (1010,610)),)
    pygame.draw.polygon(screen, "white", ((965, 585), (990, 610), (965,635), (940,610)), 3)
    return

def basesloaded_graphic():
    pygame.draw.polygon(screen, "yellow", ((1000, 550), (1025, 575), (1000,600), (975,575)),)
    pygame.draw.polygon(screen, "yellow", ((1035, 585), (1060, 610), (1035,635), (1010,610)),)
    pygame.draw.polygon(screen, "yellow", ((965, 585), (990, 610), (965,635), (940,610)),)
    return

def draw_static():
    global strikezonedrawn
    global runners
    if strikezonedrawn == True:
                pygame.draw.rect(screen, "white", strikezone, 1)
    if runners == 0:
        basesempty_graphic()
    elif runners == 1:
        runnerfirst_graphic()
    elif runners == 2:
        runnerfirstsecond_graphic()
    elif runners == 3:
        basesloaded_graphic()
    homeplate()
    batter(x,y)
    return


def drawbat():

    mousepos = pygame.mouse.get_pos()
    player_pos.x = mousepos[0]
    player_pos.y = mousepos[1]
    x = player_pos.x
    y = player_pos.y

    pygame.draw.polygon(screen, "white", ((x, y + 3 ), (x + 5, y + 3), (x + 12, y + 6), (x + 40, y + 6),
                                            (x + 150, y), (x + 200, y), (x + 200, y + 20),
                                            (x + 150, y + 20), (x + 40, y + 14),
                                            (x + 12, y + 14), (x + 5, y + 17),
                                            (x, y + 17)), 2)

    return


#righty starting x pos
c = (screen.get_width() / 2) - 40
d = (screen.get_height() / 3) + 50



x = 330
y = 190

j = (screen.get_width() / 2) - 105
k = (screen.get_height() / 3) - 40

a = (screen.get_width() / 2) - 115
b = (screen.get_height() / 3) + 50


def batter(x,y):
    screen.blit(batterimg, (x,y))

def pitcher(j,k):
    screen.blit(pitcherimg, (j,k))

def lefty(j,k):
    screen.blit(leftypitcher, (j,k))

def winduplefty(a,b):
    screen.blit(leftywindup, (a,b))

def followthroughlefty(a,b):
    screen.blit(leftyfollowthrough, (a,b))

def endlefty(a,b):
    screen.blit(leftyend, (a,b))

def homeplate():
    pygame.draw.polygon(screen, "white", ((565, 650), (695, 650), (695, 670), (630, 700), (565, 670)), 3)



def rightyone(x,y):
    screen.blit(righty1, (x,y))

def rightytwo(x,y):
    screen.blit(righty2, (x,y))

def rightythree(x,y):
    screen.blit(righty3, (x,y))

def rightyfour(x,y):
    screen.blit(righty4, (x,y))

def rightyfive(x,y):
    screen.blit(righty5, (x,y))

def rightysix(x,y):
    screen.blit(righty6, (x,y))

def rightyseven(x,y):
    screen.blit(righty7, (x,y))









def simulateadvancedlefty(yes, ball_pos, horizontalspeed,
                        horizontalacceleration, verticalspeed, verticalacceleration,
                        ballsize, traveltime, verticalbreak,
                        horizontalbreak, breaktime):


    inatbat = True

    soundplayed = 0
    starttime = pygame.time.get_ticks()
    while yes:
        current_time = pygame.time.get_ticks()
        if current_time < starttime + 1000:
            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            winduplefty(a,b)
            if strikezonedrawn == True:
                pygame.draw.rect(screen, "white", strikezone, 1)

            homeplate()
            batter(x,y)
            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()


        if current_time > starttime + 1000 and current_time < starttime + 1070:

            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            lefty(a,b)
            pygame.draw.circle(screen, "white", ball_pos, ballsize)
            ball_pos.y += verticalspeed
            ball_pos.x += horizontalspeed
            horizontalspeed += horizontalacceleration
            verticalspeed += verticalacceleration
            ballsize = ballsize * 1.030

            homeplate()
            batter(x,y)

            if strikezonedrawn == True:
                pygame.draw.rect(screen, "white", strikezone, 1)


            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

        if current_time > starttime + 1070 and current_time < starttime + breaktime + 1000:

            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            followthroughlefty(a,b)
            pygame.draw.circle(screen, "white", ball_pos, ballsize)
            ball_pos.y += verticalspeed
            ball_pos.x += horizontalspeed
            horizontalspeed += horizontalacceleration
            verticalspeed += verticalacceleration
            ballsize = ballsize * 1.030

            homeplate()
            batter(x,y)

            if strikezonedrawn == True:
                pygame.draw.rect(screen, "white", strikezone, 1)


            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()


        elif current_time > starttime + breaktime + 1000 and current_time < starttime + traveltime + 1000:

            time_delta = clock.tick(60)/1000.0
            screen.fill("black")


            followthroughlefty(a,b)
            pygame.draw.circle(screen, "white", ball_pos, ballsize)
            ball_pos.y += verticalspeed
            ball_pos.x += horizontalspeed
            horizontalspeed += horizontalbreak
            verticalspeed += verticalbreak
            ballsize = ballsize * 1.030

            homeplate()
            batter(x,y)

            if strikezonedrawn == True:
                pygame.draw.rect(screen, "white", strikezone, 1)

            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

            if current_time > ((starttime + traveltime + 1000) - 125) and current_time < starttime + traveltime + 1000 and soundplayed == 0:
                popsfx.play()
                soundplayed += 1

        elif current_time > starttime + traveltime + 1000:
            global pitchertype
            pitchertype = 2
            yes = False

            inatbat == False

    return 1



def simulateadvancedrighty(yes, ball_pos, horizontalspeed,
                        horizontalacceleration, verticalspeed, verticalacceleration,
                        ballsize, traveltime, verticalbreak,
                        horizontalbreak, breaktime):

    global currentballs
    global pitchnumber
    global currentstrikes
    global string
    global currentouts
    global currentstrikeouts
    global currentwalks
    global runners

    salepitch.hide()
    strikezonetoggle.hide()
    degrompitch.hide()


    swing.show()
    soundplayed = 0
    starttime = pygame.time.get_ticks()
    while yes:
        current_time = pygame.time.get_ticks()
        if current_time < starttime + 300:
            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            rightyone(c,d)
            draw_static()
            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

        if current_time > starttime + 300 and current_time < starttime + 500:
            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            rightytwo(c,d)
            draw_static()
            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

        if current_time > starttime + 500 and current_time < starttime + 800:
            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            rightythree(c,d)
            draw_static()
            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

        if current_time > starttime + 800 and current_time < starttime + 1000:
            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            rightyfour(c,d)
            draw_static()
            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

        if current_time > starttime + 1000 and current_time < starttime + 1100:
            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            rightyfive(c,d+10)
            draw_static()
            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

        if current_time > starttime + 1100 and current_time < starttime + 1150:


            time_delta = clock.tick(60)/1000.0
            screen.fill("black")


            rightysix(c,d+10)
            pygame.draw.circle(screen, "white", ball_pos, ballsize)
            ball_pos.y += verticalspeed
            ball_pos.x += horizontalspeed
            horizontalspeed += horizontalacceleration
            verticalspeed += verticalacceleration
            ballsize = ballsize * 1.030

            draw_static()

            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

        if current_time > starttime + 1150 and current_time < starttime + breaktime + 1150:


            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            rightyseven(c,d+10)
            pygame.draw.circle(screen, "white", ball_pos, ballsize)
            ball_pos.y += verticalspeed
            ball_pos.x += horizontalspeed
            horizontalspeed += horizontalacceleration
            verticalspeed += verticalacceleration
            ballsize = ballsize * 1.030

            draw_static()


            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()


        elif current_time > starttime + breaktime + 1150 and current_time < starttime + traveltime + 1150:

            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            if current_time > starttime + traveltime + 1000:
                swing.hide()


            rightyseven(c,d+10)
            pygame.draw.circle(screen, "white", ball_pos, ballsize)
            ball_pos.y += verticalspeed
            ball_pos.x += horizontalspeed
            horizontalspeed += horizontalbreak
            verticalspeed += verticalbreak
            ballsize = ballsize * 1.030

            draw_static()

            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

            if current_time > ((starttime + traveltime + 1150) - 125) and current_time < starttime + traveltime + 1250 and soundplayed == 0:
                popsfx.play()
                soundplayed += 1

        elif current_time > starttime + traveltime + 1150:
            global pitchertype
            pitchertype = 2
            yes = False
            global isstrike
            isstrike = 1
            if collision(ball_pos.x, ball_pos.y, 11, 630, 482.5, 130, 165):
                strikecall.play()

                pitchnumber += 1
                currentstrikes += 1
                #STRIKEOUT OCCURS
                if currentstrikes == 3:
                    string = "PITCH {} : STRIKE<br>COUNT IS {} - {}<br><b>STRIKEOUT</b>".format(pitchnumber, currentballs, currentstrikes)
                    textbox = pitchresult(string)
                    textbox.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
                    currentstrikeouts += 1
                    currentouts +=1
                    result = "CURRENT OUTS : {}<br>STRIKEOUTS : {}<br>WALKS : {}".format(currentouts, currentstrikeouts, currentwalks)
                    scoreboard = drawscoreboard(result)
                    scoreboard.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
                    pitchnumber = 0
                    currentstrikes = 0
                    currentballs = 0
                else:
                    string = "PITCH {} : STRIKE<br>COUNT IS {} - {}<br>".format(pitchnumber, currentballs, currentstrikes)
                    textbox = pitchresult(string)
                    textbox.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
            else:
                ballcall.play()
                currentballs += 1
                pitchnumber += 1
                #WALK OCCURS
                if currentballs == 4:
                    string = "PITCH {} : BALL<br>COUNT IS {} - {}<br><b>WALK</b>".format(pitchnumber, currentballs, currentstrikes)
                    textbox = pitchresult(string)
                    textbox.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
                    currentwalks += 1
                    result = "CURRENT OUTS : {}<br>STRIKEOUTS : {}<br>WALKS : {}".format(currentouts, currentstrikeouts, currentwalks)
                    scoreboard = drawscoreboard(result)
                    scoreboard.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
                    pitchnumber = 0
                    currentstrikes = 0
                    currentballs = 0
                    runners += 1
                else:
                    string = "PITCH {} : BALL<br>COUNT IS {} - {}<br>".format(pitchnumber, currentballs, currentstrikes)
                    textbox = pitchresult(string)
                    textbox.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)

            salepitch.show()
            strikezonetoggle.show()
            degrompitch.show()

    return



def pitch_decision_maker():
    global currentballs
    global currentstrikes
    rando = random.uniform(1,10)
    if ((currentballs == 0 and currentstrikes == 0) or
        (currentballs == 4) or
        (currentstrikes == 3) or
        (currentballs == 1 and currentstrikes ==1) or
        (currentballs == 3 and currentstrikes == 2)
        ):
        if rando >= 1 and rando <=3:
            lowfastball()
        elif rando > 3 and rando <=5:
            highfastball()
        elif rando > 5 and rando <=8:
            lowslider()
        else:
            lowchangeup()
    elif (currentballs == 1 and currentstrikes == 0) or (currentballs == 2 and currentstrikes == 1):
        if rando >=1 and rando <=4:
            lowfastball()
        elif rando > 4 and rando <= 5.5:
            highfastball()
        elif rando > 5.5 and rando <= 8.5:
            lowslider()
        else:
            lowchangeup()
    elif (currentballs == 0 and currentstrikes == 1) or (currentballs == 2 and currentstrikes == 2):
        if rando >= 1 and rando <= 2:
            lowfastball()
        elif rando > 2 and rando <=5:
            highfastball()
        elif rando > 5 and rando <= 7:
            lowslider()
        else:
            lowchangeup()
    elif (currentballs == 2 and currentstrikes == 0) or (currentballs == 3 and currentstrikes == 1) or (currentballs == 3 and currentstrikes == 0) :
        if rando >=1 and rando <=6:
            lowfastball()
        elif rando > 6 and rando <=7:
            highfastball()
        elif rando > 7 and rando <= 9:
            lowslider()
        else:
            lowchangeup()
    elif (currentballs == 0 and currentstrikes == 2) or (currentballs == 1 and currentstrikes == 2):
        if rando >=1 and rando <=2:
            lowfastball()
        elif rando > 2 and rando <=5:
            highfastball()
        elif rando > 5 and rando <=7:
            lowslider()
        else:
            lowchangeup()





#DEGROM PITCH TYPES
def lowfastball():
    xoffset = random.uniform(-0.5, 2)
    yoffset = random.uniform(-1, 1)
    global ball_pos
    ball_pos = pygame.Vector2((screen.get_width() / 2) - 23, (screen.get_height() / 3) + 83 )
    simulateadvancedrighty(True, ball_pos, 3 + xoffset, 0, 6 + yoffset, 0.1, 4, 390, 0.1, -0.25, 150)
    return

def highfastball():
    xoffset = random.uniform(-3, 3)
    yoffset = random.uniform(-2, 1)
    global ball_pos
    ball_pos = pygame.Vector2((screen.get_width() / 2) - 23, (screen.get_height() / 3) + 83 )
    simulateadvancedrighty(True, ball_pos, 0.3 + xoffset, 0, 3 + yoffset, 0, 4, 390, 0, -0.2, 150)
    return

def lowslider():
    xoffset = random.uniform(-1, 1)
    yoffset = random.uniform(-1, 1)
    global ball_pos
    ball_pos = pygame.Vector2((screen.get_width() / 2) - 23, (screen.get_height() / 3) + 83 )
    simulateadvancedrighty(True, ball_pos, 0.3 + xoffset, 0.2, 6 + yoffset, 0.1, 4, 410, 0.6, 0.45, 250)
    return

def lowchangeup():
    xoffset = random.uniform(-3, 3)
    yoffset = random.uniform(-1, 1)
    global ball_pos
    ball_pos = pygame.Vector2((screen.get_width() / 2) - 23, (screen.get_height() / 3) + 83 )
    simulateadvancedrighty(True, ball_pos, 1 + xoffset, -0.01, 5 + yoffset, 0.2, 4, 450, 0.5, -0.3, 170)
    return



# CREDIT TO e-James -> https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection
def collision(circlex, circley, radius, rectmiddlex, rectmiddley, rectwidth, rectheight):
    circleDistancex = abs(circlex - rectmiddlex)
    circleDistancey = abs(circley - rectmiddley)

    if (circleDistancex > (rectwidth/2 + radius)):
        return False

    if (circleDistancey > (rectheight/2 + radius)):
        return False

    if (circleDistancex <= (rectwidth/2)):
        return True
    if (circleDistancey <= (rectheight/2)):
        return True

    cornerDistance_sq = ((circleDistancex - rectwidth/2)**2) + ((circleDistancey - rectheight/2)**2)

    return (cornerDistance_sq <= ((radius)**2))








while running:

    time_delta = clock.tick(60)/1000.0

    check_menu()


    if menu_state == 1:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:

                if event.ui_element == strikezonetoggle:
                    if strikezonedrawn == True:
                        strikezonedrawn = False
                    elif strikezonedrawn == False:
                        strikezonedrawn = True







                if event.ui_element == salepitch:
                    leftypitch = random.randint(1,3)
                    #fastball
                    if leftypitch == 1:
                        xoffset = random.uniform(-1, 5)
                        yoffset = random.uniform(-3, 3)
                        ball_pos = pygame.Vector2((screen.get_width() / 2) + 90, (screen.get_height() / 3) + 70 )
                        simulateadvancedlefty(True, ball_pos, -5 + xoffset, -0.2, 0.2 + yoffset, 0.50, 4, 400, 0.65, -0.15, 240)
                    #slider
                    elif leftypitch == 2:
                        xoffset = random.uniform(-0.5, 3)
                        yoffset = random.uniform(0, 2)
                        ball_pos = pygame.Vector2((screen.get_width() / 2) + 90, (screen.get_height() / 3) + 70 )
                        simulateadvancedlefty(True, ball_pos, -2 + xoffset, -0.3, 0.2 + yoffset, 0.4, 4, 520, 0.5, -0.65, 300)
                    #changeup
                    elif leftypitch == 3:
                        xoffset = random.uniform(-4, 1)
                        yoffset = random.uniform(-1, 2)
                        ball_pos = pygame.Vector2((screen.get_width() / 2) + 90, (screen.get_height() / 3) + 70 )
                        simulateadvancedlefty(True, ball_pos, -3 + xoffset, 0.15, 0.2 + yoffset, 0.5, 4, 460, 0.7, 0.3, 300)




                if event.ui_element == degrompitch:
                    pitch_decision_maker()

            manager.process_events(event)

        manager.update(time_delta)

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        pygame.draw.circle(screen, "white", ball_pos, fourseamballsize, 2)
        draw_static()
        manager.draw_ui(screen)
        # flip() the display to put your work on screen
        pygame.display.flip()

    elif menu_state == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame_gui.UI_TEXT_EFFECT_FINISHED:
                print("whatthefuck")

            manager.process_events(event)


        screen.fill("black")
        okay = True
        while okay == True:
            summary = "INNING OVER<br>INNING SUMMARY :<br>RUNS SCORED : <br>STRIKEOUTS : {}<br>WALKS : {}<br>TOTAL PITCHES : ".format(currentstrikeouts, currentwalks)
            inningstats = inning_summary(summary)
            inningstats.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
            okay = False
        salepitch.hide()
        strikezonetoggle.hide()
        degrompitch.hide()
        swing.hide()
        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()










pygame.quit()