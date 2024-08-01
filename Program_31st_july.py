#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Devil
#
# Created:     31-07-2024
# Copyright:   (c) Devil 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
###Rock###
#Paper#
###Scissor Game###
import random

game ='''

  ____                    _   __    ________                                  _____
 |  _ >                  | | / /   |  ____  |                                / ____|          *
 | |_) \  ____     _____ | |/ /    | |    | |  __ _   _______   ___   _ ___ |  |__     _____  _   ____   ____    ____    _ ___
 |    /  /    \   |      |   /     | |____|_| / _` | |  ___  | / _ \ | |___| \____ \  |      | | /  __| /  __|  /    \  | |___|
 |  _ \ |      |  |      | |\ \    | |       | (_| | | |   | ||  __/ | |      ____) ) |      | | \___ \ \___ \ |      | | |
 |_| \_| \____/   |_____ |_| \_\   |_|        \__,_| | |___|_| \___| | |     |_____/  |_____ |_| |____/ |____/  \____/  | |
                                                     | |
                                                     | |
                                                     |_|
'''
rock = '''


        _______
-------`   ______)
        (__________)
        (_________)
        (________)
-----____(______)
'''
paper = '''
       _______
_____``    _____)____
           __________)
           ___________)
           __________)
-----,,____________)
'''
scissor = '''
      ____________
____,      ______)____
             _________)
        _______________)
        (_______)
-----__(_____)
'''
print(game)
games_images = [rock, paper, scissor]
user_choice = int(input("Enter Your Choice: Type 0 for Rock, 1 for Paper, 2 for Scissors"))
computer_choice = random.randint(0, 2)
print(f"Computer_chooose : {computer_choice}")

if user_choice >= 3 :
    print("You entered invaild number, You lose ")
else:
    print(games_images[user_choice])
    print("Computer choose```Downwards")
    print(games_images[computer_choice])
    if computer_choice == user_choice:
        print("It's a draw")
    elif computer_choice == 0 and user_choice == 2:# 0 FOR ROCK AND  Paper and scissor
        print('You lose')
    elif computer_choice == 0 and user_choice == 1:
        print('You Win')
    elif computer_choice == 1 and user_choice == 0:
        print('You lose')
    elif computer_choice == 1 and user_choice == 2:
        print('You Win')
    elif computer_choice == 2 and user_choice == 0:
        print('You Win')
    elif computer_choice == 2 and user_choice == 1:
        print('You lose')
