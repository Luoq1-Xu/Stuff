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


### Sounds
A few sounds were implemented: The glove pop sound (for when the ball hits the catcher's mitt), the sounds when the bat makes contact with the ball, and the umpire call sounds. Let's dive a bit deeper.

The glove pop sound plays whenever the ball ends up in the catcher's mitt - basically any outcome other than the batter making contact with the ball.

The bat contact sounds include - Single, Double, Triple, Homerun. Each corresponds to the equivalent outcome and will play accordingly. I got these sounds from the videogame MLB the Show. Very crisp and nice sounds to give maximum satisfaction!

The umpire call sounds will play once the ball arrives in the zone without a swing. If you do not swing and the ball clips the zone, the called strike sound will play. If the above happens and it is the third strike, the third strike sound plays. In Major League Baseball, usually umpires will have a more emphatic call when it is the called third strike. On the flip side, if you do not swing and the ball lands outside the zone, the ball call sound plays.

###Graphics
To keep simple, I used coloured images for the hitter and the batter, while everything else is basically rendered in black and white.

The strikezone and home plate are rendered simply using the built in pygame draw function. The strikezone is a simple Rect and the homeplate is a polygon.

For the ball, I used the pygame draw function to draw a circle that increases in size as time passes and it "approaches" the plate to give the illusion
that it is getting closer. I thought about using actual baseball images 

For the batter and pitcher, I searched up a couple of videos online that had the batter and pitcher from behind the home plate view(the perspective you play
as in the game). I then cropped out out a few frames manually to get a series of frames that depicted the sequence - the pitching motion for the pitcher and
the swinging motion of the batter. The result is a series of images that play to give the impression of the actual motion of a batter and pitcher.
