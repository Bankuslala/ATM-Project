name = input('What is your name? \n')
allowedUsers = ('Banke','Funmi','Manny','Tony')
allowedPassword = ('passwordBanke','passwordFunmi','passwordManny','passwordTony')

if(name in allowedUsers):
    password = input('Your Password? \n')
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):

        print('Welcome %s' % name)
        import datetime
        now = datetime.datetime.now()
        print('Current date and time is:')
        print(now.strftime('%y-%m-%d %H:%M:%S'))

        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Deposit')
        print('3. Complaint')

        selectedOption = int (input('Please select an option'))

        if(selectedOption == 1):
            Withdrawal= input(' How much would you like to withdraw \n')
            print('Take your cash')

        if(selectedOption == 2):
            Deposit= input ('How much would you like to deposit \n')
            print('Current balance')

        if(selectedOption == 3):
            Complaint = input ('What issue will you like to report? \n')
            print('Thank you for contacting us')


    else:
        print('Password incorrect, please try again')

else:
        print('Name not found, please try again')

        
def register():
    print ('******* Register **********')

    email = input('What is your email address? /n')
    first_name = input('What is your first name? /n')
    last_name = input ('What is your last nanme /n')
    password = input('create a password for yourself /n')

    accountNumber = generateAccountNumber ()

    database[accountNumber] = [first_name, last_name, email, password]

    print('Your Account has been created')
    print('== ==== ===== ==== ===')
    print('Your account number is : %d' % accountNumber)
    print('Make sure you keep it safe')
    print('== ==== ===== ==== ===')


    login()

def bankOperation (user):
    print('Welcomr %s %s' % (user[0], user[1] ))

    selectedOption = int(input('What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exist /n'))

    if (selectedOption == 1) :
         elif(selectedOption == 2):
        
        withdrawalOperation()
    elif(selectedOption == 3):
        
        logout()
    elif(selectedOption == 4):
        
        exit()
    else:
      
        print("Invalid option selected")
        bankOperation(user)


def withdrawalOperation():
    print("withdrawal")


def depositOperation():
    print("Deposit Operations")


def generationAccountNumber():

    return random.randrange(1111111111,9999999999)

def logout():
    login()



    
            
        
        
