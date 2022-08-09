# Rock-Paper-Scissors

A game of rock paper scissors where the uesr will play against the computer. The user uses the webcam which the computer translates the informaiton using a model into rock, paper or scissors. 

## Creating the model 

I created the models using https://teachablemachine.withgoogle.com/. Here I created 4 classes where I used my webcam to take continuous images to in order to train the model. This will be used to identify the user inputs. 
![image](https://user-images.githubusercontent.com/93881593/183495182-f3a96c4c-20f6-4436-8ebf-d883235f4bbc.png)

## Installing the depandancies 

Created virual enviroment using aconda. Installed the nessisary libraries and dependancies. Tested model using the file 'Rock-Paper-Scissors-Game.py'.
Then I created a manual way of playing rock, paper, scissors with the computer in file 'manual_rps.py'. Here the choice function form the random library picks an option for the computer. The players input is taken using the input function. These choices are passed into a get_winner function which compares the 2 and returns the ouput of the game as a string.
