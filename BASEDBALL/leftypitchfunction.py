 
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
        if rando >= 1 and rando <= 6:
            highlow = random.uniform(1,10)
            if highlow >= 1 and highlow <= 6:
                leftyfastball()
            else:
                leftyhighfastball()
        elif rando > 6 and rando <= 8.5:
            leftyslider()
        else:
            leftychangeup()
    # 1 - 0 OR 2 - 1
    elif (currentballs == 1 and currentstrikes == 0) or (currentballs == 2 and currentstrikes == 1):
        if rando >= 1 and rando <= 6.5:
            highlow = random.uniform(1,10)
            if highlow >= 1 and highlow <= 5:
                leftyfastball()
            else:
                leftyhighfastball()
        elif rando > 6.5 and rando <= 9:
            leftyslider()
        else:
            leftychangeup()
    # 0 - 1  OR  2 - 2
    elif (currentballs == 0 and currentstrikes == 1) or (currentballs == 2 and currentstrikes == 2):
        if rando >= 1 and rando <= 5:
            highlow = random.uniform(1,10)
            if highlow >= 1 and highlow <= 4:
                leftyfastball()
            else:
                leftyhighfastball()
        elif rando > 5 and rando <= 7:
            leftyslider()
        else:
            leftychangeup()
    # 2 - 0  OR  3 - 1  OR  3 - 0
    elif (currentballs == 2 and currentstrikes == 0) or (currentballs == 3 and currentstrikes == 1) or (currentballs == 3 and currentstrikes == 0) :
        if rando >= 1 and rando <= 7:
            highlow = random.uniform(1,10)
            if highlow >= 1 and highlow <= 8:
                leftyfastball()
            else:
                leftyhighfastball()
        elif rando > 7 and rando <= 9:
            leftyslider()
        else:
            leftychangeup()
    # 0 - 2  OR  1 - 2
    elif (currentballs == 0 and currentstrikes == 2) or (currentballs == 1 and currentstrikes == 2):
        if rando >= 1 and rando <= 3:
            highlow = random.uniform(1,10)
            if highlow >= 1 and highlow <= 3:
                leftyfastball()
            else:
                leftyhighfastball()
        elif rando > 3 and rando <= 7:
            leftyslider()
        else:
            leftychangeup()
    return