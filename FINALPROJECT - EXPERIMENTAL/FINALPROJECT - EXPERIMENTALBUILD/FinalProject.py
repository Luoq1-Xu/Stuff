# BasedBall : A baseball at-bat simulator
import pygame
import pygame_gui
import random
import button

# pygame setup
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

#Stuff for the typing effect in main menu and summary screen
dt = 0
font = pygame.font.Font('8bitoperator_jve.ttf', 40)
bigfont = pygame.font.Font('8bitoperator_jve.ttf', 70)
snip = font.render('', True, 'white')
counter = 0
speed = 3

#Some more setup
manager = pygame_gui.UIManager((1280, 720), 'theme.json')
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
strikezone = pygame.Rect((565, 400), (130, 165))
ball_pos = (0,0)
yes = True
fourseamballsize = 11
strikezonedrawn = True

#Global variables for menu and resetting
menu_state = 0
just_refreshed = 0
textfinished = 0

#Global game variables
pitchnumber = 0
currentballs = 0
currentstrikes = 0
currentouts = 0
currentstrikeouts = 0
currentwalks = 0
runners = 0
runs_scored = 0
swing_started = 0
hits = 0
hit_type = 0
ishomerun = ''
first_pitch_thrown = False

#Load Sounds
popsfx = pygame.mixer.Sound("popsfx.mp3")
strikecall = pygame.mixer.Sound("STRIKECALL.mp3")
ballcall = pygame.mixer.Sound("BALLCALL.mp3")
foulball = pygame.mixer.Sound("FOULBALL.mp3")
single = pygame.mixer.Sound("SINGLE.mp3")
double = pygame.mixer.Sound("DOUBLE.mp3")
triple = pygame.mixer.Sound("TRIPLE.mp3")
homer = pygame.mixer.Sound("HOMERUN.mp3")
called_strike_3 = pygame.mixer.Sound("CALLEDSTRIKE3.mp3")

#Load images
lefty1 = pygame.image.load('LEFTY1.png').convert_alpha()
lefty2 = pygame.image.load('LEFTY2.png').convert_alpha()
lefty3 = pygame.image.load('LEFTY3.png').convert_alpha()
lefty4 = pygame.image.load('LEFTY4.png').convert_alpha()
lefty5 = pygame.image.load('LEFTY5.png').convert_alpha()
lefty6 = pygame.image.load('LEFTY6.png').convert_alpha()
lefty7 = pygame.image.load('LEFTY7.png').convert_alpha()
lefty8 = pygame.image.load('LEFTY8.png').convert_alpha()
lefty9 = pygame.image.load('LEFTY9.png').convert_alpha()

righty1 = pygame.image.load('RIGHTY1.png').convert_alpha()
righty2 = pygame.image.load('RIGHTY2.png').convert_alpha()
righty3 = pygame.image.load('RIGHTY3.png').convert_alpha()
righty4 = pygame.image.load('RIGHTY4.png').convert_alpha()
righty5 = pygame.image.load('RIGHTY5.png').convert_alpha()
righty6 = pygame.image.load('RIGHTY6.png').convert_alpha()
righty7 = pygame.image.load('RIGHTY7.png').convert_alpha()
righty8 = pygame.image.load('RIGHTY8.png').convert_alpha()
righty9 = pygame.image.load('RIGHTY9.png').convert_alpha()

trout1 = pygame.image.load('1trout.png').convert_alpha()
troutlegraise =pygame.image.load('1.5trout.png').convert_alpha()
trout2 = pygame.image.load('2trout.png').convert_alpha()
trout3 = pygame.image.load('3trout.png').convert_alpha()
trout4 = pygame.image.load('4trout.png').convert_alpha()
trout5 = pygame.image.load('5trout.png').convert_alpha()
trout6 = pygame.image.load('6trout.png').convert_alpha()
trout7 = pygame.image.load('7trout.png').convert_alpha()

trout4high = pygame.image.load('4TROUTHIGH.png').convert_alpha()
trout5high = pygame.image.load('5TROUTHIGH.png').convert_alpha()
trout6high = pygame.image.load('6TROUTHIGH.png').convert_alpha()

salebutton = pygame.image.load('salebutton.png').convert_alpha()
degrombutton = pygame.image.load('degrombutton.png').convert_alpha()
menu = pygame.image.load('MAINMENU.png').convert_alpha()

faceoffsale = button.Button(500,500, salebutton, 0.5)
faceoffdegrom = button.Button(500,600, degrombutton, 0.5)
mainmenubutton = button.Button(540, 530, menu, 0.6)


#Pygame_gui elements (Buttons, textboxes)
strikezonetoggle = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,100), (200,100)),
                                        text = 'STRIKEZONE',
                                        manager=manager)
salepitch = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (200,100)),
                                            text = 'PITCH',
                                            manager=manager)
degrompitch = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (200,100)),
                                            text = 'PITCH',
                                            manager=manager)
backtomainmenu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 620), (200,100)),
                                            text = 'MAIN MENU',
                                            manager=manager)
container = pygame_gui.core.UIContainer(relative_rect=pygame.Rect((0, 0), (1280,720)),manager=manager, is_window_root_container=False)
banner = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((440, 0), (400,100)), manager=manager, text="")
banner.hide()
def pitchresult(input):
    return pygame_gui.elements.UITextBox(input,relative_rect=pygame.Rect((980, 350), (200,150)),
                                        manager=manager)
def drawscoreboard(results):
    return pygame_gui.elements.UITextBox(results,relative_rect=pygame.Rect((980, 150), (200,200)),
                                        manager=manager)

#Container to house the scoreboard and textbox - to allow for previous instances to be deleted when new ones are created
def containerupdate(textbox, scoreboard):
    global container
    container.add_element(textbox)
    container.add_element(scoreboard)
    return

#Function to draw bases graphic
def draw_bases(base1, base2, base3):
    basepeople = [base1, base2, base3]
    coloured = []
    x = 0
    while x < 3:
        if basepeople[x] == "white":
            coloured.append(3)
        elif basepeople[x]== "yellow":
            coloured.append(0)
        x += 1
    pygame.draw.polygon(screen, base1, ((1115, 585), (1140, 610), (1115,635), (1090,610)),coloured[0])
    pygame.draw.polygon(screen, base2, ((1080, 550), (1105, 575), (1080,600), (1055,575)),coloured[1])
    pygame.draw.polygon(screen, base3, ((1045, 585), (1070, 610), (1045,635), (1020,610)),coloured[2])
    return

def homeplate():
    pygame.draw.polygon(screen, "white", ((565, 650), (695, 650), (695, 660), (630, 675), (565, 660)), 3)

def draw_static():
    global strikezonedrawn
    global runners
    if strikezonedrawn == True:
        pygame.draw.rect(screen, "white", strikezone, 1)
    #BASES EMPTY
    if runners == 0.000:
        draw_bases("white", "white", "white")
    #RUNNER ON FIRST
    elif runners == 0.100:
        draw_bases("yellow","white","white")
    #RUNNER ON FIRST, SECOND
    elif runners == 0.110:
        draw_bases("yellow", "yellow", "white")
    #RUNNER ON FIRST, SECOND, THIRD (BASES LOADED)
    elif runners == 0.111:
        draw_bases("yellow", "yellow", "yellow")
    #RUNNER ON SECOND
    elif runners == 0.010:
        draw_bases("white","yellow","white")
    #RUNNERS ON FIRST, THIRD (RUNNERS AT THE CORNERS)
    elif runners == 0.101:
        draw_bases("yellow","white","yellow")
    #RUNNERS ON SECOND, THIRD
    elif runners == 0.011:
        draw_bases("white","yellow","yellow")
    #RUNNER ON THIRD
    elif runners == 0.001:
        draw_bases("white", "white", "yellow")
    homeplate()
    return

#Simple function to check menu_state and update the display accordingly.
def check_menu():
    global currentouts
    global menu_state
    global textfinished
    if currentouts == 3:
        for event in pygame.event.get():
            if event.type == pygame_gui.UI_TEXT_EFFECT_FINISHED:
                textfinished += 1
        if textfinished == 3:
            pygame.time.delay(500)
            menu_state = 3
    return

#righty pitcher position
c = (screen.get_width() / 2) - 20
d = (screen.get_height() / 3) + 50

#POSITION FOR BATTER
x = 370
y = 190

j = (screen.get_width() / 2) - 105
k = (screen.get_height() / 3) - 40

#Lefty pitcher position
a = (screen.get_width() / 2) - 20
b = (screen.get_height() / 3) + 120

def leftyone(a,b):
    screen.blit(lefty1, (a,b))
def leftytwo(a,b):
    screen.blit(lefty2, (a,b))
def leftythree(a,b):
    screen.blit(lefty3, (a,b))
def leftyfour(a,b):
    screen.blit(lefty4, (a,b))
def leftyfive(a,b):
    screen.blit(lefty5, (a,b))
def leftysix(a,b):
    screen.blit(lefty6, (a,b))
def leftyseven(a,b):
    screen.blit(lefty7, (a,b))
def leftyeight(a,b):
    screen.blit(lefty8, (a,b))
def leftynine(a,b):
    screen.blit(lefty9, (a,b))

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
def rightyeight(x,y):
    screen.blit(righty8,(x,y))
def rightynine(x,y):
    screen.blit(righty9,(x,y))

def troutone(x,y):
    screen.blit(trout1, (x,y))
def troutraiseleg(x,y):
    screen.blit(troutlegraise, (x,y))
def trouttwo(x,y):
    screen.blit(trout2, (x,y))
def troutthree(x,y):
    screen.blit(trout3, (x,y))
def troutfour(x,y):
    screen.blit(trout4, (x,y))
def troutfive(x,y):
    screen.blit(trout5, (x,y))
def troutsix(x,y):
    screen.blit(trout6, (x,y))
def troutseven(x,y):
    screen.blit(trout7, (x,y))

def troutfourhigh(x,y):
    screen.blit(trout4high, (x,y))
def troutfivehigh(x,y):
    screen.blit(trout5high, (x,y))
def troutsixhigh(x,y):
    screen.blit(trout6high, (x,y))

#Outcomes for a successful contact hit
def contact_hit_outcome():
    global runners
    global runs_scored
    global hit_type
    rand = random.uniform(0,10)
    if rand > 0 and rand <= 8:
        hit_type = 1
        update_runners_and_score(1)
        return "SINGLE"
    elif rand > 8 and rand <= 9:
        hit_type = 2
        update_runners_and_score(2)
        return "DOUBLE"
    elif rand > 9 and rand <= 9.3:
        hit_type = 3
        update_runners_and_score(3)
        return "TRIPLE"
    elif rand > 9.3 and rand <= 10:
        hit_type = 4
        update_runners_and_score(4)
        return "HOME RUN"

#Outcomes for a successful power hit
def power_hit_outcome():
    global runners
    global runs_scored
    global hit_type
    rand = random.uniform(0,10)
    if rand > 0 and rand <= 3:
        hit_type = 1
        update_runners_and_score(1)
        return "SINGLE"
    elif rand > 3 and rand <= 6.5:
        hit_type = 2
        update_runners_and_score(2)
        return "DOUBLE"
    elif rand > 6.5 and rand <= 7.5:
        hit_type = 3
        update_runners_and_score(3)
        return "TRIPLE"
    elif rand > 7.5 and rand <= 10:
        hit_type = 4
        update_runners_and_score(4)
        return "HOME RUN"

#LOGIC FOR UPDATING BASERUNNERS AFTER A HIT
def update_runners_and_score(hit_type):
    global runners
    global runs_scored
    global ishomerun
    ishomerun = ''

    if hit_type == 1:
        if runners == 0.000:
            runners = 0.100
        elif runners == 0.100:
            runners = 0.110
        elif runners == 0.010:
            runners = 0.101
        elif runners == 0.001:
            runners = 0.100
            runs_scored += 1
        elif runners == 0.110:
            runners = 0.111
        elif runners == 0.011:
            runners = 0.101
            runs_scored += 1
        elif runners == 0.111:
            runs_scored += 1
        elif runners == 0.101:
            runners = 0.110
            runs_scored += 1
    elif hit_type == 2:
        if runners == 0.000:
            runners = 0.010
        elif runners == 0.100:
            runners = 0.101
        elif runners == 0.010:
            runs_scored += 1
        elif runners == 0.001:
            runners = 0.010
            runs_scored += 1
        elif runners == 0.110:
            runners = 0.011
            runs_scored += 1
        elif runners == 0.011:
            runners = 0.010
            runs_scored += 2
        elif runners == 0.111:
            runners = 0.011
            runs_scored += 2
        elif runners == 0.101:
            runners = 0.011
            runs_scored += 1
    elif hit_type == 3:
        if runners == 0.000:
            runners = 0.001
        elif runners == 0.100 or runners == 0.010 or runners == 0.001:
            runners = 0.001
            runs_scored += 1
        elif runners == 0.110 or runners == 0.011 or runners == 0.101:
            runners = 0.001
            runs_scored += 2
        elif runners == 0.111:
            runners = 0.001
            runs_scored += 3
    elif hit_type == 4:
        if runners == 0.000:
            runs_scored += 1
            ishomerun = 'SOLO HOME RUN'
        elif runners == 0.100 or runners == 0.010 or runners == 0.001:
            runners = 0.000
            runs_scored += 2
            ishomerun = '2 RUN HOME RUN'
        elif runners == 0.110 or runners == 0.011 or runners == 0.101:
            runners = 0.000
            runs_scored += 3
            ishomerun = '3 RUN HOME RUN'
        elif runners == 0.111:
            runners = 0.000
            runs_scored += 4
            ishomerun = 'GRAND SLAM'
    return


#DEGROM PITCHING AI
def pitch_decision_maker():
    global currentballs
    global currentstrikes
    rando = random.uniform(1,10)
    # 0-0  OR  1 - 1  OR 3 - 2
    if ((currentballs == 0 and currentstrikes == 0) or
        (currentballs == 4) or
        (currentstrikes == 3) or
        (currentballs == 1 and currentstrikes == 1) or
        (currentballs == 3 and currentstrikes == 2)):
        if rando >= 1 and rando <= 3:
            lowfastball()
        elif rando > 3 and rando <= 5:
            highfastball()
        elif rando > 5 and rando <= 8:
            lowslider()
        else:
            lowchangeup()
    # 1 - 0 OR 2 - 1
    elif (currentballs == 1 and currentstrikes == 0) or (currentballs == 2 and currentstrikes == 1):
        if rando >= 1 and rando <= 4:
            lowfastball()
        elif rando > 4 and rando <= 5.5:
            highfastball()
        elif rando > 5.5 and rando <= 8.5:
            lowslider()
        else:
            lowchangeup()
    # 0 - 1  OR  2 - 2
    elif (currentballs == 0 and currentstrikes == 1) or (currentballs == 2 and currentstrikes == 2):
        if rando >= 1 and rando <= 2:
            lowfastball()
        elif rando > 2 and rando <= 5:
            highfastball()
        elif rando > 5 and rando <= 7:
            lowslider()
        else:
            lowchangeup()
    # 2 - 0  OR  3 - 1  OR  3 - 0
    elif (currentballs == 2 and currentstrikes == 0) or (currentballs == 3 and currentstrikes == 1) or (currentballs == 3 and currentstrikes == 0) :
        if rando >= 1 and rando <= 6:
            lowfastball()
        elif rando > 6 and rando <= 7:
            highfastball()
        elif rando > 7 and rando <= 9:
            lowslider()
        else:
            lowchangeup()
    # 0 - 2  OR  1 - 2
    elif (currentballs == 0 and currentstrikes == 2) or (currentballs == 1 and currentstrikes == 2):
        if rando >= 1 and rando <= 2:
            lowfastball()
        elif rando > 2 and rando <= 5:
            highfastball()
        elif rando > 5 and rando <= 7:
            lowslider()
        else:
            lowchangeup()
    return


#SALE PITCHING AI
def lefty_pitch_decision_maker():
    global currentballs
    global currentstrikes
    rando = random.uniform(1,10)
    # 0-0  OR  1 - 1  OR 3 - 2
    if ((currentballs == 0 and currentstrikes == 0) or
        (currentballs == 4) or
        (currentstrikes == 3) or
        (currentballs == 1 and currentstrikes == 1) or
        (currentballs == 3 and currentstrikes == 2)):
        if rando >= 1 and rando <=5:
            leftyfastball()
        elif rando > 5 and rando <=8:
            leftyslider()
        else:
            leftychangeup()
    # 1 - 0 OR 2 - 1
    elif (currentballs == 1 and currentstrikes == 0) or (currentballs == 2 and currentstrikes == 1):
        if rando >= 1 and rando <= 5.5:
            leftyfastball()
        elif rando > 5.5 and rando <= 8.5:
            leftyslider()
        else:
            leftychangeup()
    # 0 - 1  OR  2 - 2
    elif (currentballs == 0 and currentstrikes == 1) or (currentballs == 2 and currentstrikes == 2):
        if rando >= 1 and rando <= 5:
            leftyfastball()
        elif rando > 5 and rando <= 7:
            leftyslider()
        else:
            leftychangeup()
    # 2 - 0  OR  3 - 1  OR  3 - 0
    elif (currentballs == 2 and currentstrikes == 0) or (currentballs == 3 and currentstrikes == 1) or (currentballs == 3 and currentstrikes == 0) :
        if rando >= 1 and rando <= 7:
            leftyfastball()
        elif rando > 7 and rando <= 9:
            leftyslider()
        else:
            leftychangeup()
    # 0 - 2  OR  1 - 2
    elif (currentballs == 0 and currentstrikes == 2) or (currentballs == 1 and currentstrikes == 2):
        if rando >= 1 and rando <= 3:
            leftyfastball()
        elif rando > 3 and rando <= 7:
            leftyslider()
        else:
            leftychangeup()
    return

#DEGROM PITCH TYPES
def lowfastball():
    xoffset = random.uniform(0, 0)
    yoffset = random.uniform(0,0)
    global ball_pos
    ball_pos = pygame.Vector2((screen.get_width() / 2) - 24, (screen.get_height() / 3) + 84)
    simulate(True, ball_pos, 2 + xoffset, 0, 6 + yoffset, 0.1, 4, 390, 0.1, -0.15, 150, 'jacobdegrom')
    return
def highfastball():
    xoffset = random.uniform(-3, 3)
    yoffset = random.uniform(-2, 1)
    global ball_pos
    ball_pos = pygame.Vector2((screen.get_width() / 2) - 24, (screen.get_height() / 3) + 84)
    simulate(True, ball_pos, 0.3 + xoffset, 0, 3 + yoffset, 0, 4, 390, 0, -0.2, 150, 'jacobdegrom')
    return
def lowslider():
    xoffset = random.uniform(-1.5, 1)
    yoffset = random.uniform(0, 3)
    global ball_pos
    ball_pos = pygame.Vector2((screen.get_width() / 2) - 24, (screen.get_height() / 3) + 84)
    simulate(True, ball_pos, 0.3 + xoffset, 0.3, 1.5 + yoffset, 0.4, 4, 420, 0.3, 0.5, 250, 'jacobdegrom')
    return
def lowchangeup():
    xoffset = random.uniform(-2, 3)
    yoffset = random.uniform(-1, 1.5)
    global ball_pos
    ball_pos = pygame.Vector2((screen.get_width() / 2) - 24, (screen.get_height() / 3) + 84)
    simulate(True, ball_pos, 1 + xoffset, -0.1, 4 + yoffset, 0.2, 4, 450, 0.5, -0.2, 170, 'jacobdegrom')
    return

#SALE PITCH TYPES
def leftyfastball():
    xoffset = random.uniform(-0.25, 0.15)
    yoffset = random.uniform(0, 0)
    global ball_pos
    ball_pos = pygame.Vector2((screen.get_width() / 2) + 81, (screen.get_height() / 3) + 149 )
    simulate(True, ball_pos, -2, -0.15 + xoffset, 1, 0.15 + xoffset, 4, 390, 0, 0, 390, 'chrissale')
    return
def leftyslider():
    xoffset = random.uniform(-0.5, 3)
    yoffset = random.uniform(0,0)
    global ball_pos
    ball_pos = pygame.Vector2((screen.get_width() / 2) + 81, (screen.get_height() / 3) + 149 )
    simulate(True, ball_pos, -1 + xoffset, -0.3, 0.2 + yoffset, 0.35, 4, 490, 0.5, -0.65, 300, 'chrissale')
def leftychangeup():
    xoffset = random.uniform(-0.25, 0.1)
    yoffset = random.uniform(0, 0)
    global ball_pos
    ball_pos = pygame.Vector2((screen.get_width() / 2) + 81, (screen.get_height() / 3) + 149 )
    simulate(True, ball_pos, -1, xoffset, 0.5, 0.15, 4, 435, 0.20, 0, 200, 'chrissale')


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

#Low swing animation
def swing_start(timenow, swing_startime):
    if timenow <= swing_startime + 100:
        troutthree(x, y + 40)
    elif timenow > swing_startime + 100 and timenow <= swing_startime + 150:
        troutfour(x,y + 90)
    elif timenow > swing_startime + 150 and timenow <= swing_startime + 200:
        troutfive(x,y + 90)
    elif timenow > swing_startime + 200 and timenow <= swing_startime + 250:
        troutsix(x,y)
    elif timenow > swing_startime + 250:
        troutseven(x,y - 20)
    return

#Default stance if no swing
def leg_kick(currenttime, start_time):
    if currenttime <= start_time + 50:
        troutone(x,y)
    elif currenttime > start_time + 50 and currenttime <= start_time + 200:
        troutraiseleg(x,y)
    elif currenttime > start_time + 200 and currenttime <= start_time + 500:
        trouttwo(x,y)
    elif currenttime > start_time + 500:
        troutthree(x, y + 40)
    return

#High swing animation
def high_swing_start(timenow, swing_startime):
    if timenow <= swing_startime + 100:
        troutthree(x, y + 40)
    elif timenow > swing_startime + 100 and timenow <= swing_startime + 150:
        troutfourhigh(x,y + 80)
    elif timenow > swing_startime + 150 and timenow <= swing_startime + 200:
        troutfivehigh(x,y + 90)
    elif timenow > swing_startime + 200 and timenow <= swing_startime + 250:
        troutsixhigh(x - 60,y)
    elif timenow > swing_startime + 250:
        troutseven(x - 10,y - 20)
    return



#GAME LOOP FOR END/SUMMARY SCREEN
def draw_inning_summary():
    global running
    global currentstrikeouts
    global currentwalks
    global currentouts
    global pitchnumber
    global currentballs
    global currentstrikes
    global menu_state
    global runs_scored
    global runners
    global just_refreshed
    global hits
    global first_pitch_thrown
    global textfinished
    global ishomerun

    textfinished = 0
    done = False
    counter = 0
    textoffset = 0
    messages_finished = 0
    messages = ["INNING OVER",
                "HITS : {}".format(hits),
                "WALKS: {}".format(currentwalks),
                "STRIKEOUTS : {}".format(currentstrikeouts),
                "RUNS SCORED : {}".format(runs_scored)]
    active_message = 0
    message = messages[active_message]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        mousepos = pygame.mouse.get_pos()
        if pygame.Rect((540,530), (192,29)).collidepoint(mousepos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        full_message = 0
        screen.fill("black")
        if mainmenubutton.draw(screen):
            menu_state = 0
            first_pitch_thrown = False
            just_refreshed = 1
            currentballs = 0
            currentstrikes = 0
            pitchnumber = 0
            currentstrikeouts = 0
            currentwalks = 0
            currentouts = 0
            runs_scored = 0
            runners = 0
            hits = 0
            return
        clock.tick(60)/1000.0
        pygame.draw.rect(screen, 'white', [(440, 160), (400,300,)], 3)
        if counter < speed *len(message):
            counter += 1
        elif counter >= speed*len(message):
            done = True
        if (active_message < len(messages) - 1 ) and done:
            pygame.time.delay(500)
            active_message += 1
            done = False
            message = messages[active_message]
            textoffset += 50
            counter = 0
            messages_finished += 1
        if messages_finished > 0:
            offset = 0
            while full_message < messages_finished:
                oldmessage = font.render(messages[full_message], True, 'white')
                screen.blit(oldmessage, (450, 170 + offset))
                offset += 50
                full_message += 1
        snip = font.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (450, 170 + textoffset))
        pygame.display.flip()

    return

#GAME LOOP FOR MAIN MENU
def main_menu():
    global running
    global currentstrikeouts
    global currentwalks
    global currentouts
    global pitchnumber
    global currentballs
    global currentstrikes
    global menu_state
    global runs_scored
    global runners
    global just_refreshed
    global hits
    global first_pitch_thrown
    global textfinished

    done = False
    counter = 0
    textoffset = 0
    messages_finished = 0
    textfinished = 0

    messages = ["BASED BALL","A Baseball At-Bat Simulator"]

    active_message = 0
    message = messages[active_message]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        mousepos = pygame.mouse.get_pos()
        if pygame.Rect((500,500), (174,24)).collidepoint(mousepos) or pygame.Rect((500,600), (112, 24)).collidepoint(mousepos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        full_message = 0
        screen.fill("black")
        if faceoffsale.draw(screen):
            banner.hide()
            container.clear()
            menu_state = 1
            first_pitch_thrown = False
            just_refreshed = 1
            currentballs = 0
            currentstrikes = 0
            pitchnumber = 0
            currentstrikeouts = 0
            currentwalks = 0
            currentouts = 0
            runs_scored = 0
            runners = 0
            hits = 0
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return
        elif faceoffdegrom.draw(screen):
            banner.hide()
            container.clear()
            menu_state = 2
            first_pitch_thrown = False
            just_refreshed = 1
            currentballs = 0
            currentstrikes = 0
            pitchnumber = 0
            currentstrikeouts = 0
            currentwalks = 0
            currentouts = 0
            runs_scored = 0
            runners = 0
            hits = 0
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return
        clock.tick(60)/1000.0
        if counter < speed *len(message):
            counter += 1
        elif counter >= speed*len(message):
            done = True
        if (active_message < len(messages) - 1 ) and done:
            pygame.time.delay(500)
            active_message += 1
            done = False
            message = messages[active_message]
            textoffset += 100
            counter = 0
            messages_finished += 1
        if messages_finished > 0:
            offset = 0
            while full_message < messages_finished:
                oldmessage = bigfont.render(messages[full_message], True, 'white')
                screen.blit(oldmessage, (300, 170 + offset))
                offset += 100
                full_message += 1
        snip = bigfont.render(message[0:counter//speed], True, 'white')
        screen.blit(snip, (300, 170 + textoffset))
        pygame.display.flip()
    return


#GAME LOOP FOR AT-BAT
def simulate(yes, ball_pos, horizontalspeed,
            horizontalacceleration, verticalspeed, verticalacceleration,
            ballsize, traveltime, verticalbreak,
            horizontalbreak, breaktime, pitchername):

    pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR))
    global currentballs
    global pitchnumber
    global currentstrikes
    global string
    global currentouts
    global currentstrikeouts
    global currentwalks
    global runners
    global runs_scored
    global swing_started
    global hits
    global hit_type
    global first_pitch_thrown
    first_pitch_thrown = True
    swing_started = 0

    salepitch.hide()
    strikezonetoggle.hide()
    degrompitch.hide()
    backtomainmenu.hide()
    banner.hide()

    soundplayed = 0
    on_time = 0
    made_contact = 0
    contact_time = 0
    swing_type = 0
    pitch_results_done = False

    starttime = pygame.time.get_ticks()
    current_time = starttime
    while yes:
        time_delta = clock.tick(60)/1000.0
        current_time += (time_delta*1000)
        #Pitcher Windup
        if current_time <= starttime + 1100:
            screen.fill("black")
            if pitchername == 'chrissale':
                if current_time <= starttime + 300:
                    leftyone(a,b)
                elif current_time > starttime + 300 and current_time <= starttime + 500:
                    leftytwo(a,b)
                elif current_time > starttime + 500 and current_time <= starttime + 700:
                    leftythree(a,b)
                elif current_time > starttime + 700 and current_time <= starttime + 900:
                    leftyfour(a,b)
                elif current_time > starttime + 900 and current_time <= starttime + 1000:
                    leftyfive(a,b + 10)
                elif current_time > starttime + 1000 and current_time <= starttime + 1100:
                    leftysix(a + 10,b + 25)
            elif pitchername == 'jacobdegrom':
                if current_time <= starttime + 300:
                    rightyone(c,d)
                elif current_time > starttime + 300 and current_time <= starttime + 500:
                    rightytwo(c - 20,d)
                elif current_time > starttime + 500 and current_time <= starttime + 700:
                    rightythree(c - 24,d)
                elif current_time > starttime + 700 and current_time <= starttime + 900:
                    rightyfour(c - 50,d + 10)
                elif current_time > starttime + 900 and current_time <= starttime + 1000:
                    rightyfive(c - 59,d + 20)
                elif current_time > starttime + 1000 and current_time <= starttime + 1100:
                    rightysix(c,d + 30)

            leg_kick(current_time, starttime + 650)
            draw_static()
            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

        #From time ball leaves the hand until ball finishes traveling
        if (current_time > starttime + 1100 and current_time < starttime + traveltime + 1150 and (on_time == 0 or (on_time > 0 and made_contact == 1))) or (on_time > 0 and current_time <= contact_time and made_contact == 0):
            screen.fill("black")
            if current_time > starttime + 1100 and current_time <= starttime + 1150:
                if pitchername == 'chrissale':
                    leftyseven(a + 8,b + 22)
                elif pitchername == 'jacobdegrom':
                    rightyseven(c - 10,d + 30)
                pygame.draw.circle(screen, "white", ball_pos, ballsize)
                ball_pos.y += verticalspeed
                ball_pos.x += horizontalspeed
                horizontalspeed += horizontalacceleration
                verticalspeed += verticalacceleration
                ballsize = ballsize * 1.030
            elif current_time > starttime + 1150 and current_time <= starttime + breaktime + 1150 and on_time == 0:
                if current_time > starttime + 1150 and current_time <= starttime + 1200:
                    if pitchername == 'chrissale':
                        leftyeight(a - 11,b + 22)
                    elif pitchername == 'jacobdegrom':
                        rightyeight(c - 15, d + 30)
                else:
                    if pitchername == 'chrissale':
                        leftynine(a + 16, b + 22)
                    elif pitchername == 'jacobdegrom':
                        rightynine(c - 15, d + 30)
                pygame.draw.circle(screen, "white", ball_pos, ballsize)
                ball_pos.y += verticalspeed
                ball_pos.x += horizontalspeed
                horizontalspeed += horizontalacceleration
                verticalspeed += verticalacceleration
                ballsize = ballsize * 1.030
            elif (current_time > starttime + breaktime + 1150 and current_time <= starttime + traveltime + 1150 and (on_time == 0 or (on_time > 0 and made_contact == 1))) or (on_time > 0 and current_time <= contact_time and made_contact == 0):
                if pitchername == 'chrissale':
                    leftynine(a + 16, b + 22)
                elif pitchername == 'jacobdegrom':
                    rightynine(c - 15, d + 30)
                pygame.draw.circle(screen, "white", ball_pos, ballsize)
                ball_pos.y += verticalspeed
                ball_pos.x += horizontalspeed
                horizontalspeed += horizontalbreak
                verticalspeed += verticalbreak
                ballsize = ballsize * 1.030

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #CONTACT SWING
                    if event.key == pygame.K_w and swing_started == 0:
                        swing_type = 1
                        mousepos = pygame.mouse.get_pos()
                        #LOW SWING
                        if mousepos[1] > 500:
                            swing_starttime = pygame.time.get_ticks()
                            swing_started = 1
                            if abs((swing_starttime + 150) - (starttime + traveltime + 1150)) > 40 and abs((swing_starttime + 150) - (starttime + traveltime + 1150)) < 70:
                                on_time = 1
                                contact_time = swing_starttime + 150
                            elif abs((swing_starttime + 150) - (starttime + traveltime + 1150)) <= 40:
                                on_time = 2
                                contact_time = swing_starttime + 150
                        #HIGH SWING
                        elif mousepos[1] < 500:
                            swing_starttime = pygame.time.get_ticks()
                            swing_started = 2
                            if abs((swing_starttime + 150) - (starttime + traveltime + 1150)) > 40 and abs((swing_starttime + 150) - (starttime + traveltime + 1150)) < 70:
                                on_time = 1
                                contact_time = swing_starttime + 150
                            elif abs((swing_starttime + 150) - (starttime + traveltime + 1150)) <= 40:
                                on_time = 2
                                contact_time = swing_starttime + 150
                    #POWER SWING
                    elif event.key == pygame.K_e and swing_started == 0:
                        swing_type = 2
                        mousepos = pygame.mouse.get_pos()
                        #LOW SWING
                        if mousepos[1] > 500:
                            swing_starttime = pygame.time.get_ticks()
                            swing_started = 1
                            if abs((swing_starttime + 150) - (starttime + traveltime + 1150)) > 25 and abs((swing_starttime + 150) - (starttime + traveltime + 1150)) < 50:
                                on_time = 1
                                contact_time = swing_starttime + 150
                            elif abs((swing_starttime + 150) - (starttime + traveltime + 1150)) <= 25:
                                on_time = 2
                                contact_time = swing_starttime + 150
                        #HIGH SWING
                        elif mousepos[1] < 500:
                            swing_starttime = pygame.time.get_ticks()
                            swing_started = 2
                            if abs((swing_starttime + 150) - (starttime + traveltime + 1150)) > 25 and abs((swing_starttime + 150) - (starttime + traveltime + 1150)) < 50:
                                on_time = 1
                                contact_time = swing_starttime + 150
                            elif abs((swing_starttime + 150) - (starttime + traveltime + 1150)) <= 25:
                                on_time = 2
                                contact_time = swing_starttime + 150

            if swing_started > 0:
                timenow = current_time
                if swing_started == 1:
                    swing_start(timenow, swing_starttime)
                else:
                    high_swing_start(timenow, swing_starttime)
            elif swing_started == 0:
                leg_kick(current_time, starttime + 650)
            draw_static()
            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

            if (current_time > (starttime + traveltime + 1050) and soundplayed == 0 and on_time == 0) or (current_time > contact_time and soundplayed == 0 and (on_time > 0 and made_contact == 1)):
                popsfx.play()
                soundplayed += 1

        #FOUL BALL TIMING
        elif on_time == 1 and current_time > contact_time and current_time <= starttime + traveltime + 1800 and pitch_results_done == False and made_contact == 0:
            if pitchername == 'chrissale':
                leftynine(a + 16, b + 22)
            elif pitchername == 'jacobdegrom':
                rightynine(c - 15, d + 30)
            #TIMING ON BUT SWING PATH OFF (SWING OVER OR UNDER BALL)
            if (ball_pos.x < 554 or ball_pos.x > 706) or (ball_pos.y < 385 or ball_pos.y > 480) and swing_started == 2:
                made_contact = 1
            elif (ball_pos.x < 554 or ball_pos.x > 706) or (ball_pos.y < 485 or ball_pos.y > 576) and swing_started == 1:
                made_contact = 1
            #TIMING ON AND PATH ON - FOUL BALL
            else:
                made_contact = 2
                pitch_results_done = True
                pitchnumber += 1
                if currentstrikes == 2:
                    container.clear()
                    string = "<font size=5>PITCH {}: FOUL<br>COUNT IS {} - {}</font>".format(pitchnumber, currentballs, currentstrikes)
                    textbox = pitchresult(string)
                    textbox.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
                    result = "<font size=5>CURRENT OUTS : {}<br>STRIKEOUTS : {}<br>WALKS : {}<br>HITS : {}<br>RUNS SCORED: {}</font>".format(currentouts, currentstrikeouts, currentwalks, hits, runs_scored)
                    scoreboard = drawscoreboard(result)
                    containerupdate(textbox,scoreboard)
                else:
                    currentstrikes += 1
                    container.clear()
                    string = "<font size=5>PITCH {}: FOUL<br>COUNT IS {} - {}</font>".format(pitchnumber, currentballs, currentstrikes)
                    textbox = pitchresult(string)
                    textbox.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
                    result = "<font size=5>CURRENT OUTS : {}<br>STRIKEOUTS : {}<br>WALKS : {}<br>HITS : {}<br>RUNS SCORED: {}</font>".format(currentouts, currentstrikeouts, currentwalks, hits, runs_scored)
                    scoreboard = drawscoreboard(result)
                    containerupdate(textbox,scoreboard)

        #PERFECT TIMING
        elif on_time == 2 and current_time > contact_time and current_time <= starttime + traveltime + 1800 and pitch_results_done == False and made_contact == 0:
            if pitchername == 'chrissale':
                leftynine(a + 16, b + 22)
            elif pitchername == 'jacobdegrom':
                rightynine(c - 15, d + 30)
            #PERFECT TIMING BUT SWING PATH OFF
            if (ball_pos.x < 554 or ball_pos.x > 706) or (ball_pos.y < 385 or ball_pos.y > 480) and swing_started == 2:
                made_contact = 1
            elif (ball_pos.x < 554 or ball_pos.x > 706) or (ball_pos.y < 470 or ball_pos.y > 576) and swing_started == 1:
                made_contact = 1
            #PERFECT TIMING AND SWING PATH ON - SUCCESSFUL HIT
            else:
                container.clear()
                made_contact = 2
                pitch_results_done = True
                pitchnumber += 1
                if swing_type == 1:
                    hit_string = contact_hit_outcome()
                elif swing_type == 2:
                    hit_string = power_hit_outcome()
                if ishomerun != '':
                    banner.set_text("{}".format(ishomerun))
                else:
                    banner.set_text("{}".format(hit_string))
                banner.show()
                banner.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR,{'time_per_letter': 0.1})
                string = "<font size=5>PITCH {} :<br>HIT - {}</font>".format(pitchnumber, hit_string)
                textbox = pitchresult(string)
                hits += 1
                textbox.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
                result = "<font size=5>CURRENT OUTS : {}<br>STRIKEOUTS : {}<br>WALKS : {}<br>HITS : {}<br>RUNS SCORED: {}</font>".format(currentouts, currentstrikeouts, currentwalks, hits, runs_scored)
                scoreboard = drawscoreboard(result)
                scoreboard.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, {'time_per_letter': 0.0075})
                containerupdate(textbox, scoreboard)
                pitchnumber = 0
                currentstrikes = 0
                currentballs = 0

        #Follow through - play rest of the swing animation
        elif on_time > 0 and current_time > contact_time and current_time <= starttime + traveltime + 1800 and pitch_results_done == True and made_contact == 2:
            screen.fill("black")
            if pitchername == 'chrissale':
                leftynine(a + 16, b + 22)
            elif pitchername == 'jacobdegrom':
                rightynine(c - 15, d + 30)
            if swing_started > 0:
                timenow = current_time
                if swing_started == 1:
                    swing_start(timenow, swing_starttime)
                else:
                    high_swing_start(timenow, swing_starttime)
            pygame.draw.circle(screen, "white", ball_pos, fourseamballsize, 2)
            draw_static()
            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()
            #Play sounds
            if soundplayed == 0 and on_time == 1:
                foulball.play()
                soundplayed += 1
            elif soundplayed == 0 and on_time == 2:
                if hit_type == 1:
                    single.play()
                elif hit_type == 2:
                    double.play()
                elif hit_type == 3:
                    triple.play()
                elif hit_type == 4:
                    homer.play()
                soundplayed += 1

        #UPDATE RESULTS IF NO CONTACT MADE AT ALL - SWINGING STRIKE OR CALLED STRIKE OR BALL
        elif (current_time > starttime + traveltime + 1150 and pitch_results_done == False and (on_time == 0 or (on_time > 0 and made_contact == 1))):
            if pitchername == 'chrissale':
                leftynine(a + 16, b + 22)
            elif pitchername == 'jacobdegrom':
                rightynine(c - 15, d + 30)
            pitch_results_done = True
            #BALL OUTSIDE THE ZONE AND NOT SWUNG AT - BALL
            if (not collision(ball_pos.x, ball_pos.y, 11, 630, 482.5, 130, 165)) and swing_started == 0:
                ballcall.play()
                currentballs += 1
                pitchnumber += 1
                #WALK OCCURS
                if currentballs == 4:
                    container.clear()
                    string = "<font size=5>PITCH {} : BALL<br>COUNT IS {} - {}<br><b>WALK</b></font>".format(pitchnumber, currentballs, currentstrikes)
                    textbox = pitchresult(string)
                    textbox.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
                    currentwalks += 1
                    pitchnumber = 0
                    currentstrikes = 0
                    currentballs = 0
                    if runners == 0.000:
                        runners = 0.100
                    elif runners == 0.100 or runners == 0.010:
                        runners = 0.110
                    elif runners == 0.001:
                        runners = 0.101
                    elif runners == 0.110 or runners == 0.011 or runners == 0.101:
                        runners = 0.111
                    elif runners == 0.111:
                        runs_scored += 1
                    result = "<font size=5>CURRENT OUTS : {}<br>STRIKEOUTS : {}<br>WALKS : {}<br>HITS : {}<br>RUNS SCORED: {}</font>".format(currentouts, currentstrikeouts, currentwalks, hits, runs_scored)
                    scoreboard = drawscoreboard(result)
                    scoreboard.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, {'time_per_letter': 0.0075})
                    containerupdate(textbox,scoreboard)
                    banner.set_text("WALK")
                    banner.show()
                    banner.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR,{'time_per_letter': 0.1})
                else:
                    #Normal Ball
                    container.clear()
                    string = "<font size=5>PITCH {} : BALL<br>COUNT IS {} - {}</font>".format(pitchnumber, currentballs, currentstrikes)
                    textbox = pitchresult(string)
                    textbox.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
                    result = "<font size=5>CURRENT OUTS : {}<br>STRIKEOUTS : {}<br>WALKS : {}<br>HITS : {}<br>RUNS SCORED: {}</font>".format(currentouts, currentstrikeouts, currentwalks, hits, runs_scored)
                    scoreboard = drawscoreboard(result)
                    containerupdate(textbox,scoreboard)
            #STRIKE (CALLED OR SWINGING STRIKE)
            else:
                pitchnumber += 1
                currentstrikes += 1
                if swing_started == 0 and currentstrikes == 3:
                    called_strike_3.play()
                elif swing_started == 0 and currentstrikes != 3:
                    strikecall.play()
                #STRIKEOUT OCCURS
                if currentstrikes == 3:
                    container.clear()
                    string = "<font size=5>PITCH {} : STRIKE<br>COUNT IS {} - {}<br><b>STRIKEOUT</b></font>".format(pitchnumber, currentballs, currentstrikes)
                    textbox = pitchresult(string)
                    textbox.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
                    currentstrikeouts += 1
                    currentouts +=1
                    result = "<font size=5>CURRENT OUTS : {}<br>STRIKEOUTS : {}<br>WALKS : {}<br>HITS : {}<br>RUNS SCORED: {}</font>".format(currentouts, currentstrikeouts, currentwalks, hits, runs_scored)
                    scoreboard = drawscoreboard(result)
                    scoreboard.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, {'time_per_letter': 0.0075})
                    banner.set_text("STRIKEOUT")
                    banner.show()
                    banner.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR,{'time_per_letter': 0.1})
                    containerupdate(textbox,scoreboard)
                    pitchnumber = 0
                    currentstrikes = 0
                    currentballs = 0
                else:
                    #Normal Strike
                    container.clear()
                    string = "<font size=5>PITCH {} : STRIKE<br>COUNT IS {} - {}</font>".format(pitchnumber, currentballs, currentstrikes)
                    textbox = pitchresult(string)
                    textbox.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
                    result = "<font size=5>CURRENT OUTS : {}<br>STRIKEOUTS : {}<br>WALKS : {}<br>HITS : {}<br>RUNS SCORED: {}</font>".format(currentouts, currentstrikeouts, currentwalks, hits, runs_scored)
                    scoreboard = drawscoreboard(result)
                    containerupdate(textbox,scoreboard)

        #FOLLOW THROUGH IF SWUNG AND MISSED and ball has already reached the plate (For late swings)
        elif current_time > starttime + traveltime + 1150 and pitch_results_done == True and current_time <= starttime + traveltime + 1800 and (on_time == 0 or (on_time > 0 and made_contact == 1)):
            screen.fill("black")
            if pitchername == 'chrissale':
                leftynine(a + 16, b + 22)
            elif pitchername == 'jacobdegrom':
                rightynine(c - 15, d + 30)
            if (current_time > contact_time and soundplayed == 0 and (on_time > 0 and made_contact == 1)):
                popsfx.play()
                soundplayed += 1
            if swing_started > 0:
                timenow = current_time
                if swing_started == 1:
                    swing_start(timenow, swing_starttime)
                else:
                    high_swing_start(timenow, swing_starttime)
            elif swing_started == 0:
                leg_kick(current_time, starttime + 650)
            pygame.draw.circle(screen, "white", ball_pos, fourseamballsize, 2)
            draw_static()
            manager.update(time_delta)
            manager.draw_ui(screen)
            pygame.display.flip()

        #END LOOP (END OF PITCH)
        elif current_time > starttime + traveltime + 1800:
            yes = False
            salepitch.show()
            strikezonetoggle.show()
            backtomainmenu.show()

    pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
    return







#Main Game Loop
while running:

    time_delta = clock.tick(60)/1000.0
    check_menu()

    if menu_state == 0:
        main_menu()
    elif menu_state == 1:
        degrompitch.hide()
        salepitch.show()
        backtomainmenu.show()
        strikezonetoggle.show()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == strikezonetoggle:
                    if strikezonedrawn == True:
                        strikezonedrawn = False
                    elif strikezonedrawn == False:
                        strikezonedrawn = True
                elif event.ui_element == salepitch:
                    lefty_pitch_decision_maker()
                elif event.ui_element == backtomainmenu:
                    menu_state = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    lefty_pitch_decision_maker()
            manager.process_events(event)
        manager.update(time_delta)
        screen.fill("black")
        if just_refreshed == 1:
            result = "<font size=5>CURRENT OUTS : {}<br>STRIKEOUTS : {}<br>WALKS : {}<br>HITS : {}<br>RUNS SCORED: {}</font>".format(currentouts, currentstrikeouts, currentwalks, hits, runs_scored)
            scoreboard = drawscoreboard(result)
            scoreboard.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, {'time_per_letter': 0.0075})
            string = "<font size=5><br>COUNT IS {} - {}</font>".format(pitchnumber, currentballs, currentstrikes)
            textbox = pitchresult(string)
            textbox.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, {'time_per_letter': 0.0075})
            containerupdate(textbox, scoreboard)
            just_refreshed = 0
        leftyone(a,b)
        draw_static()
        troutone(x,y)
        if first_pitch_thrown:
            pygame.draw.circle(screen, "white", ball_pos, fourseamballsize, 2)
        manager.draw_ui(screen)
        pygame.display.flip()

    elif menu_state == 2:
        salepitch.hide()
        degrompitch.show()
        backtomainmenu.show()
        strikezonetoggle.show()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == strikezonetoggle:
                    if strikezonedrawn == True:
                        strikezonedrawn = False
                    elif strikezonedrawn == False:
                        strikezonedrawn = True
                elif event.ui_element == degrompitch:
                    pitch_decision_maker()
                elif event.ui_element == backtomainmenu:
                    menu_state = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pitch_decision_maker()
            manager.process_events(event)
        manager.update(time_delta)
        screen.fill("black")
        if just_refreshed == 1:
            result = "<font size=5>CURRENT OUTS : {}<br>STRIKEOUTS : {}<br>WALKS : {}<br>HITS : {}<br>RUNS SCORED: {}</font>".format(currentouts, currentstrikeouts, currentwalks, hits, runs_scored)
            scoreboard = drawscoreboard(result)
            scoreboard.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, {'time_per_letter': 0.0075})
            string = "<font size=5><br>COUNT IS {} - {}</font>".format(pitchnumber, currentballs, currentstrikes)
            textbox = pitchresult(string)
            textbox.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR, {'time_per_letter': 0.0075})
            containerupdate(textbox, scoreboard)
            just_refreshed = 0
        manager.draw_ui(screen)
        rightyone(c,d)
        draw_static()
        troutone(x,y)
        if first_pitch_thrown:
            pygame.draw.circle(screen, "white", ball_pos, fourseamballsize, 2)
        pygame.display.flip()

    elif menu_state == 3:
        draw_inning_summary()

pygame.quit()