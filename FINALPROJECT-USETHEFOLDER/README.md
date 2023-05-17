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
As this is the first python program I have written in full, please pardon the relatively poor standard of the code. I apologise in advance for the atrocious infractions that I may have committed in the process of writing this program... With that being said, the main file contains a large selection of functions, and I will explain them in further detail below.

I utilised pygame_gui for most of the Graphical User Interface in the game, as I intended the GUI to be very simple and straightforward. Pygame_gui seemed to be relatively easy to implement, while retaining the ability to customise appearance through a theme file.

The first section of the code initialises and sets up the game. This includes the pygame setup of the screen, clock and mixer(for sound). Pygame_gui setup is also done here, such as initialising the manager and setting up the buttons and textboxes. Loading in of the graphic and audio resources is also done here.
The global game variables are also initalised here, like currentouts, currentstrikes, and others. These variables will be constantly changing with multiple functions making use of them.

Next, we have some supplementary functions that assist the main game loop functions.

draw_bases, homeplate and draw_static are pretty self-explanatory - they manage the display of the static elements that do not move during or in between at-bats. draw_bases is where the actual drawing of the base graphic occurs, while draw_static manages the actual logic that determines the correct graphic to be displayed depending on the value of "runners". Admittedly, the method used is very crude but it works (for now). The value of runners is stored as a three decimal place float, and the runners on base are determined by whether each decimal place is 1 or 0. For example, runner on first only is denoted by "0.100", while bases loaded(runners on each of the three bases) is denoted by "0.111". The value of runners is then changed by other functions and then draw_static updates the bases graphic accordingly.














### Sounds
A few sounds were implemented: The glove pop sound (for when the ball hits the catcher's mitt), the sounds when the bat makes contact with the ball, and the umpire call sounds. Let's dive a bit deeper.

The glove pop sound plays whenever the ball ends up in the catcher's mitt - basically any outcome other than the batter making contact with the ball.

The bat contact sounds include - Single, Double, Triple, Homerun. Each corresponds to the equivalent outcome and will play accordingly. I got these sounds from the videogame MLB the Show. Very crisp and nice sounds to give maximum satisfaction!

The umpire call sounds will play once the ball arrives in the zone without a swing. If you do not swing and the ball clips the zone, the called strike sound will play. If the above happens and it is the third strike, the third strike sound plays. In Major League Baseball, usually umpires will have a more emphatic call when it is the called third strike. On the flip side, if you do not swing and the ball lands outside the zone, the ball call sound plays.

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
