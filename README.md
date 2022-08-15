# Rock-Paper-Scissors

A game of rock paper scissors where the uesr will play against the computer. The user uses the webcam which the computer translates the informaiton using a model into rock, paper or scissors. 

## Creating the model 

I created the models using https://teachablemachine.withgoogle.com/. Here I created 4 classes where I used my webcam to take continuous images to in order to train the model. This will be used to identify the user inputs. 
![image](https://user-images.githubusercontent.com/93881593/183495182-f3a96c4c-20f6-4436-8ebf-d883235f4bbc.png)

## Installing the depandancies 

Created virual enviroment using aconda. Installed the nessisary libraries and dependancies. Tested model using the file 'Rock-Paper-Scissors-Game.py'.
Then I created a manual way of playing rock, paper, scissors with the computer in file 'manual_rps.py'. Here the choice function form the random library picks an option for the computer. The players input is taken using the input function. These choices are passed into a get_winner function which compares the 2 and returns the ouput of the game as a string.

## Creating manual input Rock-Paper-Scissors

Crated file manual_rps.py as a manual rock, paper scissors game where the user types in their choice. Created functions 'get_user_choice', 'get_computer_choice' and 'get_winner' to read users input, randomly generate computers choice and compare the returned values to ouput the winner. 

## 

Created file 'camera_rps.py' for the game. Imported the file 'manual_rps.py' to use its functions. Installed the nessisary libraries and dependacies. First the function 'get_prediction' was made to return the users choice by using the keras model loaded in. The input is taken from the players camera. After a 5 second countdown the class with the highest probiblity is returned. This was passed into the imported function 'get_winner' with the previous 'get_computer_choice' to evaulate the winner and increment their score. The play function is looped until a score of 5 is achieved.

Inputs:
![image](https://user-images.githubusercontent.com/93881593/184707500-42566c4e-3bcd-4865-907e-1ac2184dd8f8.png)
![image](https://user-images.githubusercontent.com/93881593/184707628-02555853-cc3a-4ebc-bda9-5c191da8674e.png)
![image](https://user-images.githubusercontent.com/93881593/184707569-b7987eb5-8aad-41e0-a970-cd62241e4098.png)
![image](https://user-images.githubusercontent.com/93881593/184707890-22ae0e43-eba3-4abf-ac07-e8ce0867045f.png)

Output:

![image](https://user-images.githubusercontent.com/93881593/184708093-38a44ad2-ac52-4729-b758-08b2bad5fb9f.png)
