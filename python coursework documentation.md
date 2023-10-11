PYTHON PROGRAMING PROJECT

By laura gandia

**
**Introduction**

Computer science: the study of the design of algorithms, their properties and their linguistic and mechanical realisation.

**What is python?**

Python is an interpreted, general purpose programming language which conforms to multiple ways of programming paradigms. It is a high-level language as its written using codes that are similar to human read language.

**What is the aim of the project?**

For this controlled assessment I was given a choice of three projects to work on: a music game, a card game and a dice game. Each project had its different purpose and requirements to meet.  I chose the dice game

**The game**

The task was to develop a game where two authorised players roll two dices each, the points on the dice are added to the player’s score and an additional 10 points are added if the number on the dice is even or 5 points are taken away if the number is odd, although the score can never go below 0.

If they roll a double dice, an extra dice is rolled, and the score is added. And if by the end of the five rounds their score is the same, extra rounds take place with one dice each until the score isn’t the same. The winning score is then stored, and the top 5 scores are displayed at the end of the game along with the player’s name.

**Tasks**

1. Allow two players to enter their details, which are then authenticated to ensure that they are authorised players.
1. Allow each player to roll two 6-sided dice
1. Calculate and outputs the points for each round and each player’s total score
1. Allow the players to play 5 rounds
1. If both players have the same score after 5 rounds, allow each player to roll 1 die until someone wins
1. Outputs who has won at the end of the 5 rounds
1. Store the winner’s score with its name in an external file
1. Display the score and player name of the top 5 winning scores from the external file


**Task 1 - allows tow players to enter their details, which are then authenticated to ensure they are authorised players.**

The first task was quite straight forward and simple, and it’s quite easy to solve and spot any problems with it. I started by planning out how the code would work, what functions and what variables I would create in order for it to not only work efficiently but also fit in and work with the rest of the code that I would have to write for the other tasks. I decided to plan this roughly with a flow chart and wrote down some pseudocode within it.

My basic idea was to get a list and store the authorised player’s names and take input from the user and have it compared against the list, if the names were correct the users could go ahead and play the game. 

On the other hand, if the usernames were not on the list, the program would be killed, and they would not be able to play.


**THE CODE**

After this I started to write the code. I made a list of verified names that the player would be able to log in with and stored the list as a variable named ‘verified\_players’.

From there I went on to create the part of the code which would verify the players. I used iteration, to shorten and ease the maintainability of the code, to verify both player 1 and 2 using a “for range” and “if” statements. Within the “for range” statement the user is prompted to input their name, the name is then checked if it’s in the list and if it is, it is then the name is assigned to a variable named either ‘player\_1’ or ‘player\_2’ depending on how many players have been verified already.

I decided to make the program output whether the access had been granted for each user and used an if/else statement to kill the program if a wrong name was entered. I ran and tested the code multiple times using different names, wrong names and numbers to make sure the program worked as it should and didn’t give any unexpected errors. It worked perfectly.

**Task 2 – allows each player to roll two 6-sided dice.**

This second task was a bit trickier since I had to find a way for each person to roll two dices and for both dices to be random and independent from each other. I did some research and found a pre-existing function in python which could produce a completely random number within the given range. This function is called ‘random’.

My main idea for this task was to create four dices, two for each player. But I ended up making two different sets of dices, a two 12-sided dice set, and two 6-sided dice set. I did this to make the program shorter as the two dices for each players would have had to be added up anyway, so making one variable containing both dices reduces the amount of code I would have to write, and the other two 6 sided I decided to create them for the possible extra round that would have to take place if by the end of the 5 rounds the players had the same score.

**Task 3 – calculates and outputs the points for each round and each player’s total score.**

The task requested that two dices are rolled, both of the points on the dice are added up and added onto the score for each player, then if the sum of both numbers was even an extra ten points were added. If the result was odd, then five points were subtracted from the players’ scores, but the score could not go below zero. 

So, for this task I used the aforementioned 12-sided dices and proceeded to assign one to each player. This helped me shorten the code since by having a 12-sided dice meant that I didn’t need to write the code for the two rolls and adding up the points on the dice. I created a variable named ‘player1\_points’ and ‘player2\_points’ to store each player’s score and went on to write the code which added the dice score onto the points and then compared whether the points were even or odd, then based on that points were added or subtracted and the program outputted how many points each player had after each pair of rolls.

**Task 4 – allows the players to play 5 rounds.**

This task at first seemed quite hard, and at first I thought it would en-lengthen the code quite significantly since I had to repeat the codes for the previous steps five times, but when analysing it more carefully I realised it was actually quite simple and could use iteration to make this a much easier and less messy task. ![](Aspose.Words.2a38d52a-5dcf-4a44-9739-67017ef34cc3.009.png)![](Aspose.Words.2a38d52a-5dcf-4a44-9739-67017ef34cc3.010.png)

For the code I created a variable called rounds and assigned it the value 0, I created a while statement and used indentation to order everything that should be inside the loop. At the end of both players’ rolls I made the code add 1 to the rounds value and made the while statement until it rounds was equal to 5. 

**Task 5 – if both players have the same score after 5 rounds, allows each player to roll 1 die each until someone wins.**

For this task I needed to create extra rounds in case the score was even between players. This was actually quite simple. Outside of the while loop I made another while statement which compared both of the player’s scores and while the scores where the same the mechanics of task 3 were applied but this time with the 6-sided dices. Once the extra round was done, if the score was different the game ended, if it was still the same, another extra round was started, and the process would start again.

**Task 6 – outputs who have won at the end of the 5 rounds.**

This was again easy; I used the previously created variable for storing the player’s names and punctuation and made an if statement comparing the scores. Whoever had the highest score was outputted saying ‘Player X wins with Y points’ (X being the number of the winning player and Y being the number of points he had).

**Task 7 – stores the winner’s score, and their name, in an external file**

This task was one of the hardest yet since I struggle with file handling and decided to do quite a lot of research to decide which sort of external file, I should use to store the score and points. I decided to go for a text file since they are fairly easy to work with and don’t take up a lot of space. On the previous task I made two variables called winner and ‘winner\_points’ to shorten the code for the file writing.


I made it so that the code searched for a text file called score, and if it did not exist, a file with that name would be created. The code writes the score along the winner name and creates a different line at the end, so it is easier to read and is more organised. The file is then closed.

**Task 8 – displays the score and player name of the to 5 winning scores from the external file**

This task was also quite challenging, but I managed to find a way to order the scores and only display the top 5 scores, this took some time and was fairly challenging. The file is read line by line and then sorted, then when outputting the result, the list is reversed so only the last 5 would be the top 5. The 5 lines are outputted using an in-range statement.

**Full code and flow chart**
