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
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 3)
strikezone = pygame.Rect((565, 390), (130, 170))
yes = True
fourseamballsize = 11
strikezonedrawn = True

popsfx = pygame.mixer.Sound("popsfx.mp3")
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








strikezonetoggle = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1080,0), (200,50)),
                                      text = 'strikezonetoggle',
                                      manager=manager)


leftyfastball = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (200,50,)),
                                        text= 'leftyfastball',
                                        manager=manager)

leftyslider = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 50), (200,50,)),
                                        text= 'leftyslider',
                                        manager=manager)

leftychangeup = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 100), (200,50,)),
                                        text= 'leftychangeup',
                                        manager=manager)

salepitch = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 500), (200,50,)),
                                        text= 'salepitch',
                                        manager=manager)

rightyfastball = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1080, 100), (200,50,)),
                                        text= 'rightyfastball',
                                        manager=manager)

rightyhighfastball = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1080, 150), (200,50,)),
                                        text= 'rightyhighfastball',
                                        manager=manager)

rightyslider = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1080, 200), (200,50,)),
                                        text= 'rightyslider',
                                        manager=manager)




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
















def simulateadvanced(yes, ball_pos, horizontalspeed,
                        horizontalacceleration, verticalspeed, verticalacceleration,
                        ballsize, traveltime, verticalbreak,
                        horizontalbreak, breaktime):

    soundplayed = 0
    starttime = pygame.time.get_ticks()
    while yes:
        current_time = pygame.time.get_ticks()
        if current_time < starttime + breaktime:

            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            pitcher(j,k)
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

        elif current_time > starttime + breaktime and current_time < starttime + traveltime:

            time_delta = clock.tick(60)/1000.0
            screen.fill("black")


            pitcher(j,k)
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

            if current_time > ((starttime + traveltime) - 125) and current_time < starttime + traveltime and soundplayed == 0:
                popsfx.play()
                soundplayed += 1

        elif current_time > starttime + traveltime:
            global pitchertype
            pitchertype = 1
            yes = False

    return 1


def simulateadvancedlefty(yes, ball_pos, horizontalspeed,
                        horizontalacceleration, verticalspeed, verticalacceleration,
                        ballsize, traveltime, verticalbreak,
                        horizontalbreak, breaktime):

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

    return 1



def simulateadvancedrighty(yes, ball_pos, horizontalspeed,
                        horizontalacceleration, verticalspeed, verticalacceleration,
                        ballsize, traveltime, verticalbreak,
                        horizontalbreak, breaktime):

    soundplayed = 0
    starttime = pygame.time.get_ticks()
    while yes:
        current_time = pygame.time.get_ticks()
        if current_time < starttime + 300:
            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            rightyone(c,d)
            if strikezonedrawn == True:
                pygame.draw.rect(screen, "white", strikezone, 1)

            homeplate()
            batter(x,y)
            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

        if current_time > starttime + 300 and current_time < starttime + 500:
            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            rightytwo(c,d)
            if strikezonedrawn == True:
                pygame.draw.rect(screen, "white", strikezone, 1)

            homeplate()
            batter(x,y)
            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

        if current_time > starttime + 500 and current_time < starttime + 800:
            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            rightythree(c,d)
            if strikezonedrawn == True:
                pygame.draw.rect(screen, "white", strikezone, 1)

            homeplate()
            batter(x,y)
            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

        if current_time > starttime + 800 and current_time < starttime + 1000:
            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            rightyfour(c,d)
            if strikezonedrawn == True:
                pygame.draw.rect(screen, "white", strikezone, 1)

            homeplate()
            batter(x,y)
            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

        if current_time > starttime + 1000 and current_time < starttime + 1100:
            time_delta = clock.tick(60)/1000.0
            screen.fill("black")

            rightyfive(c,d+10)
            if strikezonedrawn == True:
                pygame.draw.rect(screen, "white", strikezone, 1)

            homeplate()
            batter(x,y)
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

            homeplate()
            batter(x,y)

            if strikezonedrawn == True:
                pygame.draw.rect(screen, "white", strikezone, 1)


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

            homeplate()
            batter(x,y)

            if strikezonedrawn == True:
                pygame.draw.rect(screen, "white", strikezone, 1)


            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()


        elif current_time > starttime + breaktime + 1150 and current_time < starttime + traveltime + 1150:

            time_delta = clock.tick(60)/1000.0
            screen.fill("black")


            rightyseven(c,d+10)
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

            if current_time > ((starttime + traveltime + 1150) - 125) and current_time < starttime + traveltime + 1250 and soundplayed == 0:
                popsfx.play()
                soundplayed += 1

        elif current_time > starttime + traveltime + 1150:
            global pitchertype
            pitchertype = 2
            yes = False

    return 1


















while running:

    time_delta = clock.tick(60)/1000.0




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


            # sinker
            # ball_pos = pygame.Vector2((screen.get_width() / 2) - 100, (screen.get_height() / 3) - 30 )
            # simulateadvanced(True, ball_pos, 1.2, -0.01, 3.5, 0.2, 5, 475, 1.3, -0.35, 200)

            # curveball upper left
            # ball_pos = pygame.Vector2((screen.get_width() / 2) - 100, (screen.get_height() / 3) - 30 )
            # simulateadvanced(True, ball_pos, 2.3, -0.05, -2, 0.3, 5, 520, 1.4, -0.07, 220)


            # high fourseam
            # ball_pos = pygame.Vector2((screen.get_width() / 2) - 100, (screen.get_height() / 3) - 30 )
            # simulateadvanced(True, ball_pos, 2, -0.01, -1.2, 0.35, 5, 450, 0.35, -0.02, 200)

            # fourseam mid mid
            # ball_pos = pygame.Vector2((screen.get_width() / 2) - 100, (screen.get_height() / 3) - 30 )
            # simulateadvanced(True, ball_pos, 1, 0.2, 0.3, 0.65, 5, 450, 1.0, 0.1, 240)

            # changeup down mid
            # ball_pos = pygame.Vector2((screen.get_width() / 2) - 100, (screen.get_height() / 3) - 30 )
            # simulateadvanced(True, ball_pos, 1.5, 0.15, -0.55, 0.8, 5, 495, 1.15, -0.075, 240)

            # slider down away
            # ball_pos = pygame.Vector2((screen.get_width() / 2) - 100, (screen.get_height() / 3) - 30 )
            # simulateadvanced(True, ball_pos, -0.5, 0.2, 3, 0.5, 5, 480, 0.75, 1.3, 300)


            # changeup down in
            # ball_pos = pygame.Vector2((screen.get_width() / 2) - 100, (screen.get_height() / 3) - 30 )
            # simulateadvanced(True, ball_pos, 0.5, 0.05, 0.3, 0.65, 5, 495, 1.3, -0.4, 250)

            # fourseam down in strike
            # ball_pos = pygame.Vector2((screen.get_width() / 2) - 100, (screen.get_height() / 3) - 30 )
            # simulateadvanced(True, ball_pos, 0.7, 0.05, 0.3, 0.65, 5, 450, 1.8, 0.037, 300)



            if event.ui_element == leftyfastball:
                xoffset = random.uniform(-1, 5)
                yoffset = random.uniform(-3, 3)
                ball_pos = pygame.Vector2((screen.get_width() / 2) + 90, (screen.get_height() / 3) + 70 )
                simulateadvancedlefty(True, ball_pos, -5 + xoffset, -0.2, 0.2 + yoffset, 0.50, 4, 400, 0.65, -0.15, 240)

            if event.ui_element == leftyslider:
                xoffset = random.uniform(-0.5, 3)
                yoffset = random.uniform(0, 2)
                ball_pos = pygame.Vector2((screen.get_width() / 2) + 90, (screen.get_height() / 3) + 70 )
                simulateadvancedlefty(True, ball_pos, -2 + xoffset, -0.3, 0.2 + yoffset, 0.4, 4, 520, 0.5, -0.65, 300)


            if event.ui_element == leftychangeup:
                xoffset = random.uniform(-4, 1)
                yoffset = random.uniform(-1, 2)
                ball_pos = pygame.Vector2((screen.get_width() / 2) + 90, (screen.get_height() / 3) + 70 )
                simulateadvancedlefty(True, ball_pos, -3 + xoffset, 0.15, 0.2 + yoffset, 0.5, 4, 460, 0.7, 0.3, 300)

            if event.ui_element == salepitch:
                leftypitch = random.randint(1,3)
                if leftypitch == 1:
                    xoffset = random.uniform(-1, 5)
                    yoffset = random.uniform(-3, 3)
                    ball_pos = pygame.Vector2((screen.get_width() / 2) + 90, (screen.get_height() / 3) + 70 )
                    simulateadvancedlefty(True, ball_pos, -5 + xoffset, -0.2, 0.2 + yoffset, 0.50, 4, 400, 0.65, -0.15, 240)
                elif leftypitch == 2:
                    xoffset = random.uniform(-0.5, 3)
                    yoffset = random.uniform(0, 2)
                    ball_pos = pygame.Vector2((screen.get_width() / 2) + 90, (screen.get_height() / 3) + 70 )
                    simulateadvancedlefty(True, ball_pos, -2 + xoffset, -0.3, 0.2 + yoffset, 0.4, 4, 520, 0.5, -0.65, 300)
                elif leftypitch == 3:
                    xoffset = random.uniform(-4, 1)
                    yoffset = random.uniform(-1, 2)
                    ball_pos = pygame.Vector2((screen.get_width() / 2) + 90, (screen.get_height() / 3) + 70 )
                    simulateadvancedlefty(True, ball_pos, -3 + xoffset, 0.15, 0.2 + yoffset, 0.5, 4, 460, 0.7, 0.3, 300)

            if event.ui_element == rightyfastball:
                xoffset = random.uniform(-0.5, 2)
                yoffset = random.uniform(-1, 1)
                ball_pos = pygame.Vector2((screen.get_width() / 2) - 20, (screen.get_height() / 3) + 80 )
                simulateadvancedrighty(True, ball_pos, 1.5 + xoffset, -0.025, 6 + yoffset, 0.1, 4, 390, 0.1, -0.025, 200)

            if event.ui_element == rightyslider:
                xoffset = random.uniform(-1, 1)
                yoffset = random.uniform(-1, 1)
                ball_pos = pygame.Vector2((screen.get_width() / 2) - 20, (screen.get_height() / 3) + 80 )
                simulateadvancedrighty(True, ball_pos, 0.3 + xoffset, 0.025, 6 + yoffset, 0.1, 4, 410, 1.7, 0.8, 250)

            if event.ui_element == rightyhighfastball:
                xoffset = random.uniform(-3, 3)
                yoffset = random.uniform(-1, 1)
                ball_pos = pygame.Vector2((screen.get_width() / 2) - 20, (screen.get_height() / 3) + 80 )
                simulateadvancedrighty(True, ball_pos, 0.3 + xoffset, 0, 3 + yoffset, 0, 4, 390, 0, 0, 250)

        manager.process_events(event)

    manager.update(time_delta)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")



    if strikezonedrawn == True:
        pygame.draw.rect(screen, "white", strikezone, 1)


    pygame.draw.circle(screen, "white", ball_pos, fourseamballsize, 2)
    homeplate()



    batter(x,y)
    drawbat()

    manager.draw_ui(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()



    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.


pygame.quit()