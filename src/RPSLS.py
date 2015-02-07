from random import randint
def name_to_number(name):
    if name.lower() == 'rock':
        n = 0
    elif name.lower() == 'spock':
        n = 1
    elif name.lower() == 'paper':
        n = 2
    elif name.lower() == 'lizard':
        n = 3
    elif name.lower() == 'scissors':
        n = 4
    else:
        print ("Not a valid name")
        return
    return n

def number_to_name(number):
    if number == 0:
        n = "rock"
    elif number == 1:
        n = "spock"
    elif number == 2:
        n = "paper"
    elif number == 3:
        n = "lizard"
    elif number == 4:
        n = "scissors"
    else:
        print ("Not a valid number")
        return
    return n

def rpsls(player_choice):
    print("Player chooses",player_choice)
    n = name_to_number(player_choice)
    cn = randint(0,4)
    computer_choice = number_to_name(cn)
    print("Computer chooses",computer_choice)
    result = (n-cn)%5
    if result == 0:
        print("Player and computer tie!\n")
    elif result == 1 or result ==2:
        print("Player wins!\n")
    else:
        print("Computer wins!\n")
rpsls("rock")
rpsls("paper")
rpsls("spock")
rpsls("lizard")
rpsls("scissors")