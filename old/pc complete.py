#dice point system
player1_points = 0
player2_points = 0
player_1 = 'a'
player_2 = 'b'
rounds = 0
import random
#Player verification
verified_players=['laura','marta','diana','kemia','aleena','buckaroo','evan']
number_of_players=0
for i in range(1,3):
    print('Player ',i,":")
    user=str(input('Please enter your username: '))
    user = user.lower()
    if user in verified_players:
        print('Player',i,' access granted')
        if i == 1:
            player_1 = user
        else:
            player_2 = user
        number_of_players=number_of_players+1
    else:
        print('Player',i,' access denied')
        break
#dices
    if number_of_players == 2:
        while rounds != 5:
            rounds=rounds+1
            print ('---------- Round ',rounds,'----------')
            
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            dice3 = random.randint(1,6)
            dice4 = random.randint(1,6)
            print("The player1 dice1 scored:",dice1)
            print("The player1 dice2 scored:",dice2)
            print("The player2 dice1 scored:",dice3)
            print("The player2 dice2 scored:",dice4)
#player1 points and dice
            if dice1 % 2 == 0:
                print("Player1 dice1 is an Even Number")
                player1_points = player1_points+10
            else:
                print("Player1 dice1 is an Odd Number")
                if player1_points-5 < 0:
                    player1_points = player1_points+0
                else:
                    player1_points = player1_points-5

            if(dice2 % 2 == 0):
                print("Player1 dice2 is an Even Number")
                player1_points = player1_points+10
            else:
                print("Player1 dice2 is an Odd Number")
                if player1_points-5 < 0:
                    player1_points = player1_points+0
                else:
                    player1_points = player1_points-5

#player2 points and dice
            if(dice3 % 2 == 0):
                print("Player2 dice1 is an Even Number")
                player2_points = player2_points+10
            else:
                print("Player2 dice1 is an Odd Number")
                if player2_points-5 < 0:
                    player2_points = player2_points+0
                else:
                    player2_points = player2_points-5

            if(dice4 % 2 == 0):
                print("Player2 dice2 is an Even Number")
                player2_points=player2_points+10
            else:
                print("Player2 dice2 is an Odd Number")
                if player2_points-5 < 0:
                    player2_points = player1_points+0
                else:
                    player2_points = player1_points-5
            print("Player One's score: ",player1_points)
            print("Player Two's score: ",player2_points)
#Extra dices
        while player1_points == player2_points:
            print('----------EXTRA ROUND----------')
            if(dice1 % 2 == 0):
                print("Player1 dice1 is an Even Number")
                player1_points = player1_points+10
            else:
                print("Player1 dice1 is an Odd Number")
                if player1_points-5 < 0:
                    player1_points = player1_points+0
                else:
                    player1_points = player1_points-5

            if(dice2 % 2 == 0):
                print("Player1 dice2 is an Even Number")
                player2_points = player2_points+10
            else:
                print("Player1 dice2 is an Odd Number")
                if player2_points-5 < 0:
                    player2_points = player2_points+0
                else:
                    player2_points = player2_points-5
            if player1_points == player2_points:
                break

if player1_points > player2_points:
    print('Player 1 wins with', player1_points,'points')
    winner_points = player1_points
    winner_user = player_1
    winner = player_1
elif player1_points < player2_points:
    print('Player 2 wins with', player2_points,'points')
    winner_points = player2_points
    winner_user = player_2
    winner = player_2
else:
    print('...................................')
#LEADERBOARD
str(winner)
winner = (str(winner_points),',',winner_user)
f = open('Winner.txt', 'a')
f.write(''.join(winner))
f.write('\n')
f.close()

f = open('Leaderboard.txt', 'r')
leaderboard = [line.replace('\n','') for line in f.readlines()]
f.close()


for idx, item in enumerate(leaderboard):
    if item.split(', ')[1] == winner[1] and int(item.split(', ')[0]) < int(winner[0]):
            leaderboard[idx] = '{}, {}'.format(winner[0], winner[1])
    else:
        pass 
leaderboard.sort(reverse=True)

with open('Leaderboard.txt', 'w') as f:
    for item in leaderboard:
        f.write("%s\n" % item)
