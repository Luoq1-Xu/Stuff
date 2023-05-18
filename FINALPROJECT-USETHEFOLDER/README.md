# BASED BALL : A baseball at-bat simulator
## Video Demo:  <URL HERE>
#### Description:
Based Ball is a simple simulator that allows you to face off against two pitchers: Chris Sale (Left hand pitcher) and Jacob Degrom (Right Hand pitcher).
The art of pitching has long fascinated me, and so I wanted to create a simple simulator that allows people to experience what it is like to step into the box and face
some good pitching. I had a few preliminary thoughts:

- I will need many different functions for various purposes.
- How to simulate the flight path of the ball visually?
- How to check for the bat path, both timing and location?
- How will the Graphical User Interface be set up?
- and many many more....

## Meet them all
The game consists of a few main assets

* Main Finalproject.py file

* Sounds

* Graphics (Images)

* theme.json file

* button.py supplementary button class file


### Finalproject.py(Main python file)
As this is the first python program I have written in full, please pardon the relatively poor standard of the code. With that being said, the main file contains a large selection of functions, and I will explain them in further detail below.

I utilised pygame_gui for most of the Graphical User Interface in the game, as I intended the GUI to be very simple and straightforward. Pygame_gui seemed to be relatively easy to implement, while retaining the ability to customise appearance through a theme file.

The first section of the code initialises and sets up the game. This includes the pygame setup of the screen, clock and mixer(for sound). Pygame_gui setup is also done here, such as initialising the manager and setting up the buttons and textboxes. Loading in of the graphic and audio resources is also done here.
The global game variables are also initalised here, like currentouts, currentstrikes, and others. These variables will be constantly changing with multiple functions making use of them.

draw_bases, homeplate and draw_static are pretty self-explanatory - they manage the display of the static elements that do not move during or in between at-bats. draw_bases is where the actual drawing of the base graphic occurs, while draw_static manages the actual logic that determines the correct graphic to be displayed depending on the value of "runners". Admittedly, the method used is very crude but it works (for now). The value of runners is stored as a three decimal place float, and the runners on base are determined by whether each decimal place is 1 or 0. For example, runner on first only is denoted by "0.100", while bases loaded(runners on each of the three bases) is denoted by "0.111". The value of runners is then changed by other functions and then draw_static updates the bases graphic accordingly.

check_menu simply updates the menu_state if 3 outs have been made and the inning is over.

Next, I put all the screen.blit instances for every image into conviniently named functions to make them easier to call instead of copy pasting screen.blit everytime.

contact_hit_outcome and power_hit_outcome: These functions serve to randomly determine the result of a hit. These functions will be called after it is determined that the player successfully gets a hit (which in turn is determined by having perfect timing and location of swing). Choosing to swing with a contact swing (pressing the "w" key) and getting a successful hit will call the contact_hit_outcome function. A contact hit will mean a much higher chance of getting a single (so called "worst" possible outcome) and much lower chance of the other outcomes happening. Conversely, getting a hit with the Power Swing(pressing the "e" key) calls the power_hit_outcome, which gives a higher chance of the other outcomes occuring. This difference is balanced by making the power swing less forgiving than the contact swing, that means your timing has to be more accurate and on time to get a hit using a power swing as compared to using the contact swing. The four possible outcomes in each of these two functions are "Single", "Double", "Triple" and "Home Run". These two functions will then call another function, update_runners_and_score, to do the actual updating of the runners and score ("runs").

update_runners_and_score serves to do the actual updating of "runners" and "runs" depending on the input. The input is an integer that represents the result to be updated, 1 represents single, 2 represents double, 3 represents triple and 4 represents home run. To keep things simple, all runners move up by the number of bases represented by the outcome. The function manually checks what is the current value of "runners", and then updates it according to the input, updating the "runs" variable also if any runs score.

For example, a single is represented by 1, all runners will move up by 1 base. If there is currently a runner on first base (runners = 0.100), a single would result in runners on first and second (runners = 0.110) -> The runner on first moves to second, and the batter (guy that swung the bat) moves to first.

Another example, if there is currently a runner on second (runners = 0.010), and the batter hits a double (2), the result will be a runner on second (0.010) and 1 run scores (runs += 1).The original runner on second moves 2 bases (2nd -> 3rd -> home) and scores (runs += 1) and the batter moves to second. (home -> 1st -> 2nd).

Next up are the pitching decision trees for each of the two pitchers. Both utilise the same structure, albeit with slight differences in probabilities and pitch types chosen. Chris Sale (Left Hander) has 3 pitch types -> Fastball, Slider, Changeup. The pitch decision tree will randomly determine a pitch to choose depending on the current count (the current number of balls and strikes). Degrom (Right Hander) has the same 3 pitch types also, but degrom is slightly different because I implemented a "High fastball" pitch type and a "Low Fastball" pitch type. That means to say that a "High Fastball" is basically guaranteed to arrive high up in the zone and I think you can guess what "Low Fastball" does. The decision tree works by altering the probabilities of each pitch type being thrown depending on the count. This is supplemented by the fact that each pitch type has different behaviours. For example, with Chris Sale, his fastball has a high probability of arriving in the zone (high likelihood of being a "strike") while his slider has a high probability of arriving outside the zone (high chance to be a ball). The pitching decision tree plays with this characteristic, to try to attain the most favourable outcome based on the relative risk to reward ratio. This is not completely realistic, because there is so many more factors to consider in real baseball, but sometimes you will see a similar decision making sequence in real life as well. While the probabilities are skewed in certain situations, the random element of it helps to maintain a little bit of realism, as just like real life, you have to be ready for any outcome. Even if you know something is more likely to happen, you still have to prepare for the possibility of something else happening.

Taking a closer look into the pitch decision tree for Chris Sale, we see some patterns.
When the count is 0 balls and 0 strikes or 3 balls and 2 strikes, the probabilities are relatively evenly balanced, as the pitch type doesn't really have much of an impact in this situation.

However, when the count is 0 balls and 2 strikes, the pitcher has a significant advantage here. We can see that the probability of throwing a slider is much higher here. It makes more sense to throw a slider (that likely arrives out of the zone) here because if the batter swings (all likely will miss), then they will strikeout with 3 strikes. Otherwise, if they do not swing, the count only goes to 1ball and 2 strikes.

If the count is 3 balls and 0 strikes, the batter has the significant advantage here, as one more ball means they walk and get a free base. Therefore, we see that the decision maker has a much higher probability of throwing a fastball (High chance of arriving in the zone), to get a strike and avoiding walking the batter on 4 balls.

The different pitch types for each pitcher are represented by the next group of functions. These are the functions that are called when pitch_decision_maker selects a pitch type to use. These functions work by calling the main function to simulate the at-bat, "simulate", and passing in some parameters that will determine how the pitch moves. These variables include: traveltime, breaktime, verticalspeed, horizontalspeed, verticalacceleration, horizontalacceleration, verticalbreak, horizontalbreak. There are also a few other less important parameters, such as pitchername to determine which pitcher is pitching, and ball_pos, used to determine the release point of the ball (which is affected by which pitcher is pitching). These parameters will be covered more in depth below, when we reach the "simulate" function. For these pitch type functions, an additional element of unpredictability is added by having "xoffset" and "yoffset" determined randomly in a range. These offsets will affect the pitch by changing it's initial trajectory. This can cause a fastball to arrive outside the zone, and can cause a slider to arrive in the zone. They also alter the way the pitch appears at the start, which is significant because the player relies on seeing and judging the way the ball moves at the start to decide whether to swing.

There is also a simple function called collision that checks whether a ball is touching a rectangle. This is used to check whether the ball touches the strikezone once it arrives at home plate, strike if it is touching, and ball otherwise. All credit goes to e-james, I used his answer on stackoverflow here:
https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection

**swing_start, high_swing_start and leg_kick**: These functions will play the respective animations, switching the image to be displayed according to the time that has elapsed since the function was first called. swing_start plays the low swing animation, high_swing_start plays the high swing animation, and leg_kick plays the default animation if the player does not swing.


`draw_inning_summary` and `main_menu`: these are responsible for the summary screen and main menu. The text typing effect was implemented with the help of LeMaster Tech's great video: https://www.youtube.com/watch?v=DhK5P2bWznA. The buttons were also put in with help from Coding with Russ's nice tutorial: https://www.youtube.com/watch?v=G8MYGDf_9ho.

`simulate` : This is the real meat of the matter of the game. It is responsible for the entire process of simulating the at-bat, including the pitcher's pitching motion, the batter's swing, the appearance of the ball as it moves towards home plate, and the management of all outcomes. A lot of variables here, so I will go through some of the more important ones.

First, the important input parameters:

traveltime, breaktime: traveltime determines how long the ball takes from leaving the pitchers hand to arriving at home plate. Fastballs take shorter time to reach the plate than sliders or changeups. breaktime determines when the ball starts to "break", which means when it starts to appear to move significantly. This is more important for pitches like sliders and changeups, which appear to "break" significantly, moving significantly in a different direction that it first appeared to move when just released out of the pitcher's hand.

verticalspeed, horizontalspeed: These determine the ball's current velocity. The ball's initial velocity will be affected by the offset( mentioned in the pitch type functions above). The ball's velocity will also be constantly changing, first by verticalacceleration and horizontal acceleration, then later by verticalbreak and horizontalbreak.

verticalacceleration, horizontalaccceleration, verticalbreak, horizontalbreak: These will update the ball's current verticalspeed and horizontalspeed once per cycle. verticalacceleration and horizontalacceleration apply to the ball initially, then verticalbreak and horizontalbreak take over after breaktime is reached. This is to create the appearance that the ball seems to move 









### Sounds
A few sounds were implemented: The glove pop sound (for when the ball hits the catcher's mitt aka the ball has finished travelling the full distance), the sounds when the bat makes contact with the ball, and the umpire call sounds.

The glove pop sound plays whenever the ball ends up in the catcher's mitt - basically any outcome other than the batter making contact with the ball.

The bat contact sounds include - Single, Double, Triple, Homerun. Each corresponds to the equivalent outcome and will play accordingly. I got these sounds from the videogame MLB the Show. Very crisp and nice sounds to give maximum satisfaction! There is also the foul sound for when a player fouls off a ball.

The umpire call sounds will play once the ball arrives in the zone without a swing. If you do not swing and the ball clips the zone, the called strike sound will play. If the above happens and it is the third strike, the third strike sound plays. On the flip side, if you do not swing and the ball lands outside the zone, the ball call sound plays.

### Graphics
To keep simple, I used coloured images for the hitter and the batter, while everything else is basically rendered in black and white.

The strikezone and home plate are rendered simply using the built in pygame draw function. The strikezone is a simple Rect and the homeplate is a polygon. The strikezone is also toggleable, for the player's preference. Generally, having the strikezone on makes it easier to determine whether a ball will be a ball or a strike.

For the ball, I used the pygame draw function to draw a circle that increases in size as time passes and it "approaches" the plate to give the illusion
that it is getting closer. I thought about bliting an actual image of the baseball onto the screen but found it very difficult because I would need to have
multiple frames to depict the spinning motion of the ball. Further complicating things is the fact that different pitch types have the ball spin differently,
so I would need separate sets of frames for different pitch types. I find that the simple solid circle would be sufficient to allow the player to appreciate the essence of a baseball at-bat, without over-emphasising the realism aspect.

When the ball reaches the strikezone or a batter swings and makes contact with a ball, a "ghost" of the ball is left behind at the location where the impact
occurred. Using a circle outline mirrors how it is depicted on television in the real world as well. This impact point allows the player to know where the ball ended up. This allows you to appreciate really good (and nasty!) strikes that juuust clipped the zone while also knowing where exactly you made contact with the ball.

For the batter and pitcher, I searched up a couple of videos online that had the batter and pitcher from behind the home plate view(the perspective you play
as in the game). I then cropped out out a few frames manually to get a series of frames that depicted the sequence - the pitching motion for the pitcher and
the swinging motion of the batter. The result is a series of images that play to give the impression of the actual motion of a batter and pitcher.
