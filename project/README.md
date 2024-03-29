# BASED BALL : A baseball at-bat simulator
## Video Demo:  <URL HERE>
#### Description:
*Based Ball* is a simple simulator that allows you to face off and bat against two pitchers: Chris Sale (Left hand pitcher) and Jacob Degrom (Right Hand pitcher).

## Meet them all
The game consists of a few main assets

* Main `Finalproject.py` file

* Sounds

* Graphics (Images)

* `theme.json` file

* `button.py` supplementary button class file


### Finalproject.py(Main python file)
As this is the first python program I have written in full, please pardon the relatively poor standard of the code. With that being said, the main file contains a large selection of functions, and I will explain them in further detail below.

I utilised `pygame_gui` for most of the Graphical User Interface in the game, as I intended the GUI to be very simple and straightforward. Pygame_gui seemed to be relatively easy to implement, while retaining the ability to customise appearance through a theme file.

The first section of the code initialises and sets up the game. This includes the pygame setup of the screen, clock and mixer(for sound). Pygame_gui setup is also done here, such as initialising the manager and setting up the buttons and textboxes. Loading in of the graphic and audio resources is also done here.
The global game variables are also initalised here, like currentouts, currentstrikes, and others. These variables will be constantly changing with multiple functions making use of them.

### `draw_bases`, `homeplate` and `draw_static`
Pretty self-explanatory - they manage the display of the static elements that do not move during or in between at-bats. draw_bases is where the actual drawing of the base graphic occurs, while draw_static manages the actual logic that determines the correct graphic to be displayed depending on the value of "runners". Admittedly, the method used is very crude but it works (for now). The value of runners is stored as a three decimal place float, and the runners on base are determined by whether each decimal place is 1 or 0. For example, runner on first only is denoted by "0.100", while bases loaded(runners on each of the three bases) is denoted by "0.111". The value of runners is then changed by other functions and then draw_static updates the bases graphic accordingly.

### `check_menu`
Simply updates the menu_state if 3 outs have been made and then changes the `menu_state` to 3 to signal that the inning is over.

Next, I put all the screen.blit instances for every image into conviniently named functions to make them easier to call instead of copy pasting screen.blit everytime.

### `contact_hit_outcome` and `power_hit_outcome`
These functions serve to randomly determine the result of a hit. These functions will be called after it is determined that the player successfully gets a hit (which in turn is determined by having perfect timing and location of swing). Choosing to swing with a contact swing (pressing the "w" key) and getting a successful hit will call the contact_hit_outcome function. A contact hit will mean a much higher chance of getting a single (so called "weakest" possible outcome) and much lower chance of the other outcomes happening. Conversely, getting a hit with the Power Swing(pressing the "e" key) calls the power_hit_outcome, which gives a higher chance of the other outcomes occuring. This difference is balanced by making the power swing less forgiving than the contact swing, that means your timing has to be more accurate and on time to get a hit using a power swing as compared to using the contact swing. The four possible outcomes in each of these two functions are "Single", "Double", "Triple" and "Home Run". These two functions will then call another function, update_runners_and_score, to do the actual updating of the runners and score ("runs").

### `update_runners_and_score`
Serves to do the actual updating of "runners" and "runs" depending on the input. The input is an integer that represents the result to be updated, 1 represents single, 2 represents double, 3 represents triple and 4 represents home run. To keep things simple, all runners move up by the number of bases represented by the outcome. The function manually checks what is the current value of "runners", and then updates it according to the input, updating the "runs" variable also if any runs score.

- For example, a single is represented by 1, all runners will move up by 1 base. If there is currently a runner on first base (runners = 0.100), a single would result in runners on first and second (runners = 0.110) -> The runner on first moves to second, and the batter (guy that swung the bat) moves to first.

- Another example, if there is currently a runner on second (runners = 0.010), and the batter hits a double (2), the result will be a runner on second (0.010) and 1 run scores (runs += 1).The original runner on second moves 2 bases (2nd -> 3rd -> home) and scores (runs += 1) and the batter moves to second. (home -> 1st -> 2nd).

### `pitch_decision_maker` and `lefty_pitch_decision_maker`
Next up are the pitching decision trees for each of the two pitchers. Both utilise the same structure, albeit with slight differences in probabilities and pitch types chosen. Chris Sale (Left Hander) has 3 pitch types -> Fastball, Slider, Changeup. The pitch decision tree will randomly determine a pitch to choose depending on the current count (the current number of balls and strikes). Degrom (Right Hander) has the same 3 pitch types also. The decision tree works by altering the probabilities of each pitch type being thrown depending on the count. This is supplemented by the fact that each pitch type has different behaviours. For example, with Chris Sale, his fastball has a high probability of arriving in the zone (high likelihood of being a "strike") while his slider has a high probability of arriving outside the zone (high chance to be a ball). The pitching decision tree plays with this characteristic, to try to attain the most favourable outcome based on the relative risk to reward ratio. This is not completely realistic, because there is so many more factors to consider in real baseball, but sometimes you will see a similar decision making sequence in real life as well. While the probabilities are skewed in certain situations, the random element of it helps to maintain a little bit of realism, as just like real life, you have to be ready for any outcome. Even if you know something is more likely to happen, you still have to prepare for the possibility of something else happening.

Taking a closer look into the pitch decision tree for Chris Sale, we see something interesting.
- When the count is 0 balls and 0 strikes or 3 balls and 2 strikes, the probabilities are relatively evenly balanced, as the pitch type doesn't really have much of an impact in this situation.

- However, when the count is 0 balls and 2 strikes, the pitcher has a significant advantage here. We can see that the probability of throwing a slider is much higher here. It makes more sense to throw a slider (that likely arrives out of the zone) here because if the batter swings (all likely will miss), then they will strikeout with 3 strikes. Otherwise, if they do not swing, the count only goes to 1ball and 2 strikes.

- If the count is 3 balls and 0 strikes, the batter has the significant advantage here, as one more ball means they walk and get a free base. Therefore, we see that the decision maker has a much higher probability of throwing a fastball (High chance of arriving in the zone), to get a strike and avoiding walking the batter on 4 balls.

### Pitch Types
The different pitch types for each pitcher are represented by the next group of functions. These are the functions that are called when pitch_decision_maker selects a pitch type to use. These functions work by calling the main function to simulate the at-bat, `simulate`, and passing in some parameters that will determine how the pitch moves. These variables include: traveltime, breaktime, verticalspeed, horizontalspeed, verticalacceleration, horizontalacceleration, verticalbreak, horizontalbreak. There are also a few other less important parameters, such as pitchername to determine which pitcher is pitching, and ball_pos, used to determine the release point of the ball (which is affected by which pitcher is pitching). These parameters will be covered more in depth below, when we reach the `simulate` function. For these pitch type functions, an additional element of unpredictability is added by having `xoffset` and `yoffset` determined randomly in a range. These offsets will affect the pitch by changing it's initial trajectory. This can cause a fastball to arrive outside the zone, and can cause a slider to arrive in the zone. They also alter the way the pitch appears at the start, which is significant because the player relies on seeing and judging the way the ball moves at the start to decide whether to swing.

### `collision`
A simple function that checks whether a ball is touching a rectangle. This is used to check whether the ball touches the strikezone once it arrives at home plate, strike if it is touching, and ball otherwise. All credit goes to e-james, I used his answer on stackoverflow here:
https://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection

### `swing_start`, `high_swing_start` and `leg_kick`
These functions will play the respective animations, switching the image to be displayed according to the time that has elapsed since the function was first called. `swing_start` plays the low swing animation, `high_swing_start` plays the high swing animation, and `leg_kick` plays the default animation if the player does not swing.

### `draw_inning_summary` and `main_menu`
These are responsible for the summary screen and main menu. The text typing effect was implemented with the help of **LeMaster Tech's** great video: https://www.youtube.com/watch?v=DhK5P2bWznA.

The buttons were also put in with help from **Coding with Russ**'s nice tutorial: https://www.youtube.com/watch?v=G8MYGDf_9ho.

### `simulate`
This is the heart of  the game. It is responsible for the entire process of simulating the at-bat, including the pitcher's pitching motion, the batter's swing, the drawing of the ball as it moves towards home plate, and the management of all outcomes. A lot of things to talk about here, so I will go through some of the more important ones below.

### `simulate` - Important input parameters:

- `traveltime`, `breaktime`: traveltime determines how long the ball takes from leaving the pitchers hand to arriving at home plate. Fastballs take shorter time to reach the plate than sliders or changeups. breaktime determines when the ball starts to "break", which means when it starts to appear to move significantly. This is more important for pitches like sliders and changeups, which appear to "break" significantly, moving significantly in a different direction that it first appeared to move when just released out of the pitcher's hand.

- `verticalspeed`, `horizontalspeed`: These determine the ball's current velocity. The ball's initial velocity will be affected by the offset( mentioned in the pitch type functions above). The ball's velocity will also be constantly changing, first by verticalacceleration and horizontal acceleration, then later by verticalbreak and horizontalbreak.

- `verticalacceleration`, `horizontalaccceleration`, `verticalbreak`, `horizontalbreak`: These will update the ball's current verticalspeed and horizontalspeed once per cycle. verticalacceleration and horizontalacceleration apply to the ball initially, then verticalbreak and horizontalbreak take over after breaktime is reached. This is to create the appearance that the ball seems to move significantly after it travels a little from release, instead of moving immediately after release, which mirrors real life.

- `ball_pos` and `ball_size` : Pretty self explanatory, these reset the ball's size and position to the default values at release point from the pitcher's hand, depending on which pitcher it is.


### `simulate` - Key design choices:

- The function itself it set up like a decision tree, going doing different branches depending on the current time with respect to the starting time.

- To determine whether the player swung on time, the function compares the time that the barrel will first enter the zone (approximately 150ms from when the swing was initiated/button was first pressed) and compares that with the time the ball will actually arrive in the zone (`starttime` + `traveltime`). If this difference is too great, it will be registered as a swing and miss. If the difference is slight but not in the perfect range, it will be a foul, and if the difference is small enough, the swing will be set as perfect timing.

- High swing or Low swing is also simply determined by the position of the player's cursor at the moment that the button is pressed. If the y-coordinate of the cursor is above the middle of the zone, it is a high swing and vice versa.

- If it is determined that the timing is sufficiently off such that the player swung and miss, it will follow the same outcome as if the batter never swung. (except of course if the ball ends up outside the zone it would still be a strike because the player swung.) On the other hand, if the timing is foul or perfect, then the function goes down a different path. It will check, at the point of contact, whether the player's bat path(determined by high or low swing), will hit or miss the ball, and then determine and update the results accordingly. For example, if the hit timing is perfect, but the player swings high when the ball actually arrives low in the zone, the end result is still a swing and a miss.

- **To summarise, a hit will be the outcome if the following conditions are satisfied**:
    - Timing is in the perfect range. (Just right not too early not too late)
    - Swing path is correct (low swing if low ball and vice versa)
    - At the point of contact, the ball's current position falls within the boundaries. (The boundary for the low swing is the bottom half of the zone plus a buffer of approximately one ball diameter from the edges of the strike zone. Similar for the high swing.)

![High and low hit zones for high swing and low swing.](./Hitzones.png)
<br><sub>Approximate hit zones. Assuming your timing is on time, if you swing high and make contact in the blue zone, you will get a hit or foul. Otherwise you miss the ball. Same for low swing and the red zone.</sub>
<br><br>

- All the calculations for Foul balls and Hits are done at the moment of contact (The timing has to be in the appropiate range first). The position of the ball currently is checked and it is determined whether it is in the correct region (depending on whether it is a high swing or low swing) to be considered for a foul or hit to occur. If the swing path is correct and timing is correct, then it will process the outcome and update all the relevant information using functions like `power_hit_outcome` and `drawscoreboard`. Otherwise, if the swing path is off, it will default to the normal strike sequence. That is, the ball continues to complete it's trajectory and all the relevant information is updated as if it were a strike.


- For "called" strike and balls (when the player did not swing at all), as well as swinging strikes (player swung but missed the ball for whatever reason), all details are updated when the ball has finished it ball flight and arrived at the plate. Strikeouts and walks are also updated here. First it is checked whether the player swung, if the player did not swing, the ball's ending position is then checked to see if it is in or touching the zone. A ball is only awarded if all of these requirements are met:
    - Player did __not__ swing
    - Ball does __not__ end up in the zone or touching the zone

    All other scenarios will result in a strike.

### Main Game Loop

The main game loop deals with everything happening outside of the actual at-bat. That is, things such as menu states and the display of static elements. The `check_menu` function runs first every loop to check if the inning is over (3 outs). Then, depending on the current `menu_state`, the corresponding static elements such as the right buttons and images are drawn. Also, the next pitch can be triggered by either pressing the "PITCH" button or pressing "q" on the keyboard.

## Sounds
A few sounds were implemented: The glove pop sound (for when the ball hits the catcher's mitt aka the ball has finished travelling the full distance), the sounds when the bat makes contact with the ball, and the umpire call sounds.

The glove pop sound plays whenever the ball ends up in the catcher's mitt - basically any outcome other than the batter making contact with the ball.

The bat contact sounds include - Single, Double, Triple, Homerun. Each corresponds to the equivalent outcome and will play accordingly. I got these sounds from the videogame MLB the Show. Very crisp and nice sounds to give maximum satisfaction! There is also the foul sound for when a player fouls off a ball.

The umpire call sounds will play once the ball arrives in the zone without a swing. If you do not swing and the ball clips the zone, the called strike sound will play. If the above happens and it is the third strike, the third strike sound plays. On the flip side, if you do not swing and the ball lands outside the zone, the ball call sound plays.

## Graphics
To keep simple, I used coloured images for the hitter and the batter, while everything else is basically rendered in black and white.

The strikezone and home plate are rendered simply using the built in pygame draw function. The strikezone is a simple Rect and the homeplate is a polygon. The strikezone is also toggleable, for the player's preference. Generally, having the strikezone on makes it easier to determine whether a ball will be a ball or a strike.

For the ball, I used the pygame draw function to draw a circle that increases in size as time passes and it "approaches" the plate to give the impression that it is getting closer. I thought about bliting an actual image of the baseball onto the screen but found it very difficult because I would need to have multiple frames to depict the spinning motion of the ball. Further complicating things is the fact that different pitch types have the ball spin differently, so I would need separate sets of frames for different pitch types. I find that the simple solid circle would be sufficient to allow the player to get the point.

When the ball reaches the strikezone or a batter swings and makes contact with a ball, a "ghost" of the ball is left behind at the location where the impact occurred. You will see this in real world television broadcasts as well. This impact point allows the player to know where the ball ended up. This allows you to appreciate really good (and nasty!) strikes that juuust clipped the zone while also knowing where exactly you made contact with the ball.

For the batter and pitcher, I searched up a couple of videos online that had the batter and pitcher from behind the home plate view(the perspective you play as in the game). I then cropped out out a few frames manually to get a series of frames that depicted the sequence - the pitching motion for the pitcher and the swinging motion of the batter. The result is a series of images that play to give the impression of the motion of a batter and pitcher.

## `Theme.json` file
This is a simple theme file for the pygame_gui elements. Enables the `8bitoperator` font to be used for the buttons and banner.

## `button.py` file
A simple file to store the button class to be used in the main menu and end screen menu. Courtesy of Coding With Russ : https://www.youtube.com/watch?v=G8MYGDf_9ho.

## Converting to exe
Conversion to a zip file with exe was done with auto-py-to-exe -> https://pypi.org/project/auto-py-to-exe/

![High score!](./HIGHSCORE.png)
<br><sub>Look ma, high score!</sub><br><br><br>



> “Every day is a new opportunity. You can build on yesterday’s success or put its failures behind and start over again. That’s the way life is, with a new game every day, and that’s the way baseball is.” – Bullet Bob Feller



## Credits:
Batter images source video : https://www.youtube.com/watch?v=QXTfBIV5Edo
Pitcher images source videos: https://www.youtube.com/watch?v=xVMXjyv-4Gs (Chris Sale) and https://www.youtube.com/watch?v=EVJka2V3MhY (Jacob Degrom)
Sounds: https://www.youtube.com/watch?v=Z5tP0MpXUcw (Umpire call sounds) and https://www.youtube.com/watch?v=08MJLtBNbJI (MLB The Show 23 Bat sounds)
Tutorial for Button Classes: https://www.youtube.com/watch?v=G8MYGDf_9ho
Tutorial for text typwriter effect: https://www.youtube.com/watch?v=DhK5P2bWznA
pygame: https://www.pygame.org/news
pygame_gui: https://pygame-gui.readthedocs.io/en/v_069/
Auto-py-to-exe: https://pypi.org/project/auto-py-to-exe/