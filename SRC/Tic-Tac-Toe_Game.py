import modules as functions

def main(): 
    player1Score = 0
    player2Score = 0  
    player1 = input(f'Enter Player1\'s name: ')
    print()
    player2 = input(f'Enter Player2\'s name: ')
    print()
    print(f"Welcome {player1} and {player2} to our game!")
    print()
    play_again = 'yes'
    while play_again == 'yes':
        topLeft = "1"
        topMiddle = "2"
        topRight = "3"
        middleLeft = "4"
        middleMiddle = "5"
        middleRight = "6"
        bottomLeft = "7"
        bottomMiddle = "8"
        bottomRight = "9"
        counter = 0
        functions.scoreBoard(player1,player2,player1Score,player2Score)
        functions.gameDesign(topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,bottomLeft,bottomMiddle,bottomRight)
        for play in range(1,10):
            if play%2 != 0:
                #X
                position = input(f"{player1} What's your move: ")
                symbol = "X"
                print()
                (topLeft,topMiddle,topRight,middleLeft,middleMiddle, middleRight,
                 bottomLeft,bottomMiddle,bottomRight, check) = functions.placing(position,symbol,topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,
                 bottomLeft,bottomMiddle,bottomRight)
                if check == True:
                    return
            if play%2 == 0:
                #O
                position = input(f"{player2} What's your move: ")
                symbol = "O"
                print()
                (topLeft,topMiddle,topRight,middleLeft,middleMiddle, middleRight,
                        bottomLeft,bottomMiddle,bottomRight, check) = functions.placing(position,symbol,topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,
                        bottomLeft,bottomMiddle,bottomRight)
                if check == True:
                    return
            winner = functions.victory(play,player1,player2)
            stop,counter,player1Score,player2Score = functions.winningCondition(winner,counter,topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,bottomLeft,
               bottomMiddle,bottomRight,player1,player1Score,player2Score)
            if stop == True:
                functions.scoreBoard(player1,player2,player1Score,player2Score)
                break
            else:
                if counter == 9:
                    print("We have a draw!")
                    functions.scoreBoard(player1,player2,player1Score,player2Score)
        counter = 0
        play_again = input("Do you want to play again?: ")
        print()
        if play_again == 'yes':
            player1,player2,player1Score,player2Score = functions.switch(player1,player2,player1Score,player2Score)        
    else:
        if player1Score > player2Score:
            print(f"The winner is {player1}!!")
        elif player1Score < player2Score:
            print(f"The winner is {player2}!!")
        else:
            print(f"We have a draw!!")
main()