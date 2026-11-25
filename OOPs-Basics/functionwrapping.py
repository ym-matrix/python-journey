def passwordProtect(func):

    def wrapper():
        password = input('Enter the password to call the function:')
        if (password == 'password123'):
            print("Access granted.")
            func()
        else: 
            print("Access denied. Sorry, you need to enter the correct password to get the secret message.")

    return wrapper


@passwordProtect
def printSecretMessage():
    secretMessage = "Shhh...this is a secret message"

    
    print("~" * len(secretMessage))
    print(secretMessage)
    print("~" * len(secretMessage))


printSecretMessage()