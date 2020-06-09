import random

print('Rock-Paper-Scissors game [Type List To Show Result]'.center(60,"#"))
count_computer = 0
count_user = 0
count_equal = 0
Y = 'Y'
while Y == 'Y':
    choose = random.choice(['ROCK','SCISSORS','PAPER'])
    user = input('\nPlayer 1 ==> Choose (Rock or Paper or Scissors) Vs Computer : ').strip().upper()
    ############################################################################################
    
    if user == choose : # if equal Match 
        count_equal+=1 #count equal match
        print(f'\n#{count_equal} Equal Match \n')
        print(f'Computer ==> {choose} | Player 1 ==>  {user} ')
        
    ############################################################################################
     
    elif user == "ROCK" and choose == 'SCISSORS' : #Part for (user) to check if Win  
        count_user +=1 #count match that user winner 
        print (f'\n+ Player 1 Winner {count_user} Match win\n')
        print(f'Computer ==> {choose} | Player 1 ==>  {user} ')
        
    elif user == "SCISSORS" and choose == "PAPER":
        count_user +=1 #count match that user winner 
        print ('\n+ Player 1 Winner {count_user} Match win \n')
        print(f'Computer ==> {choose} | Player 1 ==>  {user} ')
        
    elif user == "PAPER" and choose == "ROCK":
        count_user +=1 #count match that user winner  
        print ('\n+ Player 1 The Winner {count_user} Match win \n')
        print(f'Computer ==> {choose} | Player 1 ==>  {user} ')
    ############################################################################################    
    elif user ==  'ROCK' or user == 'SCISSORS' or user == 'PAPER':
        
        count_computer+=1 #computer match that user winner 
        print(f'\n- Computer The Winner {count_computer} Match win \n')
        print(f'Computer ==> {choose} | Player 1 ==>  {user} ')
    ############################################################################################
    else:
        print('\nWrong entry ...Try Again')
        
    ############################################################################################   
    Y = input('\nWant To Play Again [Y/N] or (List) To Show Result : ').strip().capitalize()
    
    if Y != 'Y' and Y!= 'List': #Want Play Again ==> While = 'Y'
        print('Good Bye'.center(40,"#"))
        break
    
    elif Y == 'List': #To Show Result
        print(f'\n[-] Computer {count_computer} win \n[-] User {count_user} Win \n[-] Equal Match {count_equal}')
        
    ############################################################################################
    

input()
