import random, pyfiglet

print(pyfiglet.figlet_format('Pick Colour'))

class Game:
    def __init__(self):
        user_wins = 0
        computer_wins = 0
        options = ['blue', 'red', 'black', 'green']
        while True:
            user_input = input('Enter: Blue/Red/Black/Green OR Enter Q to quit: ').lower()
            if user_input == 'q':
                break
            if user_input not in options:
                continue
            random_number = random.randint(0,3)
            computer_pick = options[random_number]
            print('computer_pick', computer_pick +'.')

            if computer_pick == user_input:
                print('You won!!!')
                user_wins += 1
            elif user_input != computer_pick:
                print('You lose')
                computer_wins +=1
            else: print('Try again.')
        print('computer_wins', computer_wins,'times.')
        print('You_wins', user_wins,'times.')
        print('\t\tThanks for Playing....')
game = Game()
