"""
tic tac toe with numbers Game.
game created by Alaa Hossam Mohammed 
ID: 20210072

"""
 #draw the board of the game
play_board = {1: ' ',2: ' ',3: ' ',
              4: ' ',5: ' ',6: ' ',
              7: ' ',8: ' ',9: ' '}

# functhion for make the board of the game
def print_board(board):
    print(board[1] + '  |' + board[2] + '  |' + board[3])
    print('____________')
    print(board[4] + '  |' + board[5] + '  |' + board[6])
    print('____________')
    print(board[7] + '  |' + board[8] + '  |' + board[9])


# Funcution for the move in game and check if the move is valid or not
def move(turn):
    global place
    place = int(input('which place you want to move?'))
    if place in play_board:
        if play_board[place] == ' ':
            play_board[place] = str(turn)
        else:
            print('that place has been failed')
            return move(turn)
    else:
        print("there is no place like this")
        return move(turn)
    

turns = 0
winner =''
# list of the numbers the players and used to check the sum of numbers to check the winner
list_players = [200, 200 ,200,
                200, 200, 200,
                200, 200, 200]
# lists of odd and even numbers 
list_odd = [1, 3, 5, 7, 9]
list_even = [0, 2, 4, 6, 8]


# the code of the game
while turns < 5:
    # if condition to check if the player2 is win or not to make player1 play
    if winner != 'player2':
        # call the function of the board
        print_board(play_board)
        player1 = int(input('please enter an odd number:'))
        # check if the number valid or not
        while player1 not in list_odd:
            player1 = int(input('please enter another odd number:'))  
        list_odd.remove(player1)    
        turn = str(player1)
        #call the function of the place 
        move(turn)
        place -=1
        # add the number in the list pf players
        list_players[place] = player1
        # if condition to check if the player1 win or not
        if turns >= 2:
            for position in list_players:
                if list_players[0] + list_players[1] + list_players[2] == 15 or list_players[3] + list_players[4] + list_players[5] == 15 \
                or list_players[6] + list_players[7] + list_players[8] == 15 or list_players[0] + list_players[3] + list_players[6] == 15 \
                or list_players[1] + list_players[4] + list_players[7] == 15 or list_players[2] + list_players[5] + list_players[8] == 15 \
                or list_players[0] + list_players[4] + list_players[8] == 15 or list_players[2] + list_players[4] + list_players[6] == 15:
                    winner = "player1"
                    print_board(play_board)
                    print(f"Winner is {winner}")
                    break


    #if condition to check if the player1 or player2 win or not to allow the player2 play
    if winner != "player1" and winner != 'player2':
        # call the function of the board
        print_board(play_board)
        #if condition to check if player2 can play or not
        if turns < 4:
            player2 = int(input('please enter an even number:'))
            # check if the number valid or not
            while player2 not in list_even:
                player2 = int(input('please enter another even number:'))
            turn = str(player2)
            #call the function of the place
            move(turn)
            place -=1
            list_players[place] = player2
            list_even.remove(player2)
            turns += 1
        else:
            break
        #if condition to check if the player2 win or not
        if turns >= 2:
            for position in list_players:
                if list_players[0] + list_players[1] + list_players[2] == 15 or list_players[3] + list_players[4] + \
                list_players[5] == 15 or list_players[6] + list_players[7] + list_players[8] == 15 or list_players[0] + \
                list_players[3] + list_players[6] == 15 or list_players[1] + list_players[4] + list_players[7] == 15 or list_players[2] + \
                list_players[5] + list_players[8] == 15 or list_players[0] + list_players[4] + list_players[8] == 15 or list_players[2] + \
                list_players[4] + list_players[6] == 15:
                    winner = "player2"
                    print_board(play_board)
                    print(f"Winner is {winner}")
                    break
    else:
        break