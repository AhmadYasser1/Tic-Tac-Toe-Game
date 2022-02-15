def victory(play,player1,player2):
    if play%2 != 0:
        return player1
    else:
        return player2

def scoreBoard(player1,player2,player1Score,player2Score):
    lengthPlayer1 = len(player1)
    lengthPlayer2 = len(player2)
    dash = "-"
    print(f" {dash*(lengthPlayer1+4) + dash*(len(str(player1Score))-1)}       {dash*(lengthPlayer2+4) + dash*(len(str(player2Score))-1)}")
    print(f"|{player1}: {player1Score} |     |{player2}: {player2Score} |")
    print(f" {dash*(lengthPlayer1+4) + dash*(len(str(player1Score))-1)}       {dash*(lengthPlayer2+4) + dash*(len(str(player2Score))-1)}")
    print()

def gameDesign(topLeft,topMiddle,topRight,middleLeft,middleMiddle, middleRight,
                        bottomLeft,bottomMiddle,bottomRight):
    print(f" {topLeft} | {topMiddle} | {topRight} ")
    print("---|---|---")
    print(f" {middleLeft} | {middleMiddle} | {middleRight} ")
    print("---|---|---")
    print(f" {bottomLeft} | {bottomMiddle} | {bottomRight} \n")
    print()

def placing(position,symbol,topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,
                        bottomLeft,bottomMiddle,bottomRight):
    
    if position == '1':
        topLeft = symbol
        gameDesign(topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,bottomLeft,
            bottomMiddle,bottomRight)
        return (topLeft,topMiddle,topRight,middleLeft,middleMiddle, middleRight,
                    bottomLeft,bottomMiddle,bottomRight, False)
            
    elif position == '2':
        topMiddle = symbol
        gameDesign(topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,bottomLeft,
           bottomMiddle,bottomRight)
        return (topLeft,topMiddle,topRight,middleLeft,middleMiddle, middleRight,
                    bottomLeft,bottomMiddle,bottomRight, False)
            
    elif position == '3':
        topRight = symbol
        gameDesign(topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,bottomLeft,
           bottomMiddle,bottomRight)
        return (topLeft,topMiddle,topRight,middleLeft,middleMiddle, middleRight,
                    bottomLeft,bottomMiddle,bottomRight, False)
                   
    elif position == '4':
        middleLeft = symbol
        gameDesign(topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,bottomLeft,
               bottomMiddle,bottomRight)
        return (topLeft,topMiddle,topRight,middleLeft,middleMiddle, middleRight,
                    bottomLeft,bottomMiddle,bottomRight, False)
                   
    elif position == '5':
        middleMiddle = symbol
        gameDesign(topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,bottomLeft,
           bottomMiddle,bottomRight)
        return (topLeft,topMiddle,topRight,middleLeft,middleMiddle, middleRight,
                    bottomLeft,bottomMiddle,bottomRight, False)
                    
    elif position == '6':
        middleRight = symbol
        gameDesign(topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,bottomLeft,
           bottomMiddle,bottomRight)
        return (topLeft,topMiddle,topRight,middleLeft,middleMiddle, middleRight,
                    bottomLeft,bottomMiddle,bottomRight, False)
                    
    elif position == '7':
        bottomLeft = symbol
        gameDesign(topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,bottomLeft,
           bottomMiddle,bottomRight)
        return (topLeft,topMiddle,topRight,middleLeft,middleMiddle, middleRight,
                    bottomLeft,bottomMiddle,bottomRight, False)
            
    elif position == '8':
        bottomMiddle = symbol
        gameDesign(topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,bottomLeft,
           bottomMiddle,bottomRight)
        return (topLeft,topMiddle,topRight,middleLeft,middleMiddle, middleRight,
                    bottomLeft,bottomMiddle,bottomRight, False)
                  
    elif position == '9':
        bottomRight = symbol
        gameDesign(topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,bottomLeft,
           bottomMiddle,bottomRight)
        return (topLeft,topMiddle,topRight,middleLeft,middleMiddle, middleRight,
                    bottomLeft,bottomMiddle,bottomRight, False)
    else :
        print("Sorry, you messed up the game re-run the program to play again!")
        return (topLeft,topMiddle,topRight,middleLeft,middleMiddle, middleRight,
                    bottomLeft,bottomMiddle,bottomRight, True)
def winningCondition(winner,counter,topLeft,topMiddle,topRight,middleLeft,middleMiddle,middleRight,bottomLeft,
               bottomMiddle,bottomRight,player1,player1Score,player2Score):
   
    if topLeft == topMiddle and topMiddle == topRight:
        
        if winner == player1:
            player1Score += 1
        else:
            player2Score += 1
        print(f"{winner} wins")
        return True,counter,player1Score,player2Score
    
    elif middleLeft == middleMiddle and middleMiddle == middleRight:
        
        if winner == player1:
            player1Score += 1
        else:
            player2Score += 1
        print(f"{winner} wins")
        return True,counter,player1Score,player2Score
    
    elif bottomLeft == bottomMiddle and bottomMiddle == bottomRight:
        
        if winner == player1:
            player1Score += 1
        else:
            player2Score += 1
        print(f"{winner} wins")
        return True,counter,player1Score,player2Score
    
    elif topLeft == middleLeft and middleLeft == bottomLeft:
        
        if winner == player1:
            player1Score += 1
        else:
            player2Score += 1
        print(f"{winner} wins")
        return True,counter,player1Score,player2Score
    
    elif topMiddle == middleMiddle and middleMiddle == bottomMiddle:
        
        if winner == player1:
            player1Score += 1
        else:
            player2Score += 1
        print(f"{winner} wins")
        return True,counter,player1Score,player2Score
    
    elif topRight == middleRight and middleRight == bottomRight:
        
        if winner == player1:
            player1Score += 1
        else:
            player2Score += 1
        print(f"{winner} wins")
        return True,counter,player1Score,player2Score
    
    elif topLeft == middleMiddle and middleMiddle == bottomRight:
        
        if winner == player1:
            player1Score += 1
            
        else:
            player2Score += 1
        print(f"{winner} wins")
        return True,counter,player1Score,player2Score
    
    elif bottomLeft == middleMiddle and middleMiddle == topRight:
        
        if winner == player1:
            player1Score += 1
        else:
            player2Score += 1
        print(f"{winner} wins")
        return True,counter,player1Score,player2Score
    
    
    else:
        counter += 1
        return False,counter,player1Score,player2Score

def switch(player1,player2,player1Score,player2Score):

    check = input(f"Do you want to switch sides? ")

    if check == "yes":
        switch = player1
        switchScore = player1Score 
        player1 = player2
        player1Score = player2Score
        player2 = switch
        player2Score = switchScore

    return player1,player2,player1Score,player2Score