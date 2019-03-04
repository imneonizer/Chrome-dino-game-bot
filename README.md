# Chrome-dino-game-bot
A python bot that plays Google Chrome's T-rex game
Hello folks!
This is an small tutorial on python native libraries to make a smiple Chrome's Famous Dino / T-Rex Game Bot

Follow along the tutorial to make your own game bot in just matter of minutes.

Step 1: Installation

So, if you are new to python or have never ever heard of it, don't worry i will get you covered.
and if you already have python installed in your computer, you can skip this step.
Go to the link to  https://www.python.org/downloads/ and download python foy your operating system i.e windows / Mac.

Step 2: Installing required libraries

Here comes the important step, for your bot to be able to run it requires some of the commmon and famous libraries of python
don't worry i will tell you how to install them aswell.
so, Here we go.
open up start menu if you are a windows user and search for cmd.exe
a terminal will be opened up just write below lines of codes to install required libraries.

>> pip install pyautogui
>> pip install pillow

so that wass it now we can go ahead to follow next steps.

Step 3: Getting hands on

Now just copy my repository you can clone-download the zip file.
After you will extract the files there is file called dino_bot.py which is the main file with the source code all other folders
are just my testing and deugging file which were created at the time when i was actually configuring the source code
as per my screen resolution.

don't worry you will be able to make yours as well. keep them incase you wanted to compare yours with mine :-)

After everything been done Let's quickly configure the source file so that it will be able to run in your computer.
P.s as this file captures the screen process images and do the calculations on raw pixel data it is important to note that different objects have different coordinates on different resolution computers.

what you have to do next is open up chrome, make sure you are offline drag the chrome window to left sade of the screen so it covers only half part of the screen and start the Dino game.. everybody Knows how to start them isn't that right. ok feed anything i the url box and hit enter game will eventually come up automatically.

you dont have to play the ame just hit space key so that game would start,what you have to do is whenever the largest tree come close to dino just take a screenshot do it twice to make sure you get the perfect one.

after that open up that image in any software like windows paint
here what we will try to do is take up the rectangle box tool and will make a rectangle box around that plant thhis will be the box where plants will get detected whenever they will uproach the dino.

and know open up the dino_bot.py side by side to fill in the values so on line 6 there is a variable named as "box_area1" with some values already assigned you have to replace them with yours. i will put a link to the video where i have explained eveything in details.
for know you have fill those coordinates values with yours which you can find in your screenshot after opening it with windows paint which you took earlier.
there are other variables also with the name of pixel_plant which are the coordinate postion of plant taking box as origin.
so thats it for this tutuorial, after filling in the values you can run the code and it will surely work.
follow the youtube video link to see the bot in action.
