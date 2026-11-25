# Decorator that wraps another function with password protection
def passwordProtect(func):

    # Wrapper asks for the password before calling the original function
    def wrapper():
        password = input('Enter the password to call the function:')
        if (password == 'password123'):
            print("Access granted.")
            func()
        else: 
            print("Access denied. Sorry, you need to enter the correct password to get the secret message.")

    return wrapper


# Apply password protection to printSecretMessage
@passwordProtect
def printSecretMessage():
    # Create the secret message and a decorative border
    secretMessage = "Shhh...this is a secret message"

    print("~" * len(secretMessage))
    print(secretMessage)
    print("~" * len(secretMessage))


# Calling this now runs the password-protected wrapper
printSecretMessage()