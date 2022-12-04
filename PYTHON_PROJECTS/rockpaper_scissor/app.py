import random
def play():
        user = input("what is your choice? r for rock, s for scissor,p for paper\n")
        computer = random.choice(['r','p','s'])
        print(computer)

        if user == computer:
            return 'it\'s a tie'

        if iswin(user,computer):
            return 'you won'

        return 'you lost'

def iswin(user, computer):
    #r>s,s>p,p>r
    if(user=='r' and computer == 's') or (user=='s' and computer == 'p') or (user=='p' and computer=='r'):
        return True

print(play())